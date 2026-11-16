"""Derive every numeric expected value in the asc-842-lessee answer key from first principles.

Run:  python compute_key.py            -> prints each check and writes computed_key.json
      python compute_key.py --verify   -> also compares against answer_key.json and exits 1 on any mismatch

Conventions (same as cases.md): annual compounding at the stated annual rate unless a case
gives a monthly rate; a payment at period t is discounted by (1 + r) ** t, including fractional t.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def pv(payments, rate):
    """payments: list of (t, amount). Returns the present value at t = 0."""
    return sum(amount / (1 + rate) ** t for t, amount in payments)


def annuity_arrears(amount, n, rate, start=1):
    return [(t, amount) for t in range(start, start + n)]


def r2(x):
    return round(x + 0.0, 2)


key = {}


def check(case, name, value):
    key[f"{case}:{name}"] = r2(value) if isinstance(value, (int, float)) else value


# Case 1 - 5 yr, 12,000 arrears, 6%, FV 100,000, life 10 -> operating
c1_L = pv(annuity_arrears(12_000, 5, 0.06), 0.06)
c1_accr = c1_L * 0.06
check(1, "pv_test_pct", c1_L / 100_000 * 100)            # 50.55% < 90%
check(1, "term_test_pct", 5 / 10 * 100)                  # 50% < 75%
check(1, "initial_liability_and_rou", c1_L)
check(1, "y1_accretion", c1_accr)
check(1, "y1_rou_amortization", 12_000 - c1_accr)
check(1, "y1_lease_expense", 12_000)

# Case 2 - 4 yr, in advance, 3% escalation, 5%, IDC 2,000, incentive 4,000
pays = [20_000, 20_600, 21_218, 21_854.54]
c2_L = pv([(t, pays[t]) for t in range(1, 4)], 0.05)    # after the t = 0 payment
c2_rou = c2_L + pays[0] + 2_000 - 4_000
c2_sl = (sum(pays) + 2_000 - 4_000) / 4
check(2, "liability_after_commencement_payment", c2_L)
check(2, "rou_asset", c2_rou)
check(2, "straight_line_cost", c2_sl)
check(2, "y1_accretion", c2_L * 0.05)
check(2, "y1_rou_amortization", c2_sl - c2_L * 0.05)

# Case 3 - 7 yr, 50,000 arrears, 7% implicit, life 9, FV 400,000 -> finance (77.8%)
c3_L = pv(annuity_arrears(50_000, 7, 0.07), 0.07)
check(3, "term_test_pct", 7 / 9 * 100)
check(3, "pv_test_pct", c3_L / 400_000 * 100)
check(3, "initial_liability", c3_L)
check(3, "y1_interest", c3_L * 0.07)
check(3, "y1_amortization", c3_L / 7)
check(3, "y1_total_expense", c3_L * 0.07 + c3_L / 7)

# Case 4 - lessee RVG 20,000, expected residual 18,000 -> 2,000 probable
c4_pay = pv(annuity_arrears(30_000, 4, 0.06), 0.06)
check(4, "pv_test_numerator_full_rvg", c4_pay + 20_000 / 1.06 ** 4)
check(4, "pv_test_threshold", 0.90 * 120_000)
check(4, "initial_liability", c4_pay + 2_000 / 1.06 ** 4)

# Case 5 - reasonably certain purchase option 10,000; useful life 8
c5_L = pv(annuity_arrears(25_000, 5, 0.08) + [(5, 10_000)], 0.08)
check(5, "initial_liability", c5_L)
check(5, "y1_amortization_8yr", c5_L / 8)
check(5, "y1_interest", c5_L * 0.08)

# Case 7 - CPI-based payments measured at the commencement index
check(7, "initial_liability", pv(annuity_arrears(40_000, 5, 0.05), 0.05))

# Case 8 - percentage rent excluded
check(8, "initial_liability", pv(annuity_arrears(60_000, 3, 0.06), 0.06))

# Case 9 - last 25% of life: major-part test skipped; PV test
check(9, "pv_test_pct", pv(annuity_arrears(5_000, 2, 0.06), 0.06) / 20_000 * 100)

# Case 10 - current portion = principal reduction over next 12 months (Case 1)
check(10, "current_portion", 12_000 - c1_accr)
check(10, "noncurrent_portion", c1_L - (12_000 - c1_accr))

# Case 11 - TI reimbursement receivable at t = 0.5 reduces the liability
c11_L = pv(annuity_arrears(36_000, 5, 0.06), 0.06) - 15_000 / 1.06 ** 0.5
check(11, "initial_liability", c11_L)
check(11, "rou_asset", c11_L)

# Case 12 - reasonably certain termination at end of Year 3, 8,000 penalty
check(12, "initial_liability", pv(annuity_arrears(20_000, 3, 0.05) + [(3, 8_000)], 0.05))

# Case 13 - combined components: fixed CAM in, variable utilities out
check(13, "initial_liability", pv(annuity_arrears(56_000, 3, 0.05), 0.05))

# Case 14 - Case 4 at end of Year 2: RVG expectation falls to 14,000 -> 6,000 probable; keep 6%
c14_before = pv(annuity_arrears(30_000, 2, 0.06) + [(2, 2_000)], 0.06)
c14_after = pv(annuity_arrears(30_000, 2, 0.06) + [(2, 6_000)], 0.06)
check(14, "carrying_before", c14_before)
check(14, "remeasured", c14_after)
check(14, "adjustment", c14_after - c14_before)

# Case 15 - Case 1 at end of Year 2: extend 2 years, remeasure at updated 7%
c15_before = pv(annuity_arrears(12_000, 3, 0.06), 0.06)
c15_after = pv(annuity_arrears(12_000, 5, 0.07), 0.07)
check(15, "carrying_before", c15_before)
check(15, "remeasured_liability", c15_after)
check(15, "rou_adjustment", c15_after - c15_before)

# Case 16 - operating ROU impaired to 20,000 at end of Year 2; then SL amortization
c16_rou_before = pv(annuity_arrears(12_000, 3, 0.06), 0.06)   # operating, no IDC: ROU = liability
check(16, "rou_before_impairment", c16_rou_before)
check(16, "impairment_loss", c16_rou_before - 20_000)
check(16, "y3_accretion", c16_rou_before * 0.06)
check(16, "y3_rou_amortization", 20_000 / 3)
check(16, "y3_total_expense", c16_rou_before * 0.06 + 20_000 / 3)

# Case 17 - contingency resolves: 10,000 fixed for Years 3-5; keep original 6%
check(17, "adjustment", pv(annuity_arrears(10_000, 3, 0.06), 0.06))

# Case 18 - 24 months, months 1-3 free, 4,000 in arrears months 4-24, 0.5% monthly
c18_L = pv([(t, 4_000) for t in range(4, 25)], 0.005)
c18_sl = 4_000 * 21 / 24
check(18, "initial_liability", c18_L)
check(18, "monthly_sl_cost", c18_sl)
check(18, "m1_rou_amortization", c18_sl - c18_L * 0.005)
check(18, "m1_end_liability", c18_L * 1.005)

# Case 19 - lessor-controlled extension is always in the term: 5 years
check(19, "initial_liability", pv(annuity_arrears(10_000, 5, 0.05), 0.05))

# Case 20 - third-party RVG excluded from the PV test
c20_L = pv(annuity_arrears(20_000, 5, 0.06), 0.06)
check(20, "pv_test_pct", c20_L / 100_000 * 100)
check(20, "initial_liability", c20_L)

# Case 21 - full deliverable: 4 yr, 15,000 arrears, 6%, IDC 1,000, incentive 2,000
c21_L = pv(annuity_arrears(15_000, 4, 0.06), 0.06)
c21_sl = (60_000 + 1_000 - 2_000) / 4
check(21, "initial_liability", c21_L)
check(21, "rou_asset", c21_L + 1_000 - 2_000)
check(21, "straight_line_cost", c21_sl)
check(21, "y1_rou_amortization", c21_sl - c21_L * 0.06)
check(21, "current_portion_at_commencement", 15_000 - c21_L * 0.06)
check(21, "imputed_interest", 60_000 - c21_L)


def main():
    for k, v in key.items():
        print(f"{k:45s} {v:>14,.2f}" if isinstance(v, float) or isinstance(v, int) else f"{k:45s} {v}")
    (HERE / "computed_key.json").write_text(json.dumps(key, indent=2))
    if "--verify" in sys.argv:
        published = json.loads((HERE / "answer_key.json").read_text())
        bad = 0
        for row in published["checks"]:
            ref = row.get("computed")
            if not ref:
                continue
            got = key[ref]
            if abs(got - row["expected"]) > row["tolerance"]:
                bad += 1
                print(f"MISMATCH case {row['case']} {row['check']}: key {row['expected']} vs computed {got}")
        n = sum(1 for r in published["checks"] if r.get("computed"))
        print(f"\nVerified {n - bad}/{n} numeric answer-key values against first-principles math.")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
