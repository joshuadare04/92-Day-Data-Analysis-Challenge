# Maven Coffee Shop Sales Analysis — Week 1

## 92-Day Data Analysis Challenge | Advanced Excel

This project is **Week 1** of my 92-Day Data Analysis Challenge, where I am building my data analysis skills through practical, project-based work.

For this project, I used the **Maven Coffee Shop Sales** dataset to analyze transaction data and turn it into business insights using Microsoft Excel.

The project covers data preparation, business analysis, product performance, pricing analysis, time-based analysis, dashboard development, and final recommendations.

---

## Project Overview

The dataset contains transaction records from **Maven Roasters**, a fictitious coffee shop operating across three locations in New York City.

The goal of this project was to move beyond simply calculating numbers and use Excel to answer practical business questions such as:

- How much revenue was generated?
- Which stores and categories performed best?
- Which products generated the most revenue?
- Does sales volume always translate into higher revenue?
- When are the busiest sales periods?
- What trends can be identified over time?
- What recommendations can be made from the findings?

---

## Dataset

**Dataset:** Maven Coffee Shop Sales

**Source:** Maven Analytics

**Records:** 149,116 transactions

**Fields:** 11

The dataset contains transaction dates, transaction times, store locations, product information, quantities, and pricing information.

The dataset is available through the Maven Analytics Data Playground.

Source: Maven Analytics — Coffee Shop Sales

---

## Tools Used

- Microsoft Excel
- Excel Tables
- Excel formulas
- Data cleaning and preparation
- Aggregation and ranking
- Data analysis
- Data visualization
- Dashboard development

---

## Project Workflow

The analysis was completed across seven days:

### Day 1 — Setup & Baseline

- Organized the dataset and workbook structure.
- Cleaned and prepared the transaction data.
- Converted the cleaned data into an Excel Table named `tbl_Sales`.
- Created a calculated **Sales** field using:

`Transaction Quantity × Unit Price`

### Day 2 — Business Analysis

Analyzed:

- Sales by store
- Sales by category
- Monthly sales trends
- Category contribution to total revenue

### Day 3 — Product Analysis

Analyzed:

- Total sales by product type
- Total quantity sold by product type
- Sales ranking
- Quantity ranking
- Differences between revenue and volume performance

### Day 4 — Pricing & Performance Analysis

Analyzed:

- Sales rank vs quantity rank
- Average selling price
- Price rank
- Sales vs price rank
- Product performance classification
- Rank gaps between sales and quantity performance

### Day 5 — Time Analysis

Analyzed:

- Sales by day of week
- Transactions by day of week
- Sales by hour
- Transactions by hour
- Average transaction value by hour

### Day 6 — Dashboard Development

Built an Excel dashboard containing:

- KPI cards
- Monthly Sales Trend
- Sales by Category
- Sales by Store
- Sales by Day of Week
- Sales by Hour
- Top 5 Products by Sales

### Day 7 — Final Insights & Recommendations

Reviewed the complete analysis and translated the findings into practical business recommendations.

---

## Key Metrics

| Metric | Result |
|---|---:|
| Total Sales | **$698,812.33** |
| Total Transactions | **149,116** |
| Total Quantity Sold | **214,470** |
| Average Transaction Value | **$4.69** |
| Product Types | **29** |
| Store Locations | **3** |

---

## Key Findings

### 1. Coffee and Tea dominated sales

Coffee generated **$269,952.45**, representing **38.63%** of total sales.

Tea generated **$196,405.95**, representing **28.11%**.

Together, Coffee and Tea generated **$466,358.40**, accounting for **66.74%** of total sales.

This makes them the two most important product categories by revenue.

---

### 2. Store performance was relatively balanced

| Store | Sales |
|---|---:|
| Hell's Kitchen | **$236,511.17** |
| Astoria | **$232,243.91** |
| Lower Manhattan | **$230,057.25** |

Hell's Kitchen recorded the highest sales, but the relatively small differences between the three locations show that overall store performance was fairly balanced.

---

### 3. Sales increased strongly over the period

February recorded the lowest monthly sales at **$76,145.19**.

Sales then increased consistently from March through June.

June recorded the highest monthly sales at **$166,485.88**.

This indicates a strong upward sales trend during the later months of the period analyzed.

---

### 4. Revenue and sales volume did not always tell the same story

The product analysis showed that sales revenue and quantity sold can produce different rankings.

For example:

- **Barista Espresso** ranked **#1 in sales** but **#3 in quantity sold**.
- **Brewed Chai Tea** ranked **#1 in quantity sold** but **#2 in sales**.

This shows why product performance should be evaluated using multiple metrics rather than sales volume alone.

---

### 5. Morning hours were particularly important

**10 AM** was the strongest individual sales hour, generating:

- **$88,673.39 in sales**
- **18,545 transactions**

The period from **8 AM to 10 AM** generated **$256,542.79**, representing **36.71% of total sales**.

This makes the morning period an important operational window.

---

### 6. Daily sales were relatively close across the week

Monday recorded the highest daily sales at **$101,677.28**.

Saturday recorded the lowest daily sales at **$96,894.48**.

However, Friday recorded the highest number of transactions at **21,701**.

This demonstrates that the day with the highest transaction volume was not necessarily the day with the highest revenue.

---

## Recommendations

### 1. Prioritize Coffee and Tea

Since Coffee and Tea account for **66.74% of total sales**, these categories should remain a major focus when considering inventory, promotions, and product availability.

### 2. Optimize morning operations

The strong performance between **8 AM and 10 AM** suggests that staffing, inventory availability, and service capacity should be prepared for the morning rush.

### 3. Investigate the drivers of monthly growth

The increase from February through June could be investigated further to identify the factors contributing to the growth and determine whether those strategies can be sustained.

### 4. Evaluate products using multiple metrics

Product decisions should consider:

- Revenue
- Quantity sold
- Average selling price
- Sales rank
- Quantity rank
- Rank differences

rather than relying on a single metric.

### 5. Compare successful practices across stores

Since the three stores performed relatively similarly, comparing their operating practices could help identify strategies that can improve performance across all locations.

---

## Dashboard

The final Excel dashboard brings the major findings together into a single visual report.

### Dashboard Overview

![Dashboard Main](Dashboard/dashboard-main.png)

### Sales Analysis

![Sales Analysis Dashboard](Dashboard/dashboard-sales-analysis.png)

### Time Analysis

![Time Analysis Dashboard](Dashboard/dashboard-time-analysis.png)

---

## Project Structure

```text
Week-01-Maven-Coffee-Shop-Sales/
│
├── README.md
│
├── Excel-Analysis/
│   └── Maven_Coffee_Shop_Sales_Analysis.xlsx
│
├── Documentation/
│   ├── Day-01-Setup-and-Baseline.md
│   ├── Day-02-Business-Analysis.md
│   ├── Day-03-Product-Analysis.md
│   ├── Day-04-Pricing-and-Performance.md
│   ├── Day-05-Time-Analysis.md
│   ├── Day-06-Dashboard.md
│   └── Day-07-Final-Insights-and-Recommendations.md
│
└── Dashboard/
    ├── dashboard-main.png
    ├── dashboard-sales-analysis.png
    └── dashboard-time-analysis.png
```

---

## Project Outcome

This project took the analysis from raw transaction data to a completed business intelligence workflow:

**Data Preparation → Business Analysis → Product Analysis → Pricing & Performance → Time Analysis → Dashboard → Insights & Recommendations**

The final result is an Excel-based analysis and dashboard that demonstrates my ability to clean, analyze, visualize, and communicate insights from transactional data.

---

## Skills Demonstrated

- Excel data cleaning
- Excel Tables
- Data aggregation
- Excel formulas
- Ranking and comparison
- Business analysis
- Time-series analysis
- Data visualization
- Dashboard development
- KPI design
- Insight generation
- Data-driven recommendations

---

## Challenge Progress

**Week 1 of 13 complete**

**Day 7/92 complete**

**October Focus: Advanced Excel**

The next stage of the challenge will continue building on these analytical skills with another dataset and progressively more advanced Excel techniques.