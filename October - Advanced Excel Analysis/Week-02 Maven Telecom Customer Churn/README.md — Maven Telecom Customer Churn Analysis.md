# Maven Telecom Customer Churn Analysis

## Project Overview

This project explores customer churn patterns in a telecommunications company using Microsoft Excel. It is the second dataset project in my **92-Day Data Analysis Challenge**, where I am developing my data analysis skills through practical, hands-on projects.

The analysis focuses on understanding customer behaviour, identifying customer segments associated with higher churn, examining financial indicators, and presenting the findings through an Excel dashboard.

The goal is to turn raw customer data into meaningful insights that can support better customer retention decisions.

## Project Objectives

- Analyse the overall distribution of customer statuses.
- Calculate the overall customer churn rate.
- Investigate churn patterns across tenure groups, age groups, contract types, and payment methods.
- Examine the distribution of churned customers by internet service type.
- Compare financial indicators across customer status groups.
- Build an Excel dashboard to communicate key findings.
- Develop data-driven recommendations to support customer retention.

## Tools and Techniques

**Tool:** Microsoft Excel

**Techniques used:**
- Data preparation and validation
- Excel tables
- Calculated columns and formulas
- PivotTables
- PivotCharts
- Churn rate calculations
- KPI cards
- Dashboard design
- Data visualisation
- Business insights and recommendations

## Dataset Overview

The dataset contains customer demographic information, service subscriptions, tenure, contract arrangements, payment methods, financial measures, customer status, and churn-related information.

The working dataset was organised as an Excel table named `tbl_Churn`.

Key fields used in the analysis included:

- Customer ID
- Gender
- Age
- Tenure in Months
- Contract
- Payment Method
- Internet Type
- Monthly Charge
- Total Charges
- Total Revenue
- Customer Status
- Churn Category
- Churn Reason

## Data Preparation

The dataset was imported into Excel and reviewed before analysis.

The preparation process included checking the data structure, ensuring numerical fields were appropriately represented, and organising the data for analysis.

A tenure grouping field was used to categorise customers into the following groups:

- 0–12 months
- 13–24 months
- 25–48 months
- 49–72 months

A churn flag was also created to support churn rate calculations.

The formula used was:

```excel
=IF(AJ2="Churned",1,0)
```

This formula assigns a value of `1` to churned customers and `0` to customers with other statuses. The average of this flag can be used in a PivotTable to calculate the proportion of customers who churned.

## Key Performance Indicators

The analysis identified the following headline figures:

| KPI | Result |
|---|---:|
| Total Customers | 7,043 |
| Churned Customers | 1,869 |
| Customers Who Stayed | 4,720 |
| Customers Who Joined | 454 |
| Overall Churn Rate | 26.54% |
| Total Revenue | $21.37 million |

The overall churn rate was calculated as:

**Churn Rate = Churned Customers ÷ Total Customers × 100**

## Analysis and Key Findings

### 1. Customer Status Distribution

The dataset contained 7,043 customers, of whom 1,869 were classified as churned.

The overall churn rate was approximately 26.54%, indicating that customer retention is an important area for further investigation.

### 2. Churn by Tenure Group

The first 12 months of tenure accounted for the largest number of churned customers, with 1,037 churned customers in this group.

The 49–72-month tenure group recorded 213 churned customers and 2,026 customers who stayed.

These results suggest that the early customer relationship period deserves particular attention when developing retention strategies.

### 3. Churn by Age Group

The 60–80 age group recorded the highest churn rate among the age groups analysed.

| Age Group | Churn Rate |
|---|---:|
| 19–29 | 21.70% |
| 30–39 | 24.41% |
| 40–49 | 23.70% |
| 50–59 | 24.52% |
| 60–80 | 35.41% |

This finding highlights an age group that may warrant further investigation to understand its service needs and reasons for leaving.

### 4. Churn by Payment Method

| Payment Method | Churn Rate |
|---|---:|
| Mailed Check | 36.88% |
| Bank Withdrawal | 34.00% |
| Credit Card | 14.48% |

Customers paying by mailed check recorded the highest churn rate among the payment methods examined, while credit card users recorded the lowest.

Further investigation would be needed to determine whether billing experience, payment convenience, or other customer characteristics help explain these differences.

### 5. Distribution of Churned Customers by Internet Type

The distribution of churned customers across internet service types was:

| Internet Type | Share of Churned Customers |
|---|---:|
| Fiber Optic | 66.13% |
| DSL | 16.43% |
| Cable | 11.40% |
| Blank/Unspecified | 6.04% |

Fiber optic customers represented the largest share of churned customers.

These figures represent the composition of the churned-customer group, not the churn rate for each internet service category.

### 6. Financial Analysis

The financial analysis compared average charges and revenue across customer status groups.

**Average Monthly Charge**

| Customer Status | Average Monthly Charge |
|---|---:|
| Churned | $73.35 |
| Joined | $42.78 |
| Stayed | $61.74 |

Churned customers had a higher average monthly charge than customers who stayed. This observation may justify further investigation into pricing, service experience, and perceived value.

**Average Total Charges**

| Customer Status | Average Total Charges |
|---|---:|
| Churned | $1,531.80 |
| Joined | $79.29 |
| Stayed | $2,788.52 |

**Average Total Revenue**

| Customer Status | Average Total Revenue |
|---|---:|
| Churned | $1,971.35 |
| Joined | $119.56 |
| Stayed | $3,735.68 |

The total revenue recorded across the dataset was approximately $21.37 million.

Total Revenue was defined as:

**Total Revenue = Total Charges − Total Refunds + Total Extra Data Charges + Total Long Distance Charges**

## Excel Dashboard

The final dashboard was developed in the `02 Analysis` worksheet.

It contains five KPI cards:

1. Total Customers
2. Churned Customers
3. Churn Rate
4. Customers Who Stayed
5. Total Revenue

The dashboard also contains six charts:

1. Customer Status Distribution
2. Churn Rate by Contract Type
3. Distribution of Churned Customers by Internet Type
4. Churn Rate by Tenure Group
5. Churn Rate by Age Group
6. Churn Rate by Payment Method

The supporting PivotTables were positioned away from the main dashboard area to create a cleaner presentation.

The dashboard was reviewed for appearance and basic functionality, with emphasis on clear visual communication and ease of interpretation.

## Business Recommendations

Based on the findings, the following recommendations are proposed:

- **Improve early customer retention:** Investigate why many churned customers left within their first 12 months and consider improving onboarding and early customer support.
- **Investigate age-related churn patterns:** Examine the needs, experiences, and feedback of customers aged 60–80.
- **Review payment-related experiences:** Investigate the factors associated with higher churn rates among customers paying by mailed check and bank withdrawal.
- **Examine pricing and perceived value:** Explore whether charges, service usage, and customer satisfaction contribute to the patterns observed among churned customers.
- **Investigate internet service churn further:** Calculate churn rates separately for each internet service type before drawing conclusions about which service category has the greatest churn risk.
- **Monitor customer retention:** Regularly review churn rates, tenure, contract type, payment method, and relevant financial indicators.

These recommendations are based on observed patterns and should be validated through further analysis before implementation.

## Limitations

This project focuses on descriptive analysis using the available dataset.

The relationships identified do not establish causation. For example, a higher churn rate among customers using a particular payment method does not prove that the payment method caused them to leave.

Additionally, the distribution of churned customers by internet type should not be interpreted as the churn rate for each internet service category.

Further investigation into churn reasons, customer feedback, and additional customer characteristics would help strengthen the recommendations.

## Conclusion

The Maven Telecom Customer Churn Analysis demonstrates how Microsoft Excel can be used to prepare data, calculate churn metrics, analyse customer segments, compare financial indicators, and communicate findings through a dashboard.

The project identified notable differences in churn patterns across tenure groups, age groups, and payment methods. It also highlighted areas where further investigation could help the business understand customer retention challenges.

This project represents the second dataset project in my 92-Day Data Analysis Challenge and has strengthened my practical experience in Excel-based data analysis, visualisation, and business interpretation.

## Challenge Progress

- **Challenge:** 92-Day Data Analysis Challenge
- **Project:** Week 2 — Maven Telecom Customer Churn Analysis
- **Primary Tool:** Microsoft Excel
- **Focus Area:** Advanced Excel, customer churn analysis, and dashboard development

---

*This project was completed as part of a practical learning challenge focused on building data analysis skills through real-world datasets.*