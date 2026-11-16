---
name: "asc-606-revenue"
description: "Use when analyzing, documenting, or booking revenue recognition under ASC 606: contracts, performance obligations, variable consideration, SSP allocation, over-time vs point-in-time, modifications, contract balances."
---

# ASC 606 — Revenue from Contracts with Customers

## Modes
- **Analyze/memo**: work through the five steps for a contract.
- **Book**: produce the schedule and entries.
- **Explain/FAR**: on "quiz me", pose a contract and grade the user's five-step answer.

## Inputs (list what's missing)
- Contract terms: parties, deliverables, price, payment terms, and options or rights such as renewals, returns, warranties, and discounts.
- Delivery and acceptance dates.
- Standalone selling prices, or the data needed to estimate them.
- Any variable elements (bonuses, penalties, rebates, usage fees).
- Any modifications to the contract.

## Calculation rule
Compute allocations and schedules in code when available, or show the arithmetic.

## Step 1 — Identify the contract
A contract exists when all of these hold:
- The parties have approved it.
- Rights and payment terms are identifiable.
- It has commercial substance.
- Collection is **probable**.

If any criterion fails, consideration received is a liability until the criteria are met or the cash is nonrefundable and the contract is complete or terminated.

Combine contracts entered at or near the same time with the same customer if they were negotiated as a package, if the price of one depends on the other, or if together they form a single performance obligation.

## Step 2 — Performance obligations
- A good or service is a separate obligation if it is **distinct**: the customer can benefit from it on its own or with readily available resources, AND it is separately identifiable within the contract.
- It is NOT separately identifiable if it involves significant integration, significant customization, or is highly interdependent with other items.
- A series of substantially the same services transferred over time counts as one obligation.

Watch these specific traps:
- **Warranties.** An assurance-type warranty is not an obligation; accrue it under ASC 460. A service-type warranty, or one sold separately, is an obligation.
- **Options.** An option is a material right, and therefore an obligation, only if it gives a discount the customer would not otherwise get.
- **Principal vs. agent.** Does the entity control the good before transfer? Indicators are primary responsibility, inventory risk, and pricing discretion. An agent recognizes only its net fee.
- **Licenses.** A functional license (software) is recognized at a point in time. A symbolic license (brand) is recognized over time.

## Step 3 — Transaction price
- **Variable consideration.** Estimate it using the expected value (many outcomes) or the most likely amount (binary outcomes).
- Apply the **constraint**: include the estimate only to the extent a significant reversal is not probable.
- **Significant financing component.** Adjust if one exists. The practical expedient applies when the gap between payment and transfer is 1 year or less.
- **Noncash consideration** is measured at fair value.
- **Consideration payable to the customer** reduces revenue unless it is for a distinct good or service.

## Step 4 — Allocate
- Allocate the transaction price on relative standalone selling price (SSP).
- If SSP isn't observable, estimate it by the adjusted market approach, expected cost plus margin, or the residual approach. Residual is allowed only when SSP is highly variable or uncertain.
- Allocate a discount proportionately, unless there is evidence it relates to specific obligations.

## Step 5 — Recognize
Recognize **over time** if any one of these is met:
1. The customer simultaneously receives and consumes the benefit.
2. The customer controls the asset as it is created or enhanced.
3. The asset has no alternative use AND the entity has an enforceable right to payment for work to date.

Over-time obligations need a measure of progress:
- Output methods, or input methods such as cost-to-cost.
- Exclude costs that don't reflect progress, such as wasted materials and uninstalled materials (recognize those at cost).

Otherwise recognize at a **point in time**. Indicators of transfer are a right to payment, legal title, physical possession, risks and rewards, and acceptance.
- Bill-and-hold requires all of the following: a substantive reason, separate identification, readiness for transfer, and no ability to redirect the goods.
- Consignment means no revenue until the end customer buys.

## Contract modifications
- If the modification adds distinct goods at SSP, treat it as a **separate contract**.
- If the remaining goods are distinct, account **prospectively** (terminate the old contract and create a new one).
- If the remaining goods are not distinct, make a **cumulative catch-up** adjustment.

## Contract costs and balances
- Capitalize incremental costs of obtaining a contract, such as commissions, and amortize them over the benefit period. The practical expedient allows expensing if that period is 1 year or less.
- Capitalize fulfillment costs only if they relate to the contract, create resources, and are recoverable.
- Balance sheet labels:
  - Receivable: the right to payment is unconditional.
  - Contract asset: the right is conditional on something other than time.
  - Contract liability: cash received ahead of performance.

## Tie-outs
- The allocation sums to the transaction price.
- Cumulative revenue plus the contract liability, less the contract asset, reconciles to cumulative billings.
- The schedule's total equals the transaction price, adjusted for any constraint releases.

## Output
1. A five-step memo with the conclusion and support for each step. Label judgments as judgments.
2. The allocation table.
3. The recognition schedule by period.
4. Journal entries.
5. Contract balances.
6. Flags for the reviewer.

## Worked example
Facts:
- Equipment plus 2 years of service sold for 1,200 total, paid upfront.
- SSPs: equipment 1,000; service 500 (total 1,500).
- The equipment is delivered on day 1.

Allocation:
- Equipment: 1,200 × 1,000/1,500 = **800**, recognized at delivery.
- Service: 1,200 × 500/1,500 = **400**, recognized at 200 per year (16.67 per month).

Entries:
- Day 1: Dr Cash 1,200 / Cr Revenue 800, Cr Contract liability 400.
- Each month: Dr Contract liability 16.67 / Cr Revenue 16.67.

## Boundaries
Principal vs. agent, the constraint, SSP estimates, and the over-time criteria are judgments. Present the evidence and a recommendation, then flag them for technical or reviewer sign-off.