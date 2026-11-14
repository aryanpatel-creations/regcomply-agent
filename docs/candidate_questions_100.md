# Complete Golden Test Set (100 Questions) for Aryan Patel's Verification

**Milestone**: M5 (B2 Full RAG Evaluation Harness)  
**Source Documents**: 5 Downloaded RBI Regulatory Circulars (`data/clean/chunks.jsonl`)  
**Total Questions**: 100 (80 In-Scope, 20 Out-of-Scope)  
**Dataset Partitions**: 70 Dev Questions (`eval/golden_dev.jsonl`), 30 Held-Out Test Questions (`eval/golden_test.jsonl`)  

---

## Breakdown by Category
- **Single Fact** (statutory amounts, turnaround times, penalties): 30 questions
- **Definition or Eligibility** (BSBD accounts, card issuance criteria, liability tiers): 20 questions
- **Paraphrased / Customer Complaint Language** (realistic retail complaint phrasing): 20 questions
- **Needs Two Sections / Multi-Circular** (cross-clause or cross-document rules): 10 questions
- **Out of Scope** (wholesale, corporate lending, IBC, crypto, SGB, FDI): 20 questions

---

## Questions Directory

### Question `q001`
- **Question**: **"What is the maximum compensation that the Banking Ombudsman can award for consequential loss suffered by a complainant?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:15`
- **Exact Source Quote**: *""*
- **Reference Answer**: The Ombudsman can award compensation up to Rupees 20 lakh for consequential loss suffered.

### Question `q002`
- **Question**: **"What is the maximum additional compensation the Ombudsman can grant for harassment and mental anguish?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:15`
- **Exact Source Quote**: *""*
- **Reference Answer**: The Ombudsman can award up to Rupees 1 lakh for loss of complainant's time, expenses incurred, and harassment or mental anguish.

### Question `q003`
- **Question**: **"Within what time period must a complaint be filed with the Ombudsman after receiving a reply from the bank?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: A complaint must be filed within one year from the date of receipt of the reply from the bank.

### Question `q004`
- **Question**: **"If the bank does not reply to a customer representation, within what timeframe can the customer approach the Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: If no reply is received, the complaint must be filed within one year and 30 days from the date of representation.

### Question `q005`
- **Question**: **"Within how many days can an aggrieved party appeal against an Award passed by the Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:17`
- **Exact Source Quote**: *""*
- **Reference Answer**: An appeal must be preferred within 30 days from the date of receipt of communication of the Award or rejection.

### Question `q006`
- **Question**: **"Within how many working days must a customer notify the bank of a third-party breach to enjoy zero liability?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: The customer must notify the bank within three working days of receiving the communication regarding the transaction.

### Question `q007`
- **Question**: **"What is the maximum liability of a Basic Savings Bank Deposit Account (BSBDA) holder if an unauthorised electronic transaction due to third-party breach is reported within 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *""*
- **Reference Answer**: The maximum customer liability is Rs. 5,000 for BSBD accounts reported between 4 to 7 working days.

### Question `q008`
- **Question**: **"What is the maximum liability for savings bank account holders reporting a third-party unauthorised electronic transaction between 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *""*
- **Reference Answer**: The maximum customer liability is Rs. 10,000.

### Question `q009`
- **Question**: **"Within how many working days must the bank credit a shadow reversal to the customer upon notification of an unauthorised electronic transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:9`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank must credit a shadow reversal within 10 working days from the date of customer notification.

### Question `q010`
- **Question**: **"What is the maximum number of days within which a bank must resolve an unauthorised electronic banking complaint?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: The complaint must be resolved and customer liability established within a maximum period of 90 days.

### Question `q011`
- **Question**: **"Within how many working days must a credit card issuer complete a customer request for credit card closure?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *""*
- **Reference Answer**: The credit card closure request must be completed within seven working days, subject to payment of all dues.

### Question `q012`
- **Question**: **"What is the penalty payable by a card issuer per day if it fails to close a credit card within seven working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *""*
- **Reference Answer**: The card issuer must pay a penalty of Rs. 500 per calendar day of delay to the cardholder until closure.

### Question `q013`
- **Question**: **"What penalty must a card issuer pay if an unsolicited credit card is issued and billed without explicit consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: The card issuer must immediately reverse all charges and pay a penalty equal to twice the value of the charges reversed.

### Question `q014`
- **Question**: **"Within how many calendar days must a bank re-credit a customer account for a failed ATM transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *""*
- **Reference Answer**: Failed ATM transactions must be re-credited within a maximum period of calendar T + 5 days.

### Question `q015`
- **Question**: **"What compensation is a bank required to pay per day of delay for failing to resolve a failed ATM transaction within T+5 days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank must pay compensation of Rs. 100 per day of delay beyond T + 5 days.

### Question `q016`
- **Question**: **"What constitutes a 'deficiency in service' under the Integrated Ombudsman Scheme?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:9`
- **Exact Source Quote**: *""*
- **Reference Answer**: Deficiency in service is defined as any shortcoming or inadequacy in a financial service that the regulated entity is required to provide under law, regulations, or terms of service.

### Question `q017`
- **Question**: **"Can an advocate represent a complainant before the Banking Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:11`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, an advocate is not permitted to represent a complainant before the Ombudsman; an authorized representative other than an advocate may appear.

### Question `q018`
- **Question**: **"In what situations is a customer entitled to zero liability for an unauthorised electronic transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: Zero liability applies when there is contributory fraud or negligence by the bank, or in third-party breaches notified within three working days.

### Question `q019`
- **Question**: **"When does a customer bear the entire loss in an unauthorised electronic banking transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7`
- **Exact Source Quote**: *""*
- **Reference Answer**: The customer bears the entire loss if it occurred due to their own negligence, such as sharing payment credentials, until the loss is reported to the bank.

### Question `q020`
- **Question**: **"On whom does the legal burden of proof lie to establish customer liability in an unauthorised transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:11`
- **Exact Source Quote**: *""*
- **Reference Answer**: The burden of proving customer liability lies entirely on the bank.

### Question `q021`
- **Question**: **"How is a credit card defined under the Master Direction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:3`
- **Exact Source Quote**: *""*
- **Reference Answer**: A credit card is a physical or virtual payment instrument with a pre-approved credit limit that can be used to purchase goods, services, or withdraw cash.

### Question `q022`
- **Question**: **"Can a card issuer increase the credit limit of a customer without obtaining prior written consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, card issuers are strictly prohibited from increasing credit limits without obtaining prior written consent from the cardholder.

### Question `q023`
- **Question**: **"What are the minimum balance and initial deposit requirements for a Basic Savings Bank Deposit Account (BSBDA)?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:4.1`
- **Exact Source Quote**: *""*
- **Reference Answer**: There is no minimum balance requirement or requirement for an initial minimum deposit in a BSBDA account.

### Question `q024`
- **Question**: **"What notice must a bank provide to a customer before levying penal charges for non-maintenance of minimum balance?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4`
- **Exact Source Quote**: *""*
- **Reference Answer**: Banks must provide at least one month notice via SMS, email, or letter advising the customer to restore the minimum balance before applying penal charges.

### Question `q025`
- **Question**: **"What authentication standards are mandated for electronic payment transactions under Digital Payment Security Controls?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: Regulated entities must implement multi-factor authentication (MFA) for all digital payment transactions.

### Question `q026`
- **Question**: **"I never applied for this credit card and the bank billed me an annual membership fee on it. What remedy am I entitled to?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank must immediately cancel the card, reverse all charges, and pay you a penalty equal to twice the charges reversed.

### Question `q027`
- **Question**: **"I submitted a request to cancel my credit card 12 days ago but the bank still has not closed it. Can I claim compensation for the delay?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *""*
- **Reference Answer**: Yes, because the bank exceeded the 7-working-day closure period, you are entitled to compensation of Rs. 500 per calendar day of delay until closure.

### Question `q028`
- **Question**: **"Fraudsters transferred money out of my bank account yesterday without my authorization, and I reported it immediately. Do I have to pay for the loss?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, reporting an unauthorised third-party electronic fraud within three working days gives you complete zero liability.

### Question `q029`
- **Question**: **"The ATM debited my savings account but did not give any cash. It has been 8 days and my money has not been refunded. What compensation can I get?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank was required to re-credit your account within T+5 calendar days; for every day of delay beyond T+5, the bank must pay you Rs. 100 per day in compensation.

### Question `q030`
- **Question**: **"The bank rejected my formal grievance 14 months ago. Can I file a complaint with the Banking Ombudsman today?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, your complaint is non-maintainable because more than one year has passed since receiving the bank's rejection reply.

### Question `q031`
- **Question**: **"My bank deducted a quarterly minimum balance penalty without sending me any advance alert. Is this allowed under RBI rules?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, banks must notify the customer by SMS, email, or letter and give at least one month notice to restore the balance before levying penalties.

### Question `q032`
- **Question**: **"Bank sales agents keep calling me at 10 PM to push loans and credit cards. Is there an RBI restriction on calling hours?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:13`
- **Exact Source Quote**: *""*
- **Reference Answer**: Yes, telemarketing calls and direct sales agents are strictly prohibited from calling customers outside 09:00 hours to 19:00 hours.

### Question `q033`
- **Question**: **"I reported an unauthorised electronic debit to my branch. How soon must the bank temporarily credit the money back while investigating?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:9`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank must credit a shadow reversal to your account within 10 working days from the date you reported the transaction.

### Question `q034`
- **Question**: **"Can I hire a lawyer to represent me and argue my case before the RBI Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:11`
- **Exact Source Quote**: *""*
- **Reference Answer**: No, legal advocates are not permitted to represent complainants before the Ombudsman; you may only appoint an authorized representative who is not an advocate.

### Question `q035`
- **Question**: **"How long does a bank have to resolve a customer grievance before the customer can escalate the issue to the Banking Ombudsman?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:16.4`
- **Exact Source Quote**: *""*
- **Reference Answer**: The bank has up to 30 days to resolve or dispose of a customer grievance before the customer can escalate to the Ombudsman.

### Question `q036`
- **Question**: **"What are the valid grounds for filing a complaint under the Ombudsman Scheme, and what conditions render a complaint non-maintainable?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:9, RBIOS2021:10`
- **Exact Source Quote**: *""*
- **Reference Answer**: Valid grounds require demonstrating deficiency in service under Section 9, while Section 10 bars complaints pending before courts or filed after more than one year from bank reply.

### Question `q037`
- **Question**: **"How does customer liability for third-party electronic fraud differ between reporting within 3 working days versus reporting between 4 to 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6, CIR_UNAUTH:7`
- **Exact Source Quote**: *""*
- **Reference Answer**: Reporting within 3 working days provides zero liability under Section 6, whereas reporting between 4 to 7 working days caps customer liability between Rs. 5,000 and Rs. 25,000 under Section 7.

### Question `q038`
- **Question**: **"What penalties apply when a bank issues an unsolicited credit card versus when it delays credit card closure beyond 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6, MD_CARDS:8`
- **Exact Source Quote**: *""*
- **Reference Answer**: Unsolicited card issuance incurs a penalty of twice the billed charges under Section 6, while delayed card closure incurs a penalty of Rs. 500 per calendar day under Section 8.

### Question `q039`
- **Question**: **"What general powers does the Ombudsman possess to resolve complaints, and what statutory compensation caps apply to final Awards?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:8, RBIOS2021:15`
- **Exact Source Quote**: *""*
- **Reference Answer**: Section 8 empowers the Ombudsman to facilitate settlements and awards, while Section 15 caps compensation at Rs. 20 lakh for consequential loss plus Rs. 1 lakh for mental harassment.

### Question `q040`
- **Question**: **"What customer notice rules govern minimum balance penalties on savings accounts, and within what timeframe must overall banking complaints be resolved?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4, MC_CUSTSERV:16.4`
- **Exact Source Quote**: *""*
- **Reference Answer**: Section 5.4 requires one month advance notice before applying minimum balance penal charges, and Section 16.4 requires banks to dispose of complaints within 30 days.

### Question `q041`
- **Question**: **"What is the current policy repo rate and reverse repo rate set by the Monetary Policy Committee?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q042`
- **Question**: **"What is the maximum loan-to-value (LTV) ratio permitted for individual home loans above 75 lakh rupees?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q043`
- **Question**: **"What is the foreign direct investment (FDI) sectoral cap in private commercial banks and insurance companies in India?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q044`
- **Question**: **"What is the statutory Cash Reserve Ratio (CRR) percentage that commercial banks must maintain with the RBI this fortnight?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q045`
- **Question**: **"What is the maximum annual investment deposit limit allowed under the Public Provident Fund (PPF) scheme?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q046`
- **Question**: **"What are the Basel III capital adequacy risk weights for commercial bank investments in rated corporate debt securities?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q047`
- **Question**: **"What is the maximum income tax deduction available on savings bank interest under Section 80TTA of the Income Tax Act?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q048`
- **Question**: **"What is the minimum lock-in period and semi-annual coupon interest rate for Sovereign Gold Bonds (SGB)?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q049`
- **Question**: **"What is the maximum Total Expense Ratio (TER) that asset management companies can charge for equity mutual fund schemes?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q050`
- **Question**: **"What are the rules and threshold for initiating Corporate Insolvency Resolution Process (CIRP) against a defaulted borrower under the IBC?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Outside retail complaint handling*
- **Reference Refusal**: 

### Question `q051`
- **Question**: **"Does the RBI mandate multi-factor authentication for electronic payment modes and fund transfers?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:33`
- **Exact Source Quote**: *"multi-factor authentication for payments through electronic modes and fund transfers, including cash withdrawals from ATMs/ micro- ATMs/ business correspondents"*
- **Reference Answer**: Yes, RBI mandates multi-factor authentication for electronic payments and fund transfers unless explicitly permitted or relaxed.

### Question `q052`
- **Question**: **"What customer alerts must regulated entities provide for payment transactions under digital security guidelines?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34`
- **Exact Source Quote**: *"alerts (like SMS, e-mail, etc.) should be applied in respect of all payment transactions (including debits and credits), creation of new account linkages"*
- **Reference Answer**: Regulated entities must send transaction alerts (via SMS, email, etc.) for all payment debits and credits, as well as for creating new account linkages.

### Question `q053`
- **Question**: **"For online transactions, should the merchant name or the payment aggregator be displayed to the customer?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34`
- **Exact Source Quote**: *"customer for online transactions shall identify the merchant name, wherever applicable, rather than the payment aggregator through which the transaction is routed"*
- **Reference Answer**: Online transaction authentication must identify the actual merchant name rather than the payment aggregator routing the payment.

### Question `q054`
- **Question**: **"What must happen if an authenticated customer session experiences interference or network disruption?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34`
- **Exact Source Quote**: *"An authenticated session, together with its encryption protocol, should remain intact throughout the interaction with the customer. Else, in the event of interference or in case of session disruption, the session should be terminated"*
- **Reference Answer**: The session and encryption protocol must remain intact throughout; in case of interference or disruption, the session must be immediately terminated.

### Question `q055`
- **Question**: **"Must banks configure mechanisms to alert customers when authentication fails?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:36`
- **Exact Source Quote**: *"mechanism to alert the customers in case of failed authentication, time frame for the same, etc."*
- **Reference Answer**: Yes, banks must document and implement mechanisms to alert customers when authentication fails.

### Question `q056`
- **Question**: **"What parameters should be monitored for system alerts according to digital payment security controls?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:37`
- **Exact Source Quote**: *"System alerts shall be parameterised and monitored in terms of various applicable parameters. Such parameters, as applicable could be: transaction velocity (e.g., fund transfers, cash withdrawals, payments through electronic modes, adding new beneficiaries, etc.) in a short period"*
- **Reference Answer**: System alerts must monitor parameters such as transaction velocity (rapid fund transfers, cash withdrawals, adding new beneficiaries) within short timeframes.

### Question `q057`
- **Question**: **"Can cardholders set separate transaction caps for domestic and international card transactions?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:72`
- **Exact Source Quote**: *"mandated both for domestic as well as international transactions separately. REs shall put in place transaction control mechanisms with necessary caps (restrictions o n transactions)"*
- **Reference Answer**: Yes, regulated entities must provide transaction control mechanisms with separate transaction caps for domestic and international transactions.

### Question `q058`
- **Question**: **"Is adaptive authentication permitted by RBI based on customer risk profiling and behavior?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34`
- **Exact Source Quote**: *"REs may also adopt adaptive authentication to select the right authentication factors. depending on risk assessment, user risk profile and behaviour."*
- **Reference Answer**: Yes, banks may adopt adaptive authentication to select authentication factors based on risk assessment and customer transaction behavior.

### Question `q059`
- **Question**: **"I noticed an unknown merchant debit on my statement that only says 'PayAggregator'. Is the bank required to show the merchant name?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34`
- **Exact Source Quote**: *"shall identify the merchant name, wherever applicable, rather than the payment aggregator through which the transaction is routed"*
- **Reference Answer**: Yes, RBI rules mandate that the transaction identifier must state the actual merchant name rather than only the payment aggregator.

### Question `q060`
- **Question**: **"Are banks required to implement multi-factor authentication for cash withdrawals from micro-ATMs and business correspondents?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:33`
- **Exact Source Quote**: *"multi-factor authentication for payments through electronic modes and fund transfers, including cash withdrawals from ATMs/ micro- ATMs/ business correspondents"*
- **Reference Answer**: Yes, multi-factor authentication applies to cash withdrawals from ATMs, micro-ATMs, and business correspondents.

### Question `q061`
- **Question**: **"Are banks allowed to charge individuals for the issuance of a passbook for savings bank accounts?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.6`
- **Exact Source Quote**: *"A passbook is a ready reckoner of transactions and is handy and compact and as such, is far more convenient to the small customer. (ii) Banks should provide passbooks to all Savings Bank Account holders (Individuals) free of charge."*
- **Reference Answer**: No, banks must provide passbooks to all individual Savings Bank account holders free of charge.

### Question `q062`
- **Question**: **"Can customers write cheques in any language or must they only be in English and Hindi?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.7`
- **Exact Source Quote**: *"cheques may be written in Hindi, English or in the concerned Regional Language. Customer may write cheques in any language of his choice."*
- **Reference Answer**: Customers can write cheques in Hindi, English, or the concerned Regional Language of their choice.

### Question `q063`
- **Question**: **"Are banks required to offer doorstep banking services to senior citizens and visually impaired persons?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:24.1`
- **Exact Source Quote**: *"Doorstep Banking Services for Senior Citizens and Differently Abled Persons Banks are advised to make concerted effort to provide a basic suite of banking services to senior citizens of more than 70 years of age and differently abled or infirm persons"*
- **Reference Answer**: Yes, banks must provide doorstep banking services to senior citizens aged 70+ and differently abled or infirm persons.

### Question `q064`
- **Question**: **"Can banks levy penal charges on savings accounts for non-maintenance of minimum balance if the account is inoperative?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.4`
- **Exact Source Quote**: *"Banks are advised to ensure that no penal charges are levied for non-maintenance of minimum balances in any inoperative account."*
- **Reference Answer**: No, RBI circular strictly prohibits levying penal charges for non-maintenance of minimum balance in any inoperative account.

### Question `q065`
- **Question**: **"What is the compensation payable by the card-issuing bank to the customer for delayed reconciliation of failed ATM transactions beyond T+5 days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"banks shall pay compensation of ₹ 100/- per day of delay to the customer, if the failed ATM transaction is not resolved within T + 5 calendar days"*
- **Reference Answer**: Banks must pay ₹100 per day of delay if a failed ATM transaction is not resolved within T+5 calendar days.

### Question `q066`
- **Question**: **"Can a bank unilaterally close a savings account simply because the balance has reduced to zero without prior notice?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:24.7`
- **Exact Source Quote**: *"Banks are advised not to close any account having balance without prior notice to the customer. Accounts having zero balance should also not be closed unilaterally without notice."*
- **Reference Answer**: No, banks cannot close zero-balance or funded accounts unilaterally without giving prior notice to the customer.

### Question `q067`
- **Question**: **"What is the basic requirement regarding printed banking materials like account opening forms and pay-in slips?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:4.3`
- **Exact Source Quote**: *"account opening forms, pay-in-slips, passbooks, etc., in trilingual form i.e., English, Hindi and the concerned Regional Language."*
- **Reference Answer**: Printed materials such as account opening forms, pay-in slips, and passbooks must be in trilingual form: English, Hindi, and Regional Language.

### Question `q068`
- **Question**: **"Are banks allowed to levy charges for non-operation or activation of an inoperative Basic Savings Bank Deposit Account?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:4.1`
- **Exact Source Quote**: *"no charge for non-operation/activation of in-operative 'Basic Savings Bank Deposit Account'."*
- **Reference Answer**: No, banks cannot levy any charge for the activation or non-operation of an inoperative Basic Savings Bank Deposit Account.

### Question `q069`
- **Question**: **"The ATM debited Rs 10,000 from my savings account but did not dispense cash, and 7 days have passed. Am I entitled to delay compensation?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"banks shall pay compensation of ₹ 100/- per day of delay to the customer, if the failed ATM transaction is not resolved within T + 5 calendar days"*
- **Reference Answer**: Yes, you are entitled to compensation of ₹100 per day for every day of delay beyond T+5 calendar days.

### Question `q070`
- **Question**: **"My branch refused to give me a physical passbook and insists on sending emails only. Is this allowed under RBI rules?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MC_CUSTSERV:5.6`
- **Exact Source Quote**: *"Banks should provide passbooks to all Savings Bank Account holders (Individuals) free of charge."*
- **Reference Answer**: No, banks are required to provide passbooks to individual Savings Bank account holders free of charge upon request.

### Question `q071`
- **Question**: **"What is the penalty if a card issuer activates an unsolicited credit card without explicit customer consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *"shall reverse the charges immediately and also pay a penalty without demur to the recipient of the card of an amount equal to twice the value of charges reversed."*
- **Reference Answer**: The card issuer must reverse the charges immediately and pay a penalty equal to twice the value of the reversed charges.

### Question `q072`
- **Question**: **"Within how many days must a credit card closure request be completed by the card-issuer?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Any request for closure of a credit card shall be honoured within seven working days by the card-issuer, subject to payment of all dues by the cardholder."*
- **Reference Answer**: The card-issuer must honor and complete a credit card closure request within 7 working days, subject to payment of dues.

### Question `q073`
- **Question**: **"What compensation is payable to a cardholder if the bank fails to close a credit card within 7 working days?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Failure on the part of the card-issuer to complete the process of closure within seven working days shall result in a penalty of ₹ 500 per day of delay payable to the cardholder, till the closure of account"*
- **Reference Answer**: The card-issuer must pay a penalty of ₹500 per day of delay to the cardholder until the card is closed.

### Question `q074`
- **Question**: **"Are card issuers allowed to offer a one-time option to cardholders to modify their billing cycle?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:13`
- **Exact Source Quote**: *"Cardholders shall be provided a one-time option to modify the billing cycle of the credit card as per their convenience."*
- **Reference Answer**: Yes, cardholders must be given at least a one-time option to modify their credit card billing cycle.

### Question `q075`
- **Question**: **"Can a card issuer provide an insurance cover on a credit or debit card without obtaining explicit written or digital consent?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *"In cases where the card-issuers are offering any insurance cover to their cardholders, in tie-up with insurance companies, the card-issuers shall obtain explicit written or digital consent from the cardholder"*
- **Reference Answer**: No, card issuers must obtain explicit written or digital consent before providing any insurance cover to cardholders.

### Question `q076`
- **Question**: **"I paid all my credit card dues and requested cancellation, but the bank took 14 working days to close it. Can I claim compensation?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8`
- **Exact Source Quote**: *"Failure on the part of the card-issuer to complete the process of closure within seven working days shall result in a penalty of ₹ 500 per day of delay payable to the cardholder"*
- **Reference Answer**: Yes, you can claim ₹500 per day of delay for the 7 working days beyond the statutory 7-day limit (₹3,500 total compensation).

### Question `q077`
- **Question**: **"The bank sent me an upgraded credit card that I never applied for, and debited an annual fee. What are my rights under RBI directions?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6`
- **Exact Source Quote**: *"The issue of unsolicited cards/upgradation is strictly prohibited. In case, an unsolicited card is issued/existing card upgraded and activated without the explicit consent of the recipient... shall reverse the charges immediately and also pay a penalty without demur to the recipient of the card of an amount equal to twice the value of charges reversed."*
- **Reference Answer**: Unsolicited card upgrades are strictly prohibited. The bank must reverse the charges immediately and pay you a penalty equal to twice the value of the reversed fee.

### Question `q078`
- **Question**: **"Who bears the burden of proof to demonstrate customer negligence in an unauthorized electronic banking transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:11`
- **Exact Source Quote**: *"The burden of proving customer liability in case of unauthorised electronic banking transactions shall lie on the bank."*
- **Reference Answer**: The burden of proving customer liability in unauthorized electronic banking transactions lies entirely on the bank.

### Question `q079`
- **Question**: **"Within how many working days must a bank credit a shadow reversal after being notified of an unauthorized electronic transaction?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:9`
- **Exact Source Quote**: *"the bank shall credit (shadow reversal) the amount involved in the unauthorised electronic transaction to the customer’s account within 10 working days from the date of such notification"*
- **Reference Answer**: The bank must credit a shadow reversal to the customer's account within 10 working days of notification.

### Question `q080`
- **Question**: **"What is the maximum turnaround time for a bank to resolve an unauthorized electronic transaction complaint from the date of receipt?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:10`
- **Exact Source Quote**: *"A complaint shall be resolved and liability of the customer, if any, established within such time, as may be specified in the bank's Board approved policy, but not exceeding 90 days from the date of receipt of the complaint"*
- **Reference Answer**: Banks must resolve the complaint and establish liability within a period not exceeding 90 days from receipt.

### Question `q081`
- **Question**: **"If an unauthorized transaction occurs due to a third-party breach and the customer notifies the bank within 3 working days, what is the customer's liability?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6`
- **Exact Source Quote**: *"Third party breach where the deficiency lies neither with the bank nor with the customer but lies elsewhere in the system, and the customer notifies the bank within three working days... customer's entitlement to zero liability shall arise"*
- **Reference Answer**: The customer has zero liability if the third-party breach is reported to the bank within 3 working days.

### Question `q082`
- **Question**: **"The bank is claiming I shared my OTP for an unauthorized debit, but I never received any message. Can the bank make me pay without proving negligence?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:11`
- **Exact Source Quote**: *"The burden of proving customer liability in case of unauthorised electronic banking transactions shall lie on the bank."*
- **Reference Answer**: No, under RBI directions, the burden of proving that you were negligent or shared credentials lies strictly on the bank.

### Question `q083`
- **Question**: **"On what grounds can the Ombudsman reject a complaint at the initial scrutiny stage?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:16`
- **Exact Source Quote**: *"The Deputy Ombudsman or the Ombudsman may reject a complaint at any stage if it appears that the complaint made: (a) is non-maintainable under clause 10; or (b) is in the nature of offering suggestions or seeking guidance or explanation"*
- **Reference Answer**: A complaint can be rejected if it is non-maintainable under clause 10, or is merely seeking guidance, suggestions, or general explanations.

### Question `q084`
- **Question**: **"Can a customer appeal against an Award passed by the Banking Ombudsman if the Award was made with mutual agreement?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:17`
- **Exact Source Quote**: *"no appeal shall lie against an Award passed with the consent of the parties or where the Award has been passed under clause 15(1)."*
- **Reference Answer**: No appeal lies against an Award passed with the mutual consent of both parties.

### Question `q085`
- **Question**: **"Can a complaint be filed with the Ombudsman if the same subject matter is already pending before a consumer court or civil court?"**
- **In Scope**: `true`
- **Gold Section(s)**: `RBIOS2021:10`
- **Exact Source Quote**: *"The complaint is pending before, or has been dealt with on merits, by any Court, Tribunal or Arbitrator or any other Forum or Authority"*
- **Reference Answer**: No, complaints that are pending or have been decided before a Court, Tribunal, or Consumer Forum are non-maintainable before the Ombudsman.

### Question `q086`
- **Question**: **"If an unauthorized transaction occurs on a basic savings account (BSBD) due to third-party deficiency and reported after 5 days, what circular sections govern customer liability?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:7, MC_CUSTSERV:4.1`
- **Exact Source Quote**: *"BSBD accounts maximum liability Rs 5,000 where reporting is delayed 4 to 7 days"*
- **Reference Answer**: Customer liability is limited to Rs 5,000 for BSBD accounts under CIR_UNAUTH:7, while BSBD basic account rules are governed under MC_CUSTSERV:4.1.

### Question `q087`
- **Question**: **"What two RBI provisions govern customer compensation when an unsolicited credit card is issued and leads to mental anguish?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:6, RBIOS2021:15`
- **Exact Source Quote**: *"unsolicited card penalty equal to twice charges reversed under MD_CARDS:6, and up to Rs 1 lakh for mental anguish under RBIOS2021:15"*
- **Reference Answer**: MD_CARDS:6 mandates reversing charges plus 2x penalty, and references RBIOS2021:15 for awarding up to Rs 1 lakh for harassment and mental anguish.

### Question `q088`
- **Question**: **"What RBI rules govern the timeline for reporting unauthorized ATM card transactions versus the bank's compensation for delayed ATM failure reconciliation?"**
- **In Scope**: `true`
- **Gold Section(s)**: `CIR_UNAUTH:6, MC_CUSTSERV:5.12`
- **Exact Source Quote**: *"zero liability within 3 working days under CIR_UNAUTH:6, and T+5 reconciliation compensation under MC_CUSTSERV:5.12"*
- **Reference Answer**: CIR_UNAUTH:6 provides zero liability if reported within 3 days, while MC_CUSTSERV:5.12 mandates ₹100/day compensation for failed ATM reconciliations beyond T+5 days.

### Question `q089`
- **Question**: **"How do digital transaction alert requirements under digital security directions interact with customer liability notifications for unauthorized electronic debits?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_DIGISEC:34, CIR_UNAUTH:4`
- **Exact Source Quote**: *"mandatory alerts under MD_DIGISEC:34, and immediate customer notification channels under CIR_UNAUTH:4"*
- **Reference Answer**: MD_DIGISEC:34 mandates alerts for all debits and credits, while CIR_UNAUTH:4 requires banks to provide 24x7 reporting channels to enable customers to establish zero liability.

### Question `q090`
- **Question**: **"What provisions govern the closure of credit cards and the non-levy of charges on zero-balance accounts?"**
- **In Scope**: `true`
- **Gold Section(s)**: `MD_CARDS:8, MC_CUSTSERV:24.7`
- **Exact Source Quote**: *"card closure within 7 working days under MD_CARDS:8, and no unilateral zero-balance closure under MC_CUSTSERV:24.7"*
- **Reference Answer**: MD_CARDS:8 regulates credit card closure timelines and delay penalties, while MC_CUSTSERV:24.7 restricts closing zero-balance accounts unilaterally.

### Question `q091`
- **Question**: **"What is the minimum voting threshold for the Committee of Creditors to approve a corporate resolution plan under the Insolvency and Bankruptcy Code (IBC)?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Corporate insolvency under IBC 2016 is outside retail bank complaint rules.*
- **Reference Refusal**: Refused: Out of scope. IBC corporate insolvency proceedings are outside the retail banking complaint circulars.

### Question `q092`
- **Question**: **"What is the maximum Loan-to-Value (LTV) ratio allowed for commercial real estate loans exceeding Rupees 100 crore?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Commercial wholesale real estate financing rules are not covered.*
- **Reference Refusal**: Refused: Out of scope. Commercial real estate prudential limits are outside the retail consumer protection circulars.

### Question `q093`
- **Question**: **"Can Indian banks offer cryptocurrency derivative exchange trading to high-net-worth institutional clients?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Cryptocurrency and virtual digital asset derivatives are outside retail complaint circulars.*
- **Reference Refusal**: Refused: Out of scope. Crypto derivatives trading is not governed by retail banking complaint circulars.

### Question `q094`
- **Question**: **"What is the current all-in-cost ceiling for External Commercial Borrowings (ECB) benchmarked against SOFR?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *External commercial borrowings and SOFR benchmarks are wholesale forex regulations.*
- **Reference Refusal**: Refused: Out of scope. External Commercial Borrowings (ECB) regulations are outside retail complaint handling.

### Question `q095`
- **Question**: **"What percentage of Adjusted Net Bank Credit (ANBC) must domestic scheduled commercial banks allocate to small and marginal farmers under Priority Sector Lending?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Priority Sector Lending targets are prudential macro guidelines, not retail grievance rules.*
- **Reference Refusal**: Refused: Out of scope. Priority Sector Lending (PSL) allocation targets are outside the retail complaint circulars.

### Question `q096`
- **Question**: **"What is the minimum tier-1 capital adequacy ratio (CRAR) required for public sector banks under Basel III capital regulations?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Basel III capital adequacy guidelines are prudential bank solvency rules.*
- **Reference Refusal**: Refused: Out of scope. Basel III CRAR requirements are prudential bank capital rules, not complaint handling guidelines.

### Question `q097`
- **Question**: **"How are Sovereign Gold Bond (SGB) semiannual interest payments taxed under the Indian Income Tax Act?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *Taxation of Sovereign Gold Bonds is governed by Income Tax laws, not RBI complaint circulars.*
- **Reference Refusal**: Refused: Out of scope. Taxation rules for Sovereign Gold Bonds are governed by the Income Tax Act.

### Question `q098`
- **Question**: **"What is the mandatory percentage of project funds that a real estate developer must deposit in a designated RERA escrow bank account?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *RERA escrow account provisions are statutory real estate laws, not RBI retail grievance guidelines.*
- **Reference Refusal**: Refused: Out of scope. Real Estate Regulatory Authority (RERA) statutory escrow requirements are outside retail banking circulars.

### Question `q099`
- **Question**: **"What is the foreign direct investment (FDI) equity cap under the automatic route for non-scheduled civil air transport services?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *FDI caps in aviation are Department for Promotion of Industry and Internal Trade (DPIIT) rules.*
- **Reference Refusal**: Refused: Out of scope. Civil aviation foreign direct investment caps are governed by DPIIT/FDI policy.

### Question `q100`
- **Question**: **"What marine cargo risks are covered under an Institute Cargo Clause A insurance policy issued through Export Credit Guarantee Corporation (ECGC)?"**
- **In Scope**: `false`
- **Reason Out of Scope**: *ECGC marine trade insurance contracts are trade credit and insurance laws.*
- **Reference Refusal**: Refused: Out of scope. ECGC marine cargo insurance is outside retail consumer banking regulations.

