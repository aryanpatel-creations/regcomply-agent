import pytest
from pii import mask_regex

CASES = [
    # 1. PAN
    ("My PAN is ABCDE1234F, please check", "My PAN is <PAN>, please check"),
    ("Shared PAN BKZPR8812K with branch", "Shared PAN <PAN> with branch"),
    ("Tax id is ALMPK4521Q for verification", "Tax id is <PAN> for verification"),
    # 2. Aadhaar
    ("Aadhaar 2345 6789 0123 was asked for", "Aadhaar <AADHAAR> was asked for"),
    ("UIDAI 9876-5432-1098 submitted", "UIDAI <AADHAAR> submitted"),
    ("Aadhaar no 345678901234 given", "Aadhaar no <AADHAAR> given"),
    # 3. Card
    ("Card 4111 1111 1111 1111 was charged twice", "Card <CARD> was charged twice"),
    ("Debit card 5555-4444-3333-2222 stolen", "Debit card <CARD> stolen"),
    ("Card 6011000011112222 debited", "Card <CARD> debited"),
    # 4. Phone
    ("Call me on +91 9876543210", "Call me on <PHONE>"),
    ("Call me on +91-9876543210", "Call me on <PHONE>"),
    ("Call me on 9876543210", "Call me on <PHONE>"),
    ("Mobile 09876543210 reachable", "Mobile <PHONE> reachable"),
    ("Contact number 8765432109", "Contact number <PHONE>"),
    ("Reach at 7123456789 urgently", "Reach at <PHONE> urgently"),
    ("Phone 6123456789 is primary", "Phone <PHONE> is primary"),
    # 5. IFSC
    ("Branch IFSC SBIN0001234", "Branch IFSC <IFSC>"),
    ("RTGS to HDFC0000128 IFSC", "RTGS to <IFSC> IFSC"),
    ("IFSC code ICIC0000001", "IFSC code <IFSC>"),
    # 6. Bank Account
    ("Account no 123456789012 at branch IFSC SBIN0001234", "Account no <ACCOUNT> at branch IFSC <IFSC>"),
    ("Transferred to account 10987654321 now", "Transferred to account <ACCOUNT> now"),
    ("Credit account 123456789", "Credit account <ACCOUNT>"),
    ("Savings a/c 112233445566778899 closed", "Savings a/c <ACCOUNT> closed"),
    ("A/c 19876543210 credited", "A/c <ACCOUNT> credited"),
    # 7. UPI
    ("Paid via ravi@okaxis yesterday", "Paid via <UPI> yesterday"),
    ("Sent via anjali.s@ybl", "Sent via <UPI>"),
    ("VPA sumit123@paytm used", "VPA <UPI> used"),
    ("UPI ID user@upi entered", "UPI ID <UPI> entered"),
    ("Payee merchant@axl charged", "Payee <UPI> charged"),
    ("Transfer to shop@ibl done", "Transfer to <UPI> done"),
    # 8. Email
    ("Mail ravi.k@example.com today", "Mail <EMAIL> today"),
    ("Write to support@bank-domain.co.in", "Write to <EMAIL>"),
    ("Query sent to fraud_alert+desk@test-bank.org", "Query sent to <EMAIL>"),
    # 9. Redacted CFPB
    ("On XX/XX/XXXX I was charged XXXX", "On <REDACTED> I was charged <REDACTED>"),
    ("Case XXXXXXXX logged", "Case <REDACTED> logged"),
    # 10. Multi-PII
    ("Call 9876543210 or email test@mail.com", "Call <PHONE> or email <EMAIL>"),
    ("PAN ABCDE1234F with phone 9876543210", "PAN <PAN> with phone <PHONE>"),
    # 11. Preserved: Amounts, Dates, Sections, Percentages (False Positive Checks)
    ("Fee of Rs 500 charged on 12 March 2026", "Fee of Rs 500 charged on 12 March 2026"),
    ("Complaint ref 2026/123 under section 10", "Complaint ref 2026/123 under section 10"),
    ("Charged $25.00 maintenance fee", "Charged $25.00 maintenance fee"),
    ("Penalty of INR 1500 levied", "Penalty of INR 1500 levied"),
    ("Transaction amount was Rs. 25,000 on 05/11/2024", "Transaction amount was Rs. 25,000 on 05/11/2024"),
    ("Under Section 8(1) and Clause 11 of the scheme", "Under Section 8(1) and Clause 11 of the scheme"),
    ("Interest rate of 8.5% was agreed", "Interest rate of 8.5% was agreed"),
    ("Late payment fee of Rs 750 plus 18% GST", "Late payment fee of Rs 750 plus 18% GST"),
    ("Dispute amount is Rs 100000 on account of fraud", "Dispute amount is Rs 100000 on account of fraud"),
    ("Loan tenure is 36 months with EMI 12500", "Loan tenure is 36 months with EMI 12500"),
    ("Notification dated 06 July 2017 circular 78", "Notification dated 06 July 2017 circular 78"),
    ("Overdraft limit of 50000 INR", "Overdraft limit of 50000 INR"),
]

@pytest.mark.parametrize("raw,expected", CASES)
def test_masking(raw, expected):
    assert mask_regex(raw)[0] == expected

def test_counts():
    _, counts = mask_regex("PAN ABCDE1234F and PAN PQRSX9876Z")
    assert counts == {"PAN": 2}
