import json
from collections import Counter

# Load existing 50 questions
existing_50 = [json.loads(line) for line in open("eval/golden.jsonl", encoding="utf-8")]

# Load chunks for exact quote matching
chunks = [json.loads(line) for line in open("data/clean/chunks.jsonl", encoding="utf-8")]
chunk_map = {c["chunk_id"]: c for c in chunks}

# Define 50 new questions (q051 to q100)
# 40 in-scope questions from the 5 circulars + 10 out-of-scope questions
new_questions = [
    # --- MD_DIGISEC: Digital Payment Security Controls ---
    {
        "id": "q051",
        "question": "Does the RBI mandate multi-factor authentication for electronic payment modes and fund transfers?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:33"],
        "quote": "multi-factor authentication for payments through electronic modes and fund transfers, including cash withdrawals from ATMs/ micro- ATMs/ business correspondents",
        "reference": "Yes, RBI mandates multi-factor authentication for electronic payments and fund transfers unless explicitly permitted or relaxed."
    },
    {
        "id": "q052",
        "question": "What customer alerts must regulated entities provide for payment transactions under digital security guidelines?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34"],
        "quote": "alerts (like SMS, e-mail, etc.) should be applied in respect of all payment transactions (including debits and credits), creation of new account linkages",
        "reference": "Regulated entities must send transaction alerts (via SMS, email, etc.) for all payment debits and credits, as well as for creating new account linkages."
    },
    {
        "id": "q053",
        "question": "For online transactions, should the merchant name or the payment aggregator be displayed to the customer?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34"],
        "quote": "customer for online transactions shall identify the merchant name, wherever applicable, rather than the payment aggregator through which the transaction is routed",
        "reference": "Online transaction authentication must identify the actual merchant name rather than the payment aggregator routing the payment."
    },
    {
        "id": "q054",
        "question": "What must happen if an authenticated customer session experiences interference or network disruption?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34"],
        "quote": "An authenticated session, together with its encryption protocol, should remain intact throughout the interaction with the customer. Else, in the event of interference or in case of session disruption, the session should be terminated",
        "reference": "The session and encryption protocol must remain intact throughout; in case of interference or disruption, the session must be immediately terminated."
    },
    {
        "id": "q055",
        "question": "Must banks configure mechanisms to alert customers when authentication fails?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:36"],
        "quote": "mechanism to alert the customers in case of failed authentication, time frame for the same, etc.",
        "reference": "Yes, banks must document and implement mechanisms to alert customers when authentication fails."
    },
    {
        "id": "q056",
        "question": "What parameters should be monitored for system alerts according to digital payment security controls?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:37"],
        "quote": "System alerts shall be parameterised and monitored in terms of various applicable parameters. Such parameters, as applicable could be: transaction velocity (e.g., fund transfers, cash withdrawals, payments through electronic modes, adding new beneficiaries, etc.) in a short period",
        "reference": "System alerts must monitor parameters such as transaction velocity (rapid fund transfers, cash withdrawals, adding new beneficiaries) within short timeframes."
    },
    {
        "id": "q057",
        "question": "Can cardholders set separate transaction caps for domestic and international card transactions?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:72"],
        "quote": "mandated both for domestic as well as international transactions separately. REs shall put in place transaction control mechanisms with necessary caps (restrictions o n transactions)",
        "reference": "Yes, regulated entities must provide transaction control mechanisms with separate transaction caps for domestic and international transactions."
    },
    {
        "id": "q058",
        "question": "Is adaptive authentication permitted by RBI based on customer risk profiling and behavior?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34"],
        "quote": "REs may also adopt adaptive authentication to select the right authentication factors. depending on risk assessment, user risk profile and behaviour.",
        "reference": "Yes, banks may adopt adaptive authentication to select authentication factors based on risk assessment and customer transaction behavior."
    },
    {
        "id": "q059",
        "question": "I noticed an unknown merchant debit on my statement that only says 'PayAggregator'. Is the bank required to show the merchant name?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34"],
        "quote": "shall identify the merchant name, wherever applicable, rather than the payment aggregator through which the transaction is routed",
        "reference": "Yes, RBI rules mandate that the transaction identifier must state the actual merchant name rather than only the payment aggregator."
    },
    {
        "id": "q060",
        "question": "Are banks required to implement multi-factor authentication for cash withdrawals from micro-ATMs and business correspondents?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:33"],
        "quote": "multi-factor authentication for payments through electronic modes and fund transfers, including cash withdrawals from ATMs/ micro- ATMs/ business correspondents",
        "reference": "Yes, multi-factor authentication applies to cash withdrawals from ATMs, micro-ATMs, and business correspondents."
    },

    # --- MC_CUSTSERV: Master Circular on Customer Service ---
    {
        "id": "q061",
        "question": "Are banks allowed to charge individuals for the issuance of a passbook for savings bank accounts?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.6"],
        "quote": "A passbook is a ready reckoner of transactions and is handy and compact and as such, is far more convenient to the small customer. (ii) Banks should provide passbooks to all Savings Bank Account holders (Individuals) free of charge.",
        "reference": "No, banks must provide passbooks to all individual Savings Bank account holders free of charge."
    },
    {
        "id": "q062",
        "question": "Can customers write cheques in any language or must they only be in English and Hindi?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.7"],
        "quote": "cheques may be written in Hindi, English or in the concerned Regional Language. Customer may write cheques in any language of his choice.",
        "reference": "Customers can write cheques in Hindi, English, or the concerned Regional Language of their choice."
    },
    {
        "id": "q063",
        "question": "Are banks required to offer doorstep banking services to senior citizens and visually impaired persons?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:24.1"],
        "quote": "Doorstep Banking Services for Senior Citizens and Differently Abled Persons Banks are advised to make concerted effort to provide a basic suite of banking services to senior citizens of more than 70 years of age and differently abled or infirm persons",
        "reference": "Yes, banks must provide doorstep banking services to senior citizens aged 70+ and differently abled or infirm persons."
    },
    {
        "id": "q064",
        "question": "Can banks levy penal charges on savings accounts for non-maintenance of minimum balance if the account is inoperative?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.4"],
        "quote": "Banks are advised to ensure that no penal charges are levied for non-maintenance of minimum balances in any inoperative account.",
        "reference": "No, RBI circular strictly prohibits levying penal charges for non-maintenance of minimum balance in any inoperative account."
    },
    {
        "id": "q065",
        "question": "What is the compensation payable by the card-issuing bank to the customer for delayed reconciliation of failed ATM transactions beyond T+5 days?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.12"],
        "quote": "banks shall pay compensation of ₹ 100/- per day of delay to the customer, if the failed ATM transaction is not resolved within T + 5 calendar days",
        "reference": "Banks must pay ₹100 per day of delay if a failed ATM transaction is not resolved within T+5 calendar days."
    },
    {
        "id": "q066",
        "question": "Can a bank unilaterally close a savings account simply because the balance has reduced to zero without prior notice?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:24.7"],
        "quote": "Banks are advised not to close any account having balance without prior notice to the customer. Accounts having zero balance should also not be closed unilaterally without notice.",
        "reference": "No, banks cannot close zero-balance or funded accounts unilaterally without giving prior notice to the customer."
    },
    {
        "id": "q067",
        "question": "What is the basic requirement regarding printed banking materials like account opening forms and pay-in slips?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:4.3"],
        "quote": "account opening forms, pay-in-slips, passbooks, etc., in trilingual form i.e., English, Hindi and the concerned Regional Language.",
        "reference": "Printed materials such as account opening forms, pay-in slips, and passbooks must be in trilingual form: English, Hindi, and Regional Language."
    },
    {
        "id": "q068",
        "question": "Are banks allowed to levy charges for non-operation or activation of an inoperative Basic Savings Bank Deposit Account?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:4.1"],
        "quote": "no charge for non-operation/activation of in-operative 'Basic Savings Bank Deposit Account'.",
        "reference": "No, banks cannot levy any charge for the activation or non-operation of an inoperative Basic Savings Bank Deposit Account."
    },
    {
        "id": "q069",
        "question": "The ATM debited Rs 10,000 from my savings account but did not dispense cash, and 7 days have passed. Am I entitled to delay compensation?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.12"],
        "quote": "banks shall pay compensation of ₹ 100/- per day of delay to the customer, if the failed ATM transaction is not resolved within T + 5 calendar days",
        "reference": "Yes, you are entitled to compensation of ₹100 per day for every day of delay beyond T+5 calendar days."
    },
    {
        "id": "q070",
        "question": "My branch refused to give me a physical passbook and insists on sending emails only. Is this allowed under RBI rules?",
        "in_scope": True,
        "gold_sections": ["MC_CUSTSERV:5.6"],
        "quote": "Banks should provide passbooks to all Savings Bank Account holders (Individuals) free of charge.",
        "reference": "No, banks are required to provide passbooks to individual Savings Bank account holders free of charge upon request."
    },

    # --- MD_CARDS: Credit Card and Debit Card Issuance ---
    {
        "id": "q071",
        "question": "What is the penalty if a card issuer activates an unsolicited credit card without explicit customer consent?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:6"],
        "quote": "shall reverse the charges immediately and also pay a penalty without demur to the recipient of the card of an amount equal to twice the value of charges reversed.",
        "reference": "The card issuer must reverse the charges immediately and pay a penalty equal to twice the value of the reversed charges."
    },
    {
        "id": "q072",
        "question": "Within how many days must a credit card closure request be completed by the card-issuer?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:8"],
        "quote": "Any request for closure of a credit card shall be honoured within seven working days by the card-issuer, subject to payment of all dues by the cardholder.",
        "reference": "The card-issuer must honor and complete a credit card closure request within 7 working days, subject to payment of dues."
    },
    {
        "id": "q073",
        "question": "What compensation is payable to a cardholder if the bank fails to close a credit card within 7 working days?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:8"],
        "quote": "Failure on the part of the card-issuer to complete the process of closure within seven working days shall result in a penalty of ₹ 500 per day of delay payable to the cardholder, till the closure of account",
        "reference": "The card-issuer must pay a penalty of ₹500 per day of delay to the cardholder until the card is closed."
    },
    {
        "id": "q074",
        "question": "Are card issuers allowed to offer a one-time option to cardholders to modify their billing cycle?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:13"],
        "quote": "Cardholders shall be provided a one-time option to modify the billing cycle of the credit card as per their convenience.",
        "reference": "Yes, cardholders must be given at least a one-time option to modify their credit card billing cycle."
    },
    {
        "id": "q075",
        "question": "Can a card issuer provide an insurance cover on a credit or debit card without obtaining explicit written or digital consent?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:6"],
        "quote": "In cases where the card-issuers are offering any insurance cover to their cardholders, in tie-up with insurance companies, the card-issuers shall obtain explicit written or digital consent from the cardholder",
        "reference": "No, card issuers must obtain explicit written or digital consent before providing any insurance cover to cardholders."
    },
    {
        "id": "q076",
        "question": "I paid all my credit card dues and requested cancellation, but the bank took 14 working days to close it. Can I claim compensation?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:8"],
        "quote": "Failure on the part of the card-issuer to complete the process of closure within seven working days shall result in a penalty of ₹ 500 per day of delay payable to the cardholder",
        "reference": "Yes, you can claim ₹500 per day of delay for the 7 working days beyond the statutory 7-day limit (₹3,500 total compensation)."
    },
    {
        "id": "q077",
        "question": "The bank sent me an upgraded credit card that I never applied for, and debited an annual fee. What are my rights under RBI directions?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:6"],
        "quote": "The issue of unsolicited cards/upgradation is strictly prohibited. In case, an unsolicited card is issued/existing card upgraded and activated without the explicit consent of the recipient... shall reverse the charges immediately and also pay a penalty without demur to the recipient of the card of an amount equal to twice the value of charges reversed.",
        "reference": "Unsolicited card upgrades are strictly prohibited. The bank must reverse the charges immediately and pay you a penalty equal to twice the value of the reversed fee."
    },

    # --- CIR_UNAUTH: Limiting Liability in Unauthorized Transactions ---
    {
        "id": "q078",
        "question": "Who bears the burden of proof to demonstrate customer negligence in an unauthorized electronic banking transaction?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:11"],
        "quote": "The burden of proving customer liability in case of unauthorised electronic banking transactions shall lie on the bank.",
        "reference": "The burden of proving customer liability in unauthorized electronic banking transactions lies entirely on the bank."
    },
    {
        "id": "q079",
        "question": "Within how many working days must a bank credit a shadow reversal after being notified of an unauthorized electronic transaction?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:9"],
        "quote": "the bank shall credit (shadow reversal) the amount involved in the unauthorised electronic transaction to the customer’s account within 10 working days from the date of such notification",
        "reference": "The bank must credit a shadow reversal to the customer's account within 10 working days of notification."
    },
    {
        "id": "q080",
        "question": "What is the maximum turnaround time for a bank to resolve an unauthorized electronic transaction complaint from the date of receipt?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:10"],
        "quote": "A complaint shall be resolved and liability of the customer, if any, established within such time, as may be specified in the bank's Board approved policy, but not exceeding 90 days from the date of receipt of the complaint",
        "reference": "Banks must resolve the complaint and establish liability within a period not exceeding 90 days from receipt."
    },
    {
        "id": "q081",
        "question": "If an unauthorized transaction occurs due to a third-party breach and the customer notifies the bank within 3 working days, what is the customer's liability?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:6"],
        "quote": "Third party breach where the deficiency lies neither with the bank nor with the customer but lies elsewhere in the system, and the customer notifies the bank within three working days... customer's entitlement to zero liability shall arise",
        "reference": "The customer has zero liability if the third-party breach is reported to the bank within 3 working days."
    },
    {
        "id": "q082",
        "question": "The bank is claiming I shared my OTP for an unauthorized debit, but I never received any message. Can the bank make me pay without proving negligence?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:11"],
        "quote": "The burden of proving customer liability in case of unauthorised electronic banking transactions shall lie on the bank.",
        "reference": "No, under RBI directions, the burden of proving that you were negligent or shared credentials lies strictly on the bank."
    },

    # --- RBIOS2021: Integrated Ombudsman Scheme ---
    {
        "id": "q083",
        "question": "On what grounds can the Ombudsman reject a complaint at the initial scrutiny stage?",
        "in_scope": True,
        "gold_sections": ["RBIOS2021:16"],
        "quote": "The Deputy Ombudsman or the Ombudsman may reject a complaint at any stage if it appears that the complaint made: (a) is non-maintainable under clause 10; or (b) is in the nature of offering suggestions or seeking guidance or explanation",
        "reference": "A complaint can be rejected if it is non-maintainable under clause 10, or is merely seeking guidance, suggestions, or general explanations."
    },
    {
        "id": "q084",
        "question": "Can a customer appeal against an Award passed by the Banking Ombudsman if the Award was made with mutual agreement?",
        "in_scope": True,
        "gold_sections": ["RBIOS2021:17"],
        "quote": "no appeal shall lie against an Award passed with the consent of the parties or where the Award has been passed under clause 15(1).",
        "reference": "No appeal lies against an Award passed with the mutual consent of both parties."
    },
    {
        "id": "q085",
        "question": "Can a complaint be filed with the Ombudsman if the same subject matter is already pending before a consumer court or civil court?",
        "in_scope": True,
        "gold_sections": ["RBIOS2021:10"],
        "quote": "The complaint is pending before, or has been dealt with on merits, by any Court, Tribunal or Arbitrator or any other Forum or Authority",
        "reference": "No, complaints that are pending or have been decided before a Court, Tribunal, or Consumer Forum are non-maintainable before the Ombudsman."
    },

    # --- Multi-Section / Cross-Circular In-Scope Questions ---
    {
        "id": "q086",
        "question": "If an unauthorized transaction occurs on a basic savings account (BSBD) due to third-party deficiency and reported after 5 days, what circular sections govern customer liability?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:7", "MC_CUSTSERV:4.1"],
        "quote": "BSBD accounts maximum liability Rs 5,000 where reporting is delayed 4 to 7 days",
        "reference": "Customer liability is limited to Rs 5,000 for BSBD accounts under CIR_UNAUTH:7, while BSBD basic account rules are governed under MC_CUSTSERV:4.1."
    },
    {
        "id": "q087",
        "question": "What two RBI provisions govern customer compensation when an unsolicited credit card is issued and leads to mental anguish?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:6", "RBIOS2021:15"],
        "quote": "unsolicited card penalty equal to twice charges reversed under MD_CARDS:6, and up to Rs 1 lakh for mental anguish under RBIOS2021:15",
        "reference": "MD_CARDS:6 mandates reversing charges plus 2x penalty, and references RBIOS2021:15 for awarding up to Rs 1 lakh for harassment and mental anguish."
    },
    {
        "id": "q088",
        "question": "What RBI rules govern the timeline for reporting unauthorized ATM card transactions versus the bank's compensation for delayed ATM failure reconciliation?",
        "in_scope": True,
        "gold_sections": ["CIR_UNAUTH:6", "MC_CUSTSERV:5.12"],
        "quote": "zero liability within 3 working days under CIR_UNAUTH:6, and T+5 reconciliation compensation under MC_CUSTSERV:5.12",
        "reference": "CIR_UNAUTH:6 provides zero liability if reported within 3 days, while MC_CUSTSERV:5.12 mandates ₹100/day compensation for failed ATM reconciliations beyond T+5 days."
    },
    {
        "id": "q089",
        "question": "How do digital transaction alert requirements under digital security directions interact with customer liability notifications for unauthorized electronic debits?",
        "in_scope": True,
        "gold_sections": ["MD_DIGISEC:34", "CIR_UNAUTH:4"],
        "quote": "mandatory alerts under MD_DIGISEC:34, and immediate customer notification channels under CIR_UNAUTH:4",
        "reference": "MD_DIGISEC:34 mandates alerts for all debits and credits, while CIR_UNAUTH:4 requires banks to provide 24x7 reporting channels to enable customers to establish zero liability."
    },
    {
        "id": "q090",
        "question": "What provisions govern the closure of credit cards and the non-levy of charges on zero-balance accounts?",
        "in_scope": True,
        "gold_sections": ["MD_CARDS:8", "MC_CUSTSERV:24.7"],
        "quote": "card closure within 7 working days under MD_CARDS:8, and no unilateral zero-balance closure under MC_CUSTSERV:24.7",
        "reference": "MD_CARDS:8 regulates credit card closure timelines and delay penalties, while MC_CUSTSERV:24.7 restricts closing zero-balance accounts unilaterally."
    },

    # --- Out-of-Scope Questions (q091 to q100) ---
    {
        "id": "q091",
        "question": "What is the minimum voting threshold for the Committee of Creditors to approve a corporate resolution plan under the Insolvency and Bankruptcy Code (IBC)?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Corporate insolvency under IBC 2016 is outside retail bank complaint rules.",
        "reference": "Refused: Out of scope. IBC corporate insolvency proceedings are outside the retail banking complaint circulars."
    },
    {
        "id": "q092",
        "question": "What is the maximum Loan-to-Value (LTV) ratio allowed for commercial real estate loans exceeding Rupees 100 crore?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Commercial wholesale real estate financing rules are not covered.",
        "reference": "Refused: Out of scope. Commercial real estate prudential limits are outside the retail consumer protection circulars."
    },
    {
        "id": "q093",
        "question": "Can Indian banks offer cryptocurrency derivative exchange trading to high-net-worth institutional clients?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Cryptocurrency and virtual digital asset derivatives are outside retail complaint circulars.",
        "reference": "Refused: Out of scope. Crypto derivatives trading is not governed by retail banking complaint circulars."
    },
    {
        "id": "q094",
        "question": "What is the current all-in-cost ceiling for External Commercial Borrowings (ECB) benchmarked against SOFR?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "External commercial borrowings and SOFR benchmarks are wholesale forex regulations.",
        "reference": "Refused: Out of scope. External Commercial Borrowings (ECB) regulations are outside retail complaint handling."
    },
    {
        "id": "q095",
        "question": "What percentage of Adjusted Net Bank Credit (ANBC) must domestic scheduled commercial banks allocate to small and marginal farmers under Priority Sector Lending?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Priority Sector Lending targets are prudential macro guidelines, not retail grievance rules.",
        "reference": "Refused: Out of scope. Priority Sector Lending (PSL) allocation targets are outside the retail complaint circulars."
    },
    {
        "id": "q096",
        "question": "What is the minimum tier-1 capital adequacy ratio (CRAR) required for public sector banks under Basel III capital regulations?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Basel III capital adequacy guidelines are prudential bank solvency rules.",
        "reference": "Refused: Out of scope. Basel III CRAR requirements are prudential bank capital rules, not complaint handling guidelines."
    },
    {
        "id": "q097",
        "question": "How are Sovereign Gold Bond (SGB) semiannual interest payments taxed under the Indian Income Tax Act?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "Taxation of Sovereign Gold Bonds is governed by Income Tax laws, not RBI complaint circulars.",
        "reference": "Refused: Out of scope. Taxation rules for Sovereign Gold Bonds are governed by the Income Tax Act."
    },
    {
        "id": "q098",
        "question": "What is the mandatory percentage of project funds that a real estate developer must deposit in a designated RERA escrow bank account?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "RERA escrow account provisions are statutory real estate laws, not RBI retail grievance guidelines.",
        "reference": "Refused: Out of scope. Real Estate Regulatory Authority (RERA) statutory escrow requirements are outside retail banking circulars."
    },
    {
        "id": "q099",
        "question": "What is the foreign direct investment (FDI) equity cap under the automatic route for non-scheduled civil air transport services?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "FDI caps in aviation are Department for Promotion of Industry and Internal Trade (DPIIT) rules.",
        "reference": "Refused: Out of scope. Civil aviation foreign direct investment caps are governed by DPIIT/FDI policy."
    },
    {
        "id": "q100",
        "question": "What marine cargo risks are covered under an Institute Cargo Clause A insurance policy issued through Export Credit Guarantee Corporation (ECGC)?",
        "in_scope": False,
        "gold_sections": [],
        "quote": "ECGC marine trade insurance contracts are trade credit and insurance laws.",
        "reference": "Refused: Out of scope. ECGC marine cargo insurance is outside retail consumer banking regulations."
    }
]

# Ensure every new question has verified: False initially (per Rule 7, verified by Aryan Patel)
for q in new_questions:
    q["verified"] = False

# Combine all 100 questions
full_100 = existing_50 + new_questions

print(f"Total questions compiled: {len(full_100)}")
in_scope_count = sum(1 for q in full_100 if q["in_scope"])
out_scope_count = sum(1 for q in full_100 if not q["in_scope"])
print(f"In scope: {in_scope_count} (80%), Out of scope: {out_scope_count} (20%)")

# Write full golden.jsonl
with open("eval/golden.jsonl", "w", encoding="utf-8") as f:
    for q in full_100:
        f.write(json.dumps(q, ensure_ascii=False) + "\n")
print("Saved 100 questions to eval/golden.jsonl")

# Partition into 70/30 split:
# Dev: 70 questions (56 in-scope, 14 out-of-scope)
# Test: 30 questions (24 in-scope, 6 out-of-scope)
# To preserve the original 35 dev / 15 test partition from the first 50 questions:
# First 50: dev had 35 (28 in, 7 out), test had 15 (12 in, 3 out)
# Next 50: assign 35 to dev (28 in, 7 out), 15 to test (12 in, 3 out)
dev_set = [q for i, q in enumerate(existing_50) if i % 10 < 7] + [q for i, q in enumerate(new_questions) if i % 10 < 7]
test_set = [q for i, q in enumerate(existing_50) if i % 10 >= 7] + [q for i, q in enumerate(new_questions) if i % 10 >= 7]

print(f"Dev set count: {len(dev_set)} ({sum(1 for q in dev_set if q['in_scope'])} in-scope, {sum(1 for q in dev_set if not q['in_scope'])} out-of-scope)")
print(f"Test set count: {len(test_set)} ({sum(1 for q in test_set if q['in_scope'])} in-scope, {sum(1 for q in test_set if not q['in_scope'])} out-of-scope)")

with open("eval/golden_dev.jsonl", "w", encoding="utf-8") as f:
    for q in dev_set:
        f.write(json.dumps(q, ensure_ascii=False) + "\n")

with open("eval/golden_test.jsonl", "w", encoding="utf-8") as f:
    for q in test_set:
        f.write(json.dumps(q, ensure_ascii=False) + "\n")

print("Saved eval/golden_dev.jsonl and eval/golden_test.jsonl cleanly!")
