# Shop-Performance-Analysis
# 🛒 Shop Performance Analysis

## 📊 Project Overview

The **Shop Performance Analysis** provides a clear view of an online shop's performance from **January 2024 to June 2026**. The analysis combines customer, order, product and payment data to identify key trends, business drivers and areas for improvement.

The project transforms raw data into **interactive visualisations, business insights and practical recommendations** to support better operational and business decision-making.

## 🎯 Objectives

The analysis aims to answer key business questions, including:

* How much revenue did the shop generate?
* How many orders were processed?
* Provide the average unit prices for all the products?
* Is revenue growing, declining or remaining stable?
* Which products and categories generate the most revenue?
* Which products sell the most units and how much revenue do they produce?
* Which cities and customer segments are most valuablevor generates most revenue?
* What percentage of orders are cancelled or returned?
* Which year produced the most revenue?
* Which payment methods experience the highest failure rates?
* Povide product categories that produced the most revenue in ascending order?
* What actions can management take based on the findings?

## 📁 Data Sources

The project uses four datasets:

| Dataset     | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| `customers` | Customer information, demographics, cities and customer segments      |
| `orders`    | Order transactions, quantities, discounts, payment methods and status |
| `payments`  | Payment attempts and payment statuses                                 |
| `products`  | Product names, categories and unit prices                             |

The tables are connected using:

```text
Orders
 ├── CustomerID → Customers
 ├── ProductID  → Products
 └── OrderID    → Payments
```

## 🧹 Data Preparation

The data preparation process includes:

* Missing-value checks
* Duplicate checks
* Data-type validation
* Inconsistent city-name checks
* Invalid-value checks
* Broken-link checks
* Joining the four datasets
* Creating calculated fields
* Revenue validation

### Revenue Calculation

```text
Revenue = Quantity × UnitPrice × (1 − Discount)
```

Additional analytical fields include:

* Year
* Month
* Month Name
* Customer Segment
* Revenue
* Order Status
* Payment Status

## 📈 Dashboard & Visualisations

The interactive dashboard includes:

### Key Performance Indicators

* Total Revenue
* Total Orders
* Units Sold
* Average Order Value
* Number of Customers
* Cancellation Rate
* Return Rate
* Payment Failure Rate

### Revenue Analysis

* Monthly revenue trends
* Revenue by category
* Revenue by product
* Revenue by customer segment
* Revenue by city

### Product Analysis

* Top-performing products
* Units sold by product
* Revenue by category
* Revenue versus units sold

### Customer Analysis

* Revenue by customer segment
* Orders by customer segment
* Average Order Value by segment
* Revenue by city
* Customer distribution

### Order & Payment Analysis

* Order status analysis
* Cancellation and return rates
* Payment status analysis
* Payment failure rates by payment method

### Discount Analysis

* Discount versus order value
* Discount versus revenue
* Revenue by discount level

### Interactive Visuals

The dashboard uses:

* 📊 Bar charts
* 📈 Line charts
* 🔥 Heatmaps
* 🔵 Scatter plots
* 🍩 Donut charts where appropriate
* 📋 Analytical tables
* 🎯 KPI cards
* 💡 Insight cards
* ✅ Recommendation cards

## 🔥 Heatmap Analysis

Heatmaps are used to identify patterns across:

* Year and month
* Day of week and month
* City and customer segment

These visuals help identify periods, locations and customer groups with stronger or weaker performance.

## 💡 Business Insights

The dashboard automatically highlights important findings from the analysis, including:

* Revenue trends
* Best-performing products and categories
* Most valuable customer segments
* Highest-performing cities
* Operational issues
* Payment problems
* Discount-related patterns

Each major finding includes a **"So What?"** explanation to translate the analysis into a business implication.

## 🚀 Recommendations

The analysis concludes with **three practical recommendations** supported by the underlying data.

Recommendations focus on areas such as:

1. Revenue and product opportunities
2. Customer and market opportunities
3. Operational and payment improvements

Recommendations are based on the actual analysis rather than generic business assumptions.

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Databricks**
* **Excel**
* **Lovable**
* **GitHub**

## 📂 Project Structure

```text
Shop-Performance-Analysis/
│
├── data/
│   ├── customers
│   ├── orders
│   ├── payments
│   └── products
│
├── notebooks/
│   └── shop_performance_analysis
│
├── dashboard/
│   └── shop_performance_dashboard
│
├── README.md
└── requirements.txt
```

## 📌 Key Deliverable

The final deliverable is an **interactive Shop Performance Dashboard** that provides:

**Data → Analysis → Insights → Recommendations**

The dashboard is designed for business users and focuses on presenting complex analysis in a simple, visual and actionable format.

## 👤 Author

**Khutso Joshua Monyebodi**

---

⭐ If you find this project useful, feel free to star the repository.

