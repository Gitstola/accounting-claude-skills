# Test cases: asc-842-lessee

21 cases, 64 pass/fail checks. This file is the only thing the blind test-taker sees besides the skill. Expected answers live in `answer_key.json`, and every expected number is derived from first principles in `compute_key.py`.

## Conventions

US GAAP, lessee only. Annual compounding at the stated annual rate unless a case gives a monthly rate; discount a payment at period t by (1 + r)^t, including fractional t. Commencement is January 1, Year 1 unless stated. Answer only what each case asks: classification and the requested numbers, each clearly labeled, plus one line of reasoning. Round to cents. Case 21 is the exception: it asks for the skill's full deliverable.

### Case 1
Equipment lease. Term 5 years; no renewal, termination, or purchase options; no ownership transfer; no residual value guarantee. Payments of $12,000 annually in arrears. IBR 6% (implicit rate not determinable). No initial direct costs, incentives, or prepaid rent. Asset fair value $100,000; economic life 10 years; not specialized. Questions: (a) classification; (b) initial lease liability and ROU asset; (c) Year 1 liability accretion, Year 1 ROU amortization, and Year 1 total lease expense.

### Case 2
Office lease. Term 4 years. Annual payments in advance each January 1: Year 1 $20,000, increasing 3% per year (Year 2 $20,600; Year 3 $21,218; Year 4 $21,854.54). The Year 1 payment is made on the commencement date. IBR 5%. The lessee paid a $2,000 broker commission that is an initial direct cost. The landlord paid the lessee a $4,000 cash incentive on the commencement date. Building fair value $5,000,000; economic life 40 years. No options or guarantees. Questions: (a) classification; (b) lease liability immediately after the commencement-date payment; (c) ROU asset at commencement; (d) annual straight-line lease cost; (e) Year 1 liability accretion and Year 1 ROU amortization.

### Case 3
Machine lease. Term 7 years; economic life 9 years; fair value $400,000. Payments of $50,000 annually in arrears. The implicit rate of 7% is readily determinable. No ownership transfer, purchase option, or residual value guarantee; not specialized. Questions: (a) classification, showing the tests; (b) initial lease liability; (c) Year 1 interest, amortization, and total expense; (d) statement of cash flows classification of the Year 1 payment.

### Case 4
Vehicle fleet lease. Term 4 years; economic life 8 years; fair value $120,000. Payments of $30,000 annually in arrears. Rate 6%. The lessee guarantees the lessor that the residual value at the end of the term will be at least $20,000. The lessee expects the residual value to be $18,000. No other options; not specialized. Questions: (a) classification, showing the present value test numbers; (b) initial lease liability.

### Case 5
Equipment lease. Term 5 years; useful life 8 years; fair value $140,000. Payments of $25,000 annually in arrears. Rate 8%. The lessee may buy the asset at the end of Year 5 for $10,000 and is reasonably certain to do so. Questions: (a) classification; (b) initial lease liability; (c) ROU amortization period and Year 1 amortization; (d) Year 1 interest.

### Case 6
Warehouse lease. Noncancellable term of 12 months at $3,000 per month. The lessee has an option to renew for another 12 months at the same rent and, because it is installing significant leasehold improvements, is reasonably certain to renew. The lessee has elected the short-term lease exemption for this asset class. Questions: (a) can the lessee apply the short-term exemption to this lease? (b) what does it recognize at commencement?

### Case 7
Retail space lease, classified as operating. Term 5 years; payments in arrears. The Year 1 payment is $40,000, and each later payment is adjusted by the change in CPI, with the commencement-date CPI as the base. IBR 5%. In Year 2, CPI rose 3%, so the Year 2 payment is $41,200. Questions: (a) initial lease liability; (b) accounting for the extra $1,200 in Year 2; (c) does the CPI change trigger remeasurement?

### Case 8
Store lease, classified as operating. Term 3 years. Fixed rent of $60,000 annually in arrears, plus 2% of annual sales above $1,000,000. The lessee expects sales of $1,500,000 per year. IBR 6%. Questions: (a) initial lease liability; (b) treatment of the percentage rent.

### Case 9
The lessee leases a used crane. Total economic life is 10 years, and 8 years have already elapsed (2 years remain). Lease term 2 years. Payments of $5,000 annually in arrears. IBR 6%. Fair value $20,000. No ownership transfer, purchase option, or residual value guarantee; not specialized. Questions: classify the lease, showing how each of the five classification tests applies.

### Case 10
Using Case 1's lease: at commencement, what amount of the lease liability is presented as current, and what amount as noncurrent?

### Case 11
Office lease, classified as operating. Term 5 years. Payments of $36,000 annually in arrears. IBR 6%. The lease requires the landlord to reimburse the lessee $15,000 for tenant improvements that are the lessee's assets. The reimbursement amount is fixed and will be paid exactly 0.5 years after commencement. No incentives were received at or before commencement. No initial direct costs. Questions: (a) initial lease liability; (b) ROU asset at commencement.

### Case 12
Equipment lease, classified as operating. Stated term 5 years. Payments of $20,000 annually in arrears. The lessee may terminate at the end of Year 3 by paying an $8,000 penalty; because of planned equipment upgrades, the lessee is reasonably certain to terminate at the end of Year 3. IBR 5%. Questions: (a) lease term; (b) initial lease liability.

### Case 13
Office lease, classified as operating. Term 3 years. Annual payments in arrears: base rent of $50,000 plus a fixed common-area maintenance (CAM) charge of $6,000. The lessee also reimburses the landlord's actual utility costs (variable, about $4,000 per year). The lessee has elected the practical expedient not to separate lease and nonlease components. IBR 5%. Questions: (a) initial lease liability; (b) treatment of the utilities.

### Case 14
Continue Case 4. At the end of Year 2, after the Year 2 payment, the lessee now expects the residual value at the end of the term to be $14,000. The lessee's current IBR is 8%. Questions: (a) does the lessee remeasure the liability, and with which discount rate? (b) carrying amount of the liability before remeasurement, the remeasured liability, and the adjustment to the ROU asset.

### Case 15
Continue Case 1. At the end of Year 2, after the Year 2 payment, the lessee and lessor agree to extend the lease by 2 years (7 years in total) at the same $12,000 annual payment. No additional underlying asset is added. The lessee's IBR on the modification date is 7%. Questions: (a) how is the modification accounted for, and with which discount rate? (b) carrying amount before the modification, the remeasured lease liability, and the adjustment to the ROU asset.

### Case 16
Equipment lease, classified as operating. Term 5 years; payments of $12,000 annually in arrears; IBR 6%; no initial direct costs, incentives, or prepaid rent. At the end of Year 2, after the Year 2 payment, the lessee tests the asset group for impairment and writes the ROU asset down to its fair value of $20,000. Questions: (a) ROU carrying amount before the impairment and the impairment loss; (b) Year 3 liability accretion, Year 3 ROU amortization, and Year 3 total lease expense.

### Case 17
Warehouse lease, classified as operating. Term 5 years; payments in arrears. Fixed rent is $50,000 per year. An additional $10,000 per year is payable only if the lessee's local revenue exceeds a threshold, and at commencement this payment is variable and not a lease payment. Rate at commencement 6%. At the end of Year 2, after the Year 2 payment, the contingency is resolved: the $10,000 becomes fixed and payable for each of Years 3 to 5. The lessee's IBR at that date is 8%. Questions: (a) which discount rate is used to remeasure? (b) the adjustment to the lease liability and ROU asset.

### Case 18
Retail kiosk lease, classified as operating. Term 24 months. Months 1 to 3 are rent-free. Months 4 to 24 require $4,000 per month, paid in arrears at the end of each month. Use a monthly rate of 0.5% (6% ÷ 12). No initial direct costs or other incentives. Questions: (a) initial lease liability; (b) monthly straight-line lease cost; (c) Month 1 liability accretion, Month 1 ROU amortization, and the lease liability at the end of Month 1.

### Case 19
Equipment lease. Noncancellable term 3 years; payments of $10,000 annually in arrears. The lessor (not the lessee) holds an option to extend the lease by 2 more years at the same rent. IBR 5%. Operating lease. Questions: (a) lease term; (b) initial lease liability.

### Case 20
Vehicle lease. Term 5 years; payments of $20,000 annually in arrears; rate 6%. Fair value $100,000; economic life 9 years. The lessor purchased a residual value guarantee of $25,000 from an unrelated third-party insurer; the lessee has no obligation under it. No ownership transfer or purchase option; not specialized. Questions: (a) classification, showing the present value test numbers; (b) initial lease liability.

### Case 21
For this case, produce the skill's full deliverable exactly as you would for a client file, including every part of the skill's Output section. Copier fleet lease. Term 4 years; payments of $15,000 annually in arrears; IBR 6% (implicit rate not determinable). The lessee paid $1,000 of initial direct costs, and the lessor paid the lessee a $2,000 cash incentive at commencement. Fair value $80,000; economic life 8 years. No options, guarantees, or ownership transfer; not specialized. The client's year-end is December 31. Provide journal entries for commencement and for Year 1.
