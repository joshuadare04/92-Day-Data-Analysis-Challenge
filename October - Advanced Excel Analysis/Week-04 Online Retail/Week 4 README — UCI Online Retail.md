# Week 4: UCI Online Retail — Data Quality Investigation and Preparation

## Project Overview

As part of my 92-Day Data Analysis Challenge, Week 4 focused on investigating, cleaning and preparing the UCI Online Retail dataset.

The dataset contains 541,909 transaction records, making it significantly larger than the datasets explored in the earlier weeks. I initially worked with Microsoft Excel but introduced Python and Pandas to handle more demanding operations efficiently.

Rather than automatically deleting records that appeared unusual, I investigated the underlying issues, evaluated the available evidence and documented the decisions made during preparation.

## Project Objectives

The main objectives were to:

* Assess the overall quality and structure of the dataset.
* Investigate missing values and unusual numerical entries.
* Examine exact duplicates and repeated invoice-product combinations.
* Understand cancellation records and zero-priced transactions.
* Investigate negative quantities, negative prices and statistical outliers.
* Apply appropriate data preparation decisions.
* Produce and validate a prepared dataset for subsequent analysis.

## Dataset Description

The UCI Online Retail dataset contains transaction records from a UK-based online retail business.

| Attribute        | Details                           |
| ---------------- | --------------------------------- |
| Total records    | 541,909                           |
| Original columns | 8                                 |
| Date coverage    | 1 December 2010 – 9 December 2011 |
| Currency         | British Pounds (£)                |
| Data format      | Excel / CSV                       |

### Original Columns

* `InvoiceNo` – Transaction invoice number.
* `StockCode` – Product or item identifier.
* `Description` – Product description.
* `Quantity` – Quantity recorded per invoice line.
* `InvoiceDate` – Transaction date and time.
* `UnitPrice` – Unit price in pounds sterling.
* `CustomerID` – Customer identifier.
* `Country` – Country associated with the transaction.

## Tools and Technologies

* Microsoft Excel
* Python
* Pandas
* NumPy
* JupyterLab

## Key Investigations

The project involved investigating several data quality issues, including:

* **Missing values:** 135,080 records had missing CustomerIDs, while 1,454 had missing descriptions.
* **Zero-priced transactions:** 2,515 records had a UnitPrice of zero.
* **Negative quantities:** 10,624 records had negative quantities, including cancellation entries and possible operational adjustments.
* **Negative prices:** Two negative UnitPrice records were identified alongside a related positive accounting entry.
* **Exact duplicates:** 5,268 additional duplicate occurrences were identified.
* **Repeated invoice-product combinations:** 9,694 combinations appeared more than once.
* **Outliers:** Quantity, UnitPrice and TransactionValue were investigated using the Interquartile Range (IQR) method.

These findings were investigated before preparation decisions were made.

## Data Preparation

The preparation process was implemented using Python and Pandas on a separate copy of the original dataset.

Key activities included:

1. Creating a calculated `TransactionValue` column using Quantity multiplied by UnitPrice.
2. Recovering 1,033 missing descriptions using a controlled StockCode-to-Description mapping based on a single distinct description available elsewhere in the dataset.
3. Flagging exact duplicates and additional duplicate occurrences.
4. Classifying cancellation records and negative-quantity, zero-price adjustments.
5. Identifying bad-debt adjustments, negative prices and zero prices.
6. Creating outlier flags for Quantity, UnitPrice and TransactionValue.

Records were retained rather than automatically deleted or modified simply because they appeared unusual.

## Final Dataset

The prepared dataset contains:

| Attribute                                      |  Result |
| ---------------------------------------------- | ------: |
| Original records                               | 541,909 |
| Prepared records                               | 541,909 |
| Original columns retained                      |       8 |
| Final columns                                  |      20 |
| Descriptions recovered                         |   1,033 |
| Descriptions still missing                     |     421 |
| Additional exact duplicate occurrences flagged |   5,268 |

The prepared dataset was exported as `Online_Retail_Prepared.csv` and successfully re-imported into Python for validation.

## Project Structure

```text
Week-04 Online Retail/
│
├── Source Data/
│
├── Excel Analysis/
│   └── Excel Analysis
│
├── Python Analysis/
│   ├── Day_29_Exact_Duplicate_Analysis.ipynb
│   ├── Day_30_Duplicate_Invoice_Line_Analysis.ipynb
│   ├── Day_31_Data_Preparation_Decisions.ipynb
│   └── Day_31_Data_Preparation_Implementation.ipynb
│
├── Documentation/
│   ├── Daily Documentation/
│   │   └── Day 22–31 Documentation
│   │
│   └── Week_4_UCI_Online_Retail_Data_Preparation_Report.docx
│
├── Deliverables/
│   └── Online_Retail_Prepared.csv
│
├── .gitignore
└── README.md
```

The Python Analysis folder contains the investigation and implementation notebooks. Documentation contains the individual daily progress records and the consolidated project report.

The `.gitignore` file excludes Jupyter checkpoint folders and other unnecessary generated or local files from Git tracking.

## Key Learning Outcomes

This project reinforced the importance of investigating data before making preparation decisions.

It also provided practical experience in handling large datasets with Python, using Pandas for data inspection and transformation, validating calculated fields, and documenting data quality decisions.

One major takeaway was that unusual data does not automatically mean incorrect data. Understanding the context behind a record is an essential part of responsible data preparation.

## Next Phase

The prepared UCI Online Retail dataset will be carried into the November phase of the 92-Day Data Analysis Challenge, where Microsoft Power BI will be used for further business analysis and dashboard development.

---

**92-Day Data Analysis Challenge | Week 4**

**FIGURING IT OUT IS A SKILL TOO.**
