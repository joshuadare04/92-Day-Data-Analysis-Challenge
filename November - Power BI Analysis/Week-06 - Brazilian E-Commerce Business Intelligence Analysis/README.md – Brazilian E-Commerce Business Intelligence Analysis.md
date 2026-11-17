# Brazilian E-Commerce Business Intelligence Analysis

## Project Overview

This project explores the Brazilian E-Commerce Public Dataset by Olist to analyse business performance across sales, customers, products, payments, orders, delivery operations and customer satisfaction.

The project follows an end-to-end data analytics workflow, beginning with data profiling using Python and Pandas, followed by data cleaning and transformation with Power Query, data modelling, DAX development and interactive dashboard creation using Microsoft Power BI.

The final deliverable is a four-page interactive Power BI dashboard designed to provide meaningful insights into different aspects of e-commerce operations.

## Project Objectives

- Examine and understand multiple related e-commerce datasets.
- Identify data-quality issues through initial profiling.
- Clean and transform datasets for analysis.
- Establish relationships between different business entities.
- Develop analytical measures using DAX.
- Analyse sales, customer, product and operational performance.
- Build an interactive multi-page Power BI dashboard.
- Present business information through meaningful visualisations.

## Dataset

**Source:** Brazilian E-Commerce Public Dataset by Olist.

**Platform:** Kaggle.

The project uses nine CSV datasets:

1. `olist_customers_dataset.csv`
2. `olist_geolocation_dataset.csv`
3. `olist_order_items_dataset.csv`
4. `olist_order_payments_dataset.csv`
5. `olist_order_reviews_dataset.csv`
6. `olist_orders_dataset.csv`
7. `olist_products_dataset.csv`
8. `olist_sellers_dataset.csv`
9. `product_category_name_translation.csv`

These datasets contain information about customers, orders, products, sellers, payments, reviews, geographical locations and product categories.

## Tools and Technologies

| Tool | Application |
|---|---|
| Python | Initial data inspection and profiling |
| Pandas | Data manipulation and quality assessment |
| Visual Studio Code | Python development environment |
| Power Query | Data cleaning and transformation |
| DAX | Analytical calculations and measures |
| Power BI Desktop | Data modelling and dashboard development |

## Project Workflow

The project followed these major stages:

### 1. Data Acquisition and Organisation
Downloaded and organised the nine source datasets.

### 2. Data Profiling
Used Python and Pandas to inspect dataset structures, dimensions, data types, missing values and duplicate records.

### 3. Data Cleaning and Transformation
Used Power Query to prepare the datasets for analysis.

### 4. Data Modelling
Established relationships between the relevant tables and created a dedicated DateTable for time-based analysis.

### 5. DAX Development
Created and validated 25 analytical measures to support the different business analysis areas.

### 6. Dashboard Development
Designed and developed four interactive Power BI dashboard pages.

### 7. Testing and Validation
Tested the measures, visual interactions, slicers and cross-page filtering functionality.

## Dashboard Pages

The final Power BI report contains four pages.

### 1. Executive Overview
Provides a high-level summary of business performance.

Key indicators include:
- Total Sales
- Total Orders
- Total Customers
- Average Order Value
- Average Review Score

Visualisations cover monthly sales performance, order status distribution, product category revenue and payment methods.

### 2. Customer Insights
Explores customer distribution, review activity and satisfaction.

Key indicators include:
- Total Reviews
- Positive Review Rate
- Negative Reviews

Visualisations include customer distribution by state, review score distribution and average review score by month.

### 3. Sales and Product Analysis
Examines product-level performance and revenue contribution.

Key indicators include:
- Total Product Revenue
- Total Freight Value
- Total Items Sold
- Unique Products Sold

Visualisations include:
- Top 10 Products by Revenue.
- Revenue by Product Category.
- Top 10 Products by Quantity Sold.

### 4. Order and Delivery Analysis
Focuses on order fulfilment and delivery performance, providing a dedicated view of operational activities.

## Dashboard Interactivity

The report includes synchronised slicers for:

- Year
- Month
- Order Status

These slicers work across all four dashboard pages, allowing users to explore the report using consistent filters.

## Key Technical Highlights

- Nine related CSV datasets.
- Python and Pandas data profiling.
- Power Query data preparation.
- Relational data modelling.
- Dedicated DateTable.
- 25 DAX measures.
- Four-page interactive Power BI report.
- Cross-page slicer synchronisation.

## Repository Structure

```text
Week-06 - Brazilian E-Commerce Business Intelligence Analysis/
│
├── Source Data/
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
│
├── Power BI/
│   └── Brazilian_E-Commerce_Analysis.pbix
│
├── Documentation/
│   ├── Daily Documentation/
│   │   ├── Day 41.docx
│   │   ├── Day 42.docx
│   │   ├── Day 43.docx
│   │   ├── Day 44.docx
│   │   ├── Day 45.docx
│   │   ├── Day 46.docx
│   │   └── Day 47.docx
│   │
│   └── Project Documentation/
│       └── Project Documentation.docx
│
├── Deliverables/
│   └── Dashboard Screenshots/
│
└── README.md
```

*Note: The filenames in the structure are illustrative; retain the actual filenames used in your project.*

## Project Outcome

Successfully developed an interactive four-page Business Intelligence dashboard from nine related e-commerce datasets.

The project demonstrates the application of Python, Pandas, Power Query, DAX and Power BI in an end-to-end analytical workflow.

It also strengthened practical skills in data preparation, modelling, business analysis and interactive data visualisation.

## Author

**Joshua Dare**

Data Analyst | Excel | SQL | Python | Power BI

Part of my 92-Day Data Analysis Challenge.

## Acknowledgements

Dataset provided by Olist through Kaggle.

**Dataset:** Brazilian E-Commerce Public Dataset by Olist.