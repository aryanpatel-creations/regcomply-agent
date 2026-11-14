"""One small client for every free model option.

chat_json(): ask for JSON that matches a Pydantic model; validates it and retries once.
embed():     turn texts into vectors (Ollama only; the cloud demo uses BM25 instead).
"""
import json, time
import requests
from pydantic import BaseModel, ValidationError
import config


def _ollama_chat(messages, schema):
    for attempt in range(3):
        try:
            r = requests.post(f"{config.OLLAMA_URL}/api/chat", timeout=180, json={
                "model": config.CHAT_MODEL, "messages": messages, "stream": False,
                "format": schema, "options": {"temperature": 0, "num_predict": 400}})
            r.raise_for_status()
            data = r.json()
            usage = {"input_tokens": data.get("prompt_eval_count", 0), "output_tokens": data.get("eval_count", 0)}
            return data["message"]["content"], usage
        except (requests.RequestException, requests.exceptions.Timeout):
            if attempt == 2:
                raise
            time.sleep(3)


def _openai_compat_chat(messages, schema, name):
    body = {"model": config.CHAT_MODEL, "messages": messages, "temperature": 0}
    if config.JSON_MODE == "schema":
        body["response_format"] = {"type": "json_schema",
                                   "json_schema": {"name": name, "schema": schema}}
    elif config.JSON_MODE == "object":
        body["response_format"] = {"type": "json_object"}
    for attempt in range(4):                                   # free tiers rate-limit: back off on 429
        base_url = config.API_BASE_URL.rstrip("/")
        r = requests.post(f"{base_url}/chat/completions", timeout=120, json=body,
                          headers={"Authorization": f"Bearer {config.API_KEY}"})
        if r.status_code != 429:
            break
        time.sleep(2 ** attempt * 5)
    r.raise_for_status()
    data = r.json()
    u = data.get("usage", {})
    usage = {"input_tokens": u.get("prompt_tokens", 0), "output_tokens": u.get("completion_tokens", 0)}
    return data["choices"][0]["message"]["content"], usage


def chat_json(system: str, user: str, model_cls: type[BaseModel]) -> tuple[BaseModel, dict]:
    """Returns (validated object, usage dict with tokens and latency)."""
    schema = model_cls.model_json_schema()
    system = f"{system}\n\nReply with JSON only, matching this schema:\n{json.dumps(schema)}"
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    start = time.perf_counter()
    for attempt in range(2):
        if config.LLM_PROVIDER == "ollama":
            raw, usage = _ollama_chat(messages, schema)
        else:
            raw, usage = _openai_compat_chat(messages, schema, model_cls.__name__)
        try:
            obj = model_cls.model_validate_json(raw)
            usage["latency_ms"] = int(1000 * (time.perf_counter() - start))
            usage["retries"] = attempt
            return obj, usage
        except ValidationError as e:                            # show the model its mistake once
            messages += [{"role": "assistant", "content": raw},
                         {"role": "user", "content": f"That JSON was invalid: {e.errors()[:3]}. Try again."}]
    raise ValueError(f"Model did not return valid {model_cls.__name__} JSON")


def embed(texts: list[str], batch: int = 32) -> list[list[float]]:
    vectors = []
    for i in range(0, len(texts), batch):
        r = requests.post(f"{config.OLLAMA_URL}/api/embed", timeout=300,
                          json={"model": config.EMBED_MODEL, "input": texts[i:i + batch]})
        r.raise_for_status()
        vectors += r.json()["embeddings"]
    return vectors
