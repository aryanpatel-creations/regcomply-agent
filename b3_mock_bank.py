"""Create a small fake core-banking database (all data is invented)."""
import random, sqlite3
from datetime import date, timedelta
import config

SCHEMA = """
CREATE TABLE customers   (customer_id TEXT PRIMARY KEY, name TEXT, segment TEXT, city TEXT);
CREATE TABLE accounts    (account_id TEXT PRIMARY KEY, customer_id TEXT, type TEXT, status TEXT,
                          balance_inr REAL);
CREATE TABLE transactions(txn_id TEXT PRIMARY KEY, account_id TEXT, txn_date TEXT, description TEXT,
                          amount_inr REAL, channel TEXT);
CREATE TABLE tickets     (ticket_id TEXT PRIMARY KEY, customer_id TEXT, opened TEXT, category TEXT,
                          status TEXT, assigned_team TEXT);
CREATE TABLE refund_requests(request_id TEXT PRIMARY KEY, ticket_id TEXT, amount_inr REAL, reason TEXT,
                          status TEXT, approved_by TEXT, created TEXT, UNIQUE(ticket_id, amount_inr));
"""
FIRST = ["Asha", "Ravi", "Meera", "Arjun", "Priya", "Kiran", "Neha", "Vikram"]
LAST = ["Rao", "Sharma", "Iyer", "Patel", "Das", "Nair", "Gupta", "Khan"]
CITIES = ["Pune", "Chennai", "Kolkata", "Jaipur", "Kochi", "Lucknow"]
DESCS = [("ATM withdrawal", "ATM"), ("UPI payment", "UPI"), ("Card purchase", "CARD"),
         ("Annual card fee", "FEE"), ("Overdraft charge", "FEE"), ("Salary credit", "NEFT")]


def build(path: str = config.BANK_DB, n_customers: int = 50, seed: int = 7):
    rnd = random.Random(seed)
    con = sqlite3.connect(path)
    con.executescript("".join(f"DROP TABLE IF EXISTS {t};" for t in
                              ["customers", "accounts", "transactions", "tickets", "refund_requests"]) + SCHEMA)
    today = date(2026, 11, 1)
    for i in range(1, n_customers + 1):
        cid, aid = f"C{i:04d}", f"A{i:04d}"
        con.execute("INSERT INTO customers VALUES (?,?,?,?)",
                    (cid, f"{rnd.choice(FIRST)} {rnd.choice(LAST)}", rnd.choice(["Retail", "Premier"]),
                     rnd.choice(CITIES)))
        con.execute("INSERT INTO accounts VALUES (?,?,?,?,?)",
                    (aid, cid, rnd.choice(["Savings", "Current"]), rnd.choice(["Active"] * 9 + ["Frozen"]),
                     round(rnd.uniform(500, 250000), 2)))
        for j in range(12):
            desc, ch = rnd.choice(DESCS)
            amt = round(rnd.uniform(100, 20000), 2) * (1 if desc == "Salary credit" else -1)
            con.execute("INSERT INTO transactions VALUES (?,?,?,?,?,?)",
                        (f"T{i:04d}{j:02d}", aid, str(today - timedelta(days=rnd.randint(0, 60))), desc, amt, ch))
        if rnd.random() < 0.6:
            con.execute("INSERT INTO tickets VALUES (?,?,?,?,?,?)",
                        (f"K{i:04d}", cid, str(today - timedelta(days=rnd.randint(0, 40))),
                         rnd.choice(["Charges", "Card dispute", "Account access", "Delay"]),
                         rnd.choice(["Open", "Open", "Awaiting customer", "Closed"]),
                         rnd.choice(["Cards", "Savings & Current", "Digital Banking"])))
    con.commit()
    con.close()


if __name__ == "__main__":
    build()
    print("Mock bank created at", config.BANK_DB)
