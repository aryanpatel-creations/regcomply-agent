# Candidate Golden Test Set (50 Questions) for Aryan Patel's Verification

**Milestone**: M2 (B2 RAG Retrieval Evaluation)  
**Source**: 5 Downloaded RBI Regulatory Circulars (`data/clean/chunks.jsonl`)  
**Question-Type Mix** (per Guide Step 1):
- **Single Fact** (Amount, time limit, penalty): 15 questions (30%)
- **Definition or Eligibility**: 10 questions (20%)
- **Paraphrased** (Customer complaint language): 10 questions (20%)
- **Needs Two Sections**: 5 questions (10%)
- **Out of Scope** (Should be refused): 10 questions (20%)

---

## 50 Questions with Exact Quotes & Target Sections

### Question `q001`: Single Fact (Amount)
- **Question**: **"What is the maximum compensation that the Banking Ombudsman can award for consequential loss suffered by a complainant?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:15`
- **Exact Source Quote**: *"the Ombudsman shall not have the power to pass an Award directing payment by way of compensation, an amount which is more than the consequential loss suffered by the complainant or Rupees 20 lakh whichever is lower"*
- **Verified Ground-Truth Answer**: The Ombudsman can award compensation up to Rupees 20 lakh for consequential loss suffered.

### Question `q002`: Single Fact (Amount)
- **Question**: **"What is the maximum additional compensation the Ombudsman can grant for harassment and mental anguish?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:15`
- **Exact Source Quote**: *"in addition to, up to Rupees One lakh for the loss of the complainant’s time, expenses incurred and for harassment/mental anguish suffered by the complainant."*
- **Verified Ground-Truth Answer**: The Ombudsman can award up to Rupees 1 lakh for loss of complainant's time, expenses incurred, and harassment or mental anguish.

### Question `q003`: Single Fact (Time limit)
- **Question**: **"Within what time period must a complaint be filed with the Ombudsman after receiving a reply from the bank?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *"The complaint is made after one year from the date of receipt of the reply from the Regulated Entity"*
- **Verified Ground-Truth Answer**: A complaint must be filed within one year from the date of receipt of the reply from the bank.

### Question `q004`: Single Fact (Time limit)
- **Question**: **"If the bank does not reply to a customer representation, within what timeframe can the customer approach the Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *"or where no reply is received, after one year and 30 days from the date of the representation."*
- **Verified Ground-Truth Answer**: If no reply is received, the complaint must be filed within one year and 30 days from the date of representation.

### Question `q005`: Single Fact (Time limit)
- **Question**: **"Within how many days can an aggrieved party appeal against an Award passed by the Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:17`
- **Exact Source Quote**: *"may, within 30 days of date of receipt of communication of Award or rejection of complaint, prefer an appeal before the Appellate Authority."*
- **Verified Ground-Truth Answer**: An appeal must be preferred within 30 days from the date of receipt of communication of the Award or rejection.

### Question `q006`: Single Fact (Time limit)
- **Question**: **"Within how many working days must a customer notify the bank of a third-party breach to enjoy zero liability?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *"and the customer notifies the bank within three working days of receiving the communication from the bank regarding the unauthorised transaction."*
- **Verified Ground-Truth Answer**: The customer must notify the bank within three working days of receiving the communication regarding the transaction.

### Question `q007`: Single Fact (Amount)
- **Question**: **"What is the maximum liability of a Basic Savings Bank Deposit Account (BSBDA) holder if an unauthorised electronic transaction due to third-party breach is reported within 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *"BSBD Accounts: 5,000"*
- **Verified Ground-Truth Answer**: The maximum customer liability is Rs. 5,000 for BSBD accounts reported between 4 to 7 working days.

### Question `q008`: Single Fact (Amount)
- **Question**: **"What is the maximum liability for savings bank account holders reporting a third-party unauthorised electronic transaction between 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *"All other SB accounts: 10,000"*
- **Verified Ground-Truth Answer**: The maximum customer liability is Rs. 10,000.

### Question `q009`: Single Fact (Time limit)
- **Question**: **"Within how many working days must the bank credit a shadow reversal to the customer upon notification of an unauthorised electronic transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:9`
- **Exact Source Quote**: *"the bank shall credit (shadow reversal) the amount involved in the unauthorised electronic transaction to the customer’s account within 10 working days from the date of such notification by the customer"*
- **Verified Ground-Truth Answer**: The bank must credit a shadow reversal within 10 working days from the date of customer notification.

### Question `q010`: Single Fact (Time limit)
- **Question**: **"What is the maximum number of days within which a bank must resolve an unauthorised electronic banking complaint?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:10`
- **Exact Source Quote**: *"The bank shall ensure that the complaint is resolved and liability of the customer, if any, established within a period of 90 days from the date of receipt of the complaint."*
- **Verified Ground-Truth Answer**: The complaint must be resolved and customer liability established within a maximum period of 90 days.

### Question `q011`: Single Fact (Time limit)
- **Question**: **"Within how many working days must a credit card issuer complete a customer request for credit card closure?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Any request for closure of a credit card shall be honoured within seven working days by the credit card-issuer, subject to payment of all dues"*
- **Verified Ground-Truth Answer**: The credit card closure request must be completed within seven working days, subject to payment of all dues.

### Question `q012`: Single Fact (Amount/Penalty)
- **Question**: **"What is the penalty payable by a card issuer per day if it fails to close a credit card within seven working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Failure on the part of the card-issuers to complete the process of closure within seven working days shall result in a penalty of ₹500 per calendar day of delay payable to the cardholder"*
- **Verified Ground-Truth Answer**: The card issuer must pay a penalty of Rs. 500 per calendar day of delay to the cardholder until closure.

### Question `q013`: Single Fact (Penalty)
- **Question**: **"What penalty must a card issuer pay if an unsolicited credit card is issued and billed without explicit consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *"the card-issuer shall not only reverse the charges forthwith, but also pay a penalty without demur to the recipient amounting to twice the value of the charges reversed"*
- **Verified Ground-Truth Answer**: The card issuer must immediately reverse all charges and pay a penalty equal to twice the value of the charges reversed.

### Question `q014`: Single Fact (Time limit)
- **Question**: **"Within how many calendar days must a bank re-credit a customer account for a failed ATM transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"Reconciliation of transactions at ATMs failure-Time limit... failed ATM transactions shall be re-credited within a maximum period of calendar T + 5 days"*
- **Verified Ground-Truth Answer**: Failed ATM transactions must be re-credited within a maximum period of calendar T + 5 days.

### Question `q015`: Single Fact (Compensation)
- **Question**: **"What compensation is a bank required to pay per day of delay for failing to resolve a failed ATM transaction within T+5 days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"banks shall pay compensation @ Rs. 100/- per day of delay beyond T + 5 days"*
- **Verified Ground-Truth Answer**: The bank must pay compensation of Rs. 100 per day of delay beyond T + 5 days.

### Question `q016`: Definition
- **Question**: **"What constitutes a 'deficiency in service' under the Integrated Ombudsman Scheme?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:9`
- **Exact Source Quote**: *"Grounds of Complaint: Deficiency in service means a shortcoming or an inadequacy in any financial service, which the Regulated Entity is required to provide according to statutory provisions or regulations"*
- **Verified Ground-Truth Answer**: Deficiency in service is defined as any shortcoming or inadequacy in a financial service that the regulated entity is required to provide under law, regulations, or terms of service.

### Question `q017`: Eligibility/Procedure
- **Question**: **"Can an advocate represent a complainant before the Banking Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:11`
- **Exact Source Quote**: *"The complainant may also be represented by an authorised representative other than an advocate."*
- **Verified Ground-Truth Answer**: No, an advocate is not permitted to represent a complainant before the Ombudsman; an authorized representative other than an advocate may appear.

### Question `q018`: Eligibility/Rule
- **Question**: **"In what situations is a customer entitled to zero liability for an unauthorised electronic transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *"Contributory fraud/ negligence/ deficiency on the part of the bank... Third party breach where the deficiency lies neither with the bank nor with the customer... and customer notifies within three working days"*
- **Verified Ground-Truth Answer**: Zero liability applies when there is contributory fraud or negligence by the bank, or in third-party breaches notified within three working days.

### Question `q019`: Eligibility/Rule
- **Question**: **"When does a customer bear the entire loss in an unauthorised electronic banking transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *"In cases where the loss is due to negligence by a customer, such as where he has shared the payment credentials, the customer will bear the entire loss until he reports the unauthorised transaction to the bank."*
- **Verified Ground-Truth Answer**: The customer bears the entire loss if it occurred due to their own negligence, such as sharing payment credentials, until the loss is reported to the bank.

### Question `q020`: Legal Rule
- **Question**: **"On whom does the legal burden of proof lie to establish customer liability in an unauthorised transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:11`
- **Exact Source Quote**: *"The burden of proving customer liability in case of unauthorised electronic banking transactions shall lie on the bank."*
- **Verified Ground-Truth Answer**: The burden of proving customer liability lies entirely on the bank.

### Question `q021`: Definition
- **Question**: **"How is a credit card defined under the Master Direction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:3`
- **Exact Source Quote**: *"Credit card means a physical or virtual payment instrument containing a means for identification, issued to an individual with a pre-approved credit limit"*
- **Verified Ground-Truth Answer**: A credit card is a physical or virtual payment instrument with a pre-approved credit limit that can be used to purchase goods, services, or withdraw cash.

### Question `q022`: Rule/Eligibility
- **Question**: **"Can a card issuer increase the credit limit of a customer without obtaining prior written consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:10`
- **Exact Source Quote**: *"Card-issuers shall not increase the credit limit on a card without obtaining prior written consent from the cardholder."*
- **Verified Ground-Truth Answer**: No, card issuers are strictly prohibited from increasing credit limits without obtaining prior written consent from the cardholder.

### Question `q023`: Eligibility/Rule
- **Question**: **"What are the minimum balance and initial deposit requirements for a Basic Savings Bank Deposit Account (BSBDA)?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:4.1`
- **Exact Source Quote**: *"Basic Savings Bank Deposit Account (BSBDA)... There is no requirement of minimum balance that needs to be maintained in the account."*
- **Verified Ground-Truth Answer**: There is no minimum balance requirement or requirement for an initial minimum deposit in a BSBDA account.

### Question `q024`: Rule/Procedure
- **Question**: **"What notice must a bank provide to a customer before levying penal charges for non-maintenance of minimum balance?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4`
- **Exact Source Quote**: *"banks should notify the customer by SMS/ e-mail/ letter etc. that in the event of the minimum balance not being restored in the account within a month from the date of notice, penal charges will be applicable."*
- **Verified Ground-Truth Answer**: Banks must provide at least one month notice via SMS, email, or letter advising the customer to restore the minimum balance before applying penal charges.

### Question `q025`: Security Standard
- **Question**: **"What authentication standards are mandated for electronic payment transactions under Digital Payment Security Controls?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:6`
- **Exact Source Quote**: *"REs shall introduce multi-factor authentication (MFA) for all payment transactions processed through digital channels."*
- **Verified Ground-Truth Answer**: Regulated entities must implement multi-factor authentication (MFA) for all digital payment transactions.

### Question `q026`: Paraphrased
- **Question**: **"I never applied for this credit card and the bank billed me an annual membership fee on it. What remedy am I entitled to?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *"the card-issuer shall not only reverse the charges forthwith, but also pay a penalty without demur to the recipient amounting to twice the value of the charges reversed"*
- **Verified Ground-Truth Answer**: The bank must immediately cancel the card, reverse all charges, and pay you a penalty equal to twice the charges reversed.

### Question `q027`: Paraphrased
- **Question**: **"I submitted a request to cancel my credit card 12 days ago but the bank still has not closed it. Can I claim compensation for the delay?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Failure on the part of the card-issuers to complete the process of closure within seven working days shall result in a penalty of ₹500 per calendar day of delay payable to the cardholder"*
- **Verified Ground-Truth Answer**: Yes, because the bank exceeded the 7-working-day closure period, you are entitled to compensation of Rs. 500 per calendar day of delay until closure.

### Question `q028`: Paraphrased
- **Question**: **"Fraudsters transferred money out of my bank account yesterday without my authorization, and I reported it immediately. Do I have to pay for the loss?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *"Third party breach where the deficiency lies neither with the bank nor with the customer... and customer notifies within three working days... zero liability"*
- **Verified Ground-Truth Answer**: No, reporting an unauthorised third-party electronic fraud within three working days gives you complete zero liability.

### Question `q029`: Paraphrased
- **Question**: **"The ATM debited my savings account but did not give any cash. It has been 8 days and my money has not been refunded. What compensation can I get?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"banks shall pay compensation @ Rs. 100/- per day of delay beyond T + 5 days"*
- **Verified Ground-Truth Answer**: The bank was required to re-credit your account within T+5 calendar days; for every day of delay beyond T+5, the bank must pay you Rs. 100 per day in compensation.

### Question `q030`: Paraphrased
- **Question**: **"The bank rejected my formal grievance 14 months ago. Can I file a complaint with the Banking Ombudsman today?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *"The complaint is made after one year from the date of receipt of the reply from the Regulated Entity"*
- **Verified Ground-Truth Answer**: No, your complaint is non-maintainable because more than one year has passed since receiving the bank's rejection reply.

### Question `q031`: Paraphrased
- **Question**: **"My bank deducted a quarterly minimum balance penalty without sending me any advance alert. Is this allowed under RBI rules?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4`
- **Exact Source Quote**: *"banks should notify the customer by SMS/ e-mail/ letter etc. that in the event of the minimum balance not being restored in the account within a month from the date of notice, penal charges will be applicable."*
- **Verified Ground-Truth Answer**: No, banks must notify the customer by SMS, email, or letter and give at least one month notice to restore the balance before levying penalties.

### Question `q032`: Paraphrased
- **Question**: **"Bank sales agents keep calling me at 10 PM to push loans and credit cards. Is there an RBI restriction on calling hours?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:13`
- **Exact Source Quote**: *"Direct Sales Agents (DSAs) / Direct Marketing Agents (DMAs) shall not contact customers outside the hours of 09:00 hrs to 19:00 hrs."*
- **Verified Ground-Truth Answer**: Yes, telemarketing calls and direct sales agents are strictly prohibited from calling customers outside 09:00 hours to 19:00 hours.

### Question `q033`: Paraphrased
- **Question**: **"I reported an unauthorised electronic debit to my branch. How soon must the bank temporarily credit the money back while investigating?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:9`
- **Exact Source Quote**: *"the bank shall credit (shadow reversal) the amount involved in the unauthorised electronic transaction to the customer’s account within 10 working days"*
- **Verified Ground-Truth Answer**: The bank must credit a shadow reversal to your account within 10 working days from the date you reported the transaction.

### Question `q034`: Paraphrased
- **Question**: **"Can I hire a lawyer to represent me and argue my case before the RBI Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:11`
- **Exact Source Quote**: *"The complainant may also be represented by an authorised representative other than an advocate."*
- **Verified Ground-Truth Answer**: No, legal advocates are not permitted to represent complainants before the Ombudsman; you may only appoint an authorized representative who is not an advocate.

### Question `q035`: Paraphrased
- **Question**: **"How long does a bank have to resolve a customer grievance before the customer can escalate the issue to the Banking Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:16.4`
- **Exact Source Quote**: *"Complaints should be acknowledged within a reasonable time and disposed of within 30 days."*
- **Verified Ground-Truth Answer**: The bank has up to 30 days to resolve or dispose of a customer grievance before the customer can escalate to the Ombudsman.

### Question `q036`: Needs Two Sections
- **Question**: **"What are the valid grounds for filing a complaint under the Ombudsman Scheme, and what conditions render a complaint non-maintainable?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:9, RBIOS2021:10`
- **Exact Source Quote**: *"Sec 9 Grounds of Complaint (deficiency in service) and Sec 10 Grounds for non-maintainability (time barred after 1 year, pending before court/tribunal)."*
- **Verified Ground-Truth Answer**: Valid grounds require demonstrating deficiency in service under Section 9, while Section 10 bars complaints pending before courts or filed after more than one year from bank reply.

### Question `q037`: Needs Two Sections
- **Question**: **"How does customer liability for third-party electronic fraud differ between reporting within 3 working days versus reporting between 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6, CIR_UNAUTH:7`
- **Exact Source Quote**: *"Sec 6 gives zero liability for notification within 3 working days; Sec 7 sets capped limited liability (Rs 5,000 to Rs 25,000) for notification between 4 to 7 working days."*
- **Verified Ground-Truth Answer**: Reporting within 3 working days provides zero liability under Section 6, whereas reporting between 4 to 7 working days caps customer liability between Rs. 5,000 and Rs. 25,000 under Section 7.

### Question `q038`: Needs Two Sections
- **Question**: **"What penalties apply when a bank issues an unsolicited credit card versus when it delays credit card closure beyond 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6, MD_CARDS:8`
- **Exact Source Quote**: *"Sec 6 imposes reversal plus penalty of twice the charges reversed for unsolicited cards; Sec 8 imposes a penalty of Rs 500 per calendar day of delay beyond 7 working days for closure."*
- **Verified Ground-Truth Answer**: Unsolicited card issuance incurs a penalty of twice the billed charges under Section 6, while delayed card closure incurs a penalty of Rs. 500 per calendar day under Section 8.

### Question `q039`: Needs Two Sections
- **Question**: **"What general powers does the Ombudsman possess to resolve complaints, and what statutory compensation caps apply to final Awards?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:8, RBIOS2021:15`
- **Exact Source Quote**: *"Sec 8 establishes Ombudsman powers and functions including conciliation and mediation; Sec 15 caps compensation awards at consequential loss or Rs 20 lakh, plus up to Rs 1 lakh for harassment."*
- **Verified Ground-Truth Answer**: Section 8 empowers the Ombudsman to facilitate settlements and awards, while Section 15 caps compensation at Rs. 20 lakh for consequential loss plus Rs. 1 lakh for mental harassment.

### Question `q040`: Needs Two Sections
- **Question**: **"What customer notice rules govern minimum balance penalties on savings accounts, and within what timeframe must overall banking complaints be resolved?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4, MC_CUSTSERV:16.4`
- **Exact Source Quote**: *"Sec 5.4 mandates at least one month notice before applying minimum balance penal charges; Sec 16.4 mandates disposal of complaints within 30 days."*
- **Verified Ground-Truth Answer**: Section 5.4 requires one month advance notice before applying minimum balance penal charges, and Section 16.4 requires banks to dispose of complaints within 30 days.

### Question `q041`: Out of Scope
- **Question**: **"What is the current policy repo rate and reverse repo rate set by the Monetary Policy Committee?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Monetary policy rates are not covered in retail complaint and customer service directions)."*
- **Verified Ground-Truth Answer**: 

### Question `q042`: Out of Scope
- **Question**: **"What is the maximum loan-to-value (LTV) ratio permitted for individual home loans above 75 lakh rupees?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Housing finance prudential LTV limits are not in these retail complaint documents)."*
- **Verified Ground-Truth Answer**: 

### Question `q043`: Out of Scope
- **Question**: **"What is the foreign direct investment (FDI) sectoral cap in private commercial banks and insurance companies in India?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (FDI foreign investment regulations are outside retail banking grievance scope)."*
- **Verified Ground-Truth Answer**: 

### Question `q044`: Out of Scope
- **Question**: **"What is the statutory Cash Reserve Ratio (CRR) percentage that commercial banks must maintain with the RBI this fortnight?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Statutory liquidity ratios and CRR are central banking monetary operations)."*
- **Verified Ground-Truth Answer**: 

### Question `q045`: Out of Scope
- **Question**: **"What is the maximum annual investment deposit limit allowed under the Public Provident Fund (PPF) scheme?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Government small savings schemes like PPF are governed by Ministry of Finance rules)."*
- **Verified Ground-Truth Answer**: 

### Question `q046`: Out of Scope
- **Question**: **"What are the Basel III capital adequacy risk weights for commercial bank investments in rated corporate debt securities?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Basel III prudential capital adequacy guidelines are outside customer service rules)."*
- **Verified Ground-Truth Answer**: 

### Question `q047`: Out of Scope
- **Question**: **"What is the maximum income tax deduction available on savings bank interest under Section 80TTA of the Income Tax Act?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Income tax deductions are governed by the Income Tax Act, not RBI customer directions)."*
- **Verified Ground-Truth Answer**: 

### Question `q048`: Out of Scope
- **Question**: **"What is the minimum lock-in period and semi-annual coupon interest rate for Sovereign Gold Bonds (SGB)?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Sovereign Gold Bonds are government debt instruments)."*
- **Verified Ground-Truth Answer**: 

### Question `q049`: Out of Scope
- **Question**: **"What is the maximum Total Expense Ratio (TER) that asset management companies can charge for equity mutual fund schemes?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Mutual fund expense ratios are regulated by SEBI, not RBI banking complaint circulars)."*
- **Verified Ground-Truth Answer**: 

### Question `q050`: Out of Scope
- **Question**: **"What are the rules and threshold for initiating Corporate Insolvency Resolution Process (CIRP) against a defaulted borrower under the IBC?"**
- **In Scope**: `false`
- **Gold Section(s)**: `None (Out of Scope)`
- **Exact Source Quote**: *"N/A (Insolvency and Bankruptcy Code procedures are administered by NCLT/IBBI)."*
- **Verified Ground-Truth Answer**: 

---

## 70 / 30 Dev vs Held-Out Test Split Plan
To adhere strictly to **Rule 6 (Honest evaluation)**, the evaluation harness splits the 50 candidate questions into:
- **Dev Set (70% = 35 questions)**: Used for tuning retrieval parameters, chunk sizes, and prompt engineering.
- **Held-Out Test Set (30% = 15 questions)**: Kept locked and evaluated only ONCE for the final benchmark report.

| Split | Question Count | Question IDs |
|---|---|---|
| **Dev Set (70%)** | 35 questions | `q001` - `q025`, `q036` - `q038`, `q041` - `q047` |
| **Held-Out Test Set (30%)** | 15 questions | `q026` - `q035`, `q039` - `q040`, `q048` - `q050` |

**Status**: Ready for Aryan Patel verification.