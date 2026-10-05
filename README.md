# Shop-Performance-Analysis
# Shop Performance Analysis (Jan 2024 – Jun 2026)

A beginner data analysis case study (BrightLearn) that turns raw online-shop data into a clear performance picture for the Head of Operations.

## Objective

Measure how the online shop performed between January 2024 and June 2026, explain what is driving the results, and give three recommendations the Head of Operations can act on. The audience is non-technical, so the outputs use simple numbers, clear charts and plain-language takeaways.

## Business Questions

1. How much revenue did the shop make, from how many orders, and what is the average order value?
2. Is revenue growing, shrinking or flat month by month? Are there seasonal peaks?
3. Which products and categories earn the most revenue? Which sell the most units? Are they the same?
4. Which cities and customer segments (New, Regular, VIP) are most valuable?
5. What share of orders are cancelled or returned? What share of payments fail, and do some payment methods fail more often?
6. Do bigger discounts lead to bigger orders, or just lower revenue?

## Deliverables

| File | Description |
|---|---|
| `Shop_Performance_Presentation.pptx` | Conducted a presentation using PowerPoint |
| `Shop_Performance_Cleaned.xlsx | This is a final results from Databricks as an Excel file|
| Dashboard | Interactive dashboard: https://pixel-perfect-view-4937.lovable.app/ |
| `Shop_Performance.xlsx` | Source data: orders joined to customers, products and payments |
| `Shop_Performance_Case_Study.pdf` | Original case study brief |

## Tools Used

| Tool | Purpose |
|---|---|
| Excel | Source workbook |
| DataBricks to codePython (pandas, numpy) | Data cleaning, joins, new columns, aggregation |
| PowerBI | Did my visuals on PowerBI |
| PowerPoint | Used to build a presentation |
| Lovable | Interactive dashboard |

## Method

**Revenue rule:** `Quantity × UnitPrice × (1 − Discount)`, counted only for orders that are **Completed** and **Paid**. Cancelled, returned, failed and refunded orders are not counted, because the shop did not keep that money.

**Cleaning decisions**

| Problem | Action |
|---|---|
| There were 120 duplicates which were removed | Removed (50 000 orders remain) |
| 30 orders linked to a non-existent customer (I D 999999) | Kept for product totals; shown as Unknown in city and segment views |
| 80 quantities and 220 discounts filled with the average | Replaced with 2 units and a 5% discount |
| Unknown city (665) and payment method (450) | Kept as Unknown, not guessed |
| Year and Month built from signup date | Rebuilt from order date |
| Duplicates, inconsistent product prices | Checked; none found |
|Null Values| Checked and removed either with mode, mean, Unknown |

## Key Results

- **Revenue:** R2.997M from 42,825 paid, completed orders (49,975 orders placed). Average order value is R70.
- **Trend:** about R105k a month through 2024–2025, then about R71k a month from Feb 2026 (−32% vs the same months of 2025). The fall appears in every category, and there are no seasonal peaks.
- **Products:** Electronics earns 51% of revenue. Stationery sells many units but earns 2%.
- **Customers:** Tehran contributes 27.5% of revenue and Regular customers 55%.
- **Lost orders:** 14.3% of orders earn no revenue (R505k at list value). Payment failure rates are 3.6–4.0% on every method.
- **Discounts:** units per order stay near 1.9 at every discount level, while average order value falls from R75 (no discount) to R56 (30%).

## Recommendations

1. Investigate and fix the February 2026 drop in orders (checking traffic, marketing, website or checkout, and stock).
2. Cap discounts at 10% and test for one quarter.
3. Recover the 14.3% of orders that earn nothing by retrying failed payments and recording cancellation and return reasons.

## Data Caveats

- Monitor is priced at R21, which looks too low; the price should be confirmed.
- 28% of orders are dated before the customer's signup date, so segment labels may be unreliable.
- Some Cancelled orders show as Paid; none are counted as revenue.
- The analysis shows association, not proof of cause, and there is no cost data, so profit is not measured.



