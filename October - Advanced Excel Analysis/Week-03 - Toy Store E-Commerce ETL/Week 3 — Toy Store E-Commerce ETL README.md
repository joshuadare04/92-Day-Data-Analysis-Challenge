# Week 3: Toy Store E-Commerce ETL

**92-Day Data Analysis Challenge | October — Advanced Excel**

## Project Overview

This project focuses on building a refreshable ETL workflow using Excel Power Query to clean, transform, combine, and validate e-commerce data.

Using the Maven Fuzzy Factory dataset, I developed a workflow that connects order, product, and refund information to analyse sales performance, profitability, refund patterns, and trends over time.

The project demonstrates how raw business data can be transformed into a structured, analysis-ready dataset and used to develop an interactive Excel dashboard.

## Project Objectives

- Import and inspect multiple CSV datasets.
- Clean and transform data using Power Query.
- Merge related tables using appropriate join operations.
- Validate relationships and check for duplicate records.
- Calculate sales, cost of goods sold (COGS), gross profit, and net sales after refunds.
- Analyse product performance, profitability, and refund ratios.
- Build an interactive Excel dashboard for business insights.

## Tools Used

- **Microsoft Excel:** Data analysis, PivotTables, PivotCharts, slicers, KPI cards, and dashboard development.
- **Power Query:** Data extraction, transformation, merging, cleaning, and validation.
- **GitHub:** Project versioning, documentation, and portfolio presentation.

## ETL Workflow

The project follows three main stages:

### 1. Extract

Imported the source CSV files into Power Query, including:

- `orders`
- `order_items`
- `order_item_refunds`
- `products`
- `website_sessions`
- `website_pageviews`

The data dictionary was also retained as a reference for understanding the dataset.

### 2. Transform

Performed the following operations:

- Inspected column quality and data types.
- Merged related tables to bring order, product, and refund information together.
- Expanded relevant columns from merged tables.
- Created a clean refund amount field to handle missing refund values appropriately.
- Calculated gross profit from sales and cost of goods sold.
- Created an order date field for time-based analysis.
- Checked table relationships and validated merges using anti-join checks.
- Checked for duplicate records and reviewed the resulting dataset.

### 3. Load and Analyse

Loaded the transformed data into Excel for further analysis using PivotTables, PivotCharts, and an interactive dashboard.

The analysis covered:

- Sales and gross profit by product.
- Product contribution to total sales.
- Gross profit margin by product.
- Refund amounts and refund-to-sales ratios.
- Net sales after refunds.
- Sales and gross profit trends over time.

## Key Results

| Metric | Result |
|---|---:|
| Total Order Items | 40,025 |
| Total Sales | $1,938,509.75 |
| Total COGS | $722,370.25 |
| Gross Profit | $1,216,139.50 |
| Gross Profit Margin | 62.74% |
| Total Refunds | $85,338.69 |
| Net Sales After Refunds | $1,853,171.06 |
| Overall Refund-to-Sales Ratio | 4.40% |

*These figures represent the validated results from the completed analysis.*

## Key Business Insights

### Product Performance

- **The Original Mr. Fuzzy** generated the highest sales and gross profit, contributing approximately 62.47% of total sales.
- **The Birthday Sugar Panda** recorded the highest gross profit margin at approximately 68.49%.
- The results show that the product generating the highest revenue is not necessarily the product with the highest profit margin.

### Refund Analysis

- The Original Mr. Fuzzy recorded the highest refund amount at $61,837.63.
- The Birthday Sugar Panda had the highest refund-to-sales ratio at approximately 6.04%.
- The overall refund-to-sales ratio was approximately 4.40%.

These findings help distinguish products with strong sales performance from those that may warrant closer review of refund patterns.

### Time-Based Analysis

Sales and gross profit were analysed across years and months to identify changes in business performance over time.

The analysis showed that 2014 recorded the highest annual sales and gross profit within the dataset.

## Dashboard

The completed Excel dashboard includes:

- KPI cards for key financial metrics.
- Product contribution to total sales.
- Sales versus gross profit by product.
- Gross profit margin by product.
- Monthly sales and gross profit trends.
- A product slicer connected to the dashboard charts.

The slicer allows users to explore product-level performance interactively.

**Note:** The Gross Profit Margin and Net Sales After Refunds KPI cards display overall totals and do not dynamically recalculate for individual product selections. Product-specific values should be read from the relevant analysis tables.

## Repository Structure

```text
Week 3 - Toy Store E-Commerce ETL/
│
├── Source Data/
│   ├── Original CSV files
│   └── Data dictionary
│
├── Excel Analysis/
│   └── Toy_Store_ETL_Workflow.xlsx
│
├── Documentation/
│   ├── Overall project documentation
│   └── Daily documentation (Days 15–21)
│
├── Deliverables/
│   └── Dashboard screenshot and presentation outputs
│
└── README.md
```

## Project Learning Outcomes

Through this project, I strengthened my practical understanding of:

- Designing a refreshable ETL workflow in Power Query.
- Combining related datasets while validating joins.
- Handling missing values and maintaining appropriate data types.
- Calculating business performance metrics.
- Building interactive Excel dashboards.
- Translating analytical results into business insights.
- Documenting analytical work for reproducibility and portfolio development.

## Conclusion

This project demonstrates an end-to-end Excel-based data preparation and analysis workflow, from importing raw e-commerce data to producing validated metrics and an interactive dashboard.

It forms **Week 3 of my 92-Day Data Analysis Challenge**, documenting my continued development in data analytics through practical, project-based learning.

**Project Focus:** ETL | Data Cleaning | Data Transformation | Data Validation | Excel | Power Query | Business Intelligence