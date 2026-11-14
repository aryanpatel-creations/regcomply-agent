"""The shapes of everything the model must return. Pydantic validates them."""
from typing import Literal
from pydantic import BaseModel, Field


class Triage(BaseModel):
    is_complaint: bool
    category: Literal["Charges", "Card dispute", "Account access", "Delay", "Fraud", "Other"]
    product: Literal["Cards", "Accounts", "Payments", "Other"]
    urgency: Literal["low", "medium", "high"]
    search_query: str = Field(description="Short query to find the relevant RBI rules")
    confidence: float = Field(ge=0, le=1)


class ChecklistItem(BaseModel):
    requirement: str
    status: Literal["met", "not_met", "check"]
    citation: str = Field(description="chunk_id that states the requirement")


class Draft(BaseModel):
    reply: str = Field(description="Reply to the customer, for the agent to review")
    cited_chunk_ids: list[str]
    checklist: list[ChecklistItem]
    proposed_refund_inr: float = 0
    confidence: float = Field(ge=0, le=1)
