# Aviation Operations Analytics – Turning Flight Data into Business Insights

## Project Overview

This project focuses on analysing U.S. airline flight operations to understand flight punctuality, delays, cancellations, diversions, airline performance, and airport activity.

Using data covering August 2025 to August 2026, I applied Python, Power Query, and Power BI to inspect, clean, transform, analyse, and visualise flight performance data.

The goal was to turn raw flight records into meaningful insights that can support better understanding of airline operations and operational performance.

## Project Objectives

- Analyse flight operations and monthly flight activity.
- Evaluate airline punctuality and delay performance.
- Examine flight cancellations and diversions.
- Identify airports with high departure activity and arrival delays.
- Investigate data quality issues and missing values.
- Build an interactive Power BI dashboard to communicate findings.

## Dataset Overview

The dataset used for this project is the **U.S. Flight Punctuality Dataset** published by TripStow on Hugging Face.

The data is based on the U.S. Department of Transportation's Bureau of Transportation Statistics (BTS) Airline On-Time Performance data.

The project uses 13 monthly CSV files covering **August 2025 to August 2026**.

| Dataset Detail | Description |
|---|---|
| Records | 542,767 |
| Original Columns | 12 |
| Monthly Files | 13 |
| Airlines | 14 |
| Airports | 360 |
| Period Covered | August 2025 – August 2026 |

The original dataset contains 12 columns, including:

- `month`
- `carrier`
- `flight_number`
- `origin`
- `dest`
- `flights`
- `cancelled`
- `diverted`
- `on_time`
- `late_30`
- `arr_delay_mean`
- `arr_delay_median`

Power Query added a `Source.Name` column during the data combination process, bringing the final table to 13 columns.

## Dataset Licence and Attribution

The dataset was obtained from [TripStow's U.S. Flight Punctuality Dataset](https://huggingface.co/datasets/tripstow/us-flight-punctuality) on Hugging Face. It is based on U.S. Department of Transportation, Bureau of Transportation Statistics (BTS), Airline On-Time Performance data and is released under the **CC0 1.0 Universal licence**, which permits free use, modification, and redistribution.

Attribution is not required but is appreciated.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Initial data inspection, profiling, validation, and exploratory analysis |
| Pandas | Data manipulation and analysis |
| Power Query | Data cleaning, transformation, and preparation |
| Power BI | Data modelling, DAX calculations, and dashboard development |
| DAX | Creating measures and performance indicators |
| GitHub | Project documentation and version control |

## Project Workflow

### 1. Python Data Analysis

Python and Pandas were used to perform the initial inspection and investigation of the 13 CSV files.

The analysis covered:

- Dataset structure and column inspection.
- Missing-value analysis.
- Duplicate record checks.
- Data type and consistency checks.
- Investigation of negative arrival delays.
- Examination of unusually high delay values.
- Airline data coverage across the reporting period.
- Final data quality audit.

Some important observations from this stage included:

- The dataset contained 542,767 records.
- No duplicate rows were identified.
- There were 2,422 missing cells, all within the two arrival delay statistic columns.
- Negative arrival delay values were retained because they represent flights arriving earlier than scheduled.
- Unusually high delay values were investigated and retained rather than automatically removed.
- Two airlines had incomplete coverage across the 13-month period.

### 2. Power Query – Data Preparation

The 13 monthly CSV files were imported into Power BI using the Folder connector.

Power Query was used to:

- Combine all monthly files into one table.
- Inspect column quality, distribution, and data profiles.
- Verify data types.
- Apply Trim and Clean transformations to text columns.
- Retain the source filename column for traceability.
- Review missing values and preserve valid analytical information.

The final combined table contained 542,767 records and 13 columns, including `Source.Name`.

### 3. Data Modelling and DAX

A dimensional data model was created to support the analysis.

The model included:

- A central flight data table.
- A Date dimension.
- An Airline dimension.
- An Airport dimension.

Relationships were established between the fact table and dimension tables, including an inactive relationship for destination airports to support arrival-side analysis.

DAX measures were developed to calculate:

- Total scheduled flights.
- Operated flights.
- Cancelled flights.
- Diverted flights.
- On-time flights.
- Delayed flights.
- On-time performance.
- Delayed flight rate.
- Cancellation rate.
- Diversion rate.
- Average arrival delay.
- Airline and airport performance indicators.

## Key Findings

The analysis produced the following results:

| Metric | Result |
|---|---:|
| Total Scheduled Flights | 7,652,247 |
| Operated Flights | 7,512,553 |
| Cancelled Flights | 139,694 |
| Diverted Flights | 22,835 |
| On-Time Flights | 5,787,585 |
| Delayed Flights | 1,105,167 |
| On-Time Performance | 77.04% |
| Delayed Flight Rate | 14.71% |
| Cancellation Rate | 1.83% |
| Diversion Rate | 0.30% |
| Weighted Average Arrival Delay | 8.72 minutes |

**Methodological note:** For this project, operated flights were calculated as scheduled flights minus cancelled flights. Diverted flights remain within this denominator. The resulting 77.04% on-time performance is therefore based on this project-defined denominator and should not be confused with the source dataset's published on-time share calculation, which excludes both cancelled and diverted flights.

### Additional Insights

- A total of 14 airlines were represented in the dataset.
- Airline on-time performance varied, with HA recording the highest observed value of 81.76%.
- HA appeared in only five of the 13 months, so its result should not be interpreted as a complete-period comparison with airlines represented throughout the dataset.
- The analysis covered 360 airports.
- Airport departure activity and arrival delay performance were examined separately.
- The airport arrival delay ranking was restricted to airports with at least 1,000 arrival flights to avoid drawing conclusions from very low-volume airports.
- Missing arrival delay statistics represented a small proportion of the overall flight volume and were retained rather than replaced with zero.

## Dashboard Development

The final Power BI report contains two interactive dashboard pages.

### Page 1: Flight Operations Overview

This page provides a general overview of flight activity and operational performance.

It includes:

- Total scheduled flights.
- Operated flights.
- On-time performance.
- Delayed flight rate.
- Monthly flight operations trend.
- Flight outcome distribution.
- Monthly average arrival delay trend.
- Airline and date slicers.
- A 3D-style aircraft visual with dynamic performance indicators.

The aircraft performance indicators respond to report selections, allowing the displayed operational status and insights to change as the data is filtered.

### Page 2: Airline & Airport Performance

This page focuses on comparing airline reliability and airport activity.

It includes:

- Total number of airlines.
- Total number of airports.
- Best recorded airline on-time performance.
- Top performing airline.
- Top 10 airlines by on-time performance.
- Airline cancellation and diversion counts.
- Top 10 departure airports by flight volume.
- Top 10 airports by average arrival delay.

The report pages are connected through synchronised airline and date slicers, allowing selections made on the first page to update the analysis on the second page.

## Recommendations

Based on the findings, the following areas deserve attention:

1. **Monitor airline punctuality:** Airlines should regularly track on-time performance and investigate patterns associated with poor punctuality.

2. **Investigate recurring delays:** Consistent delays should be examined further to identify possible operational, scheduling, weather-related, or airport-related contributing factors.

3. **Monitor cancellations and diversions:** These indicators should be tracked alongside punctuality to provide a broader view of operational performance.

4. **Investigate airport performance:** Airports with relatively high arrival delays should be examined further, while considering their flight volumes.

5. **Consider data coverage:** Airline comparisons should account for differences in the number of months represented in the dataset.

6. **Improve delay data completeness:** Missing delay statistics should be monitored to improve the completeness of future analysis.

7. **Use multiple performance indicators:** Operational decisions should consider punctuality, delays, cancellations, diversions, and flight volume together rather than relying on a single metric.

These recommendations identify areas for further investigation; the dataset alone does not establish the causes of delays or disruptions.

## Project Structure

```text
Week-07 - Aviation Operations Analytics/
│
├── Source Data/
│   └── 13 monthly CSV files
│
├── Python Analysis/
│   └── Python scripts for profiling,
│       exploration, validation, and analysis
│
├── Power BI Analysis/
│   └── Power BI report (.pbix)
│
└── Documentation/
    ├── Daily documentation
    └── Final project documentation
```

## Conclusion

This project provided an opportunity to work through a complete data analysis workflow, from inspecting and validating raw data to preparing a data model and building an interactive Power BI dashboard.

Beyond the technical skills involved, the project reinforced the importance of understanding the data, validating calculations, making informed decisions about data quality, and communicating findings clearly.

It also provided an opportunity to explore how data analytics can be applied to aviation operations and how operational data can support better performance monitoring and decision-making.

**FIGURING IT OUT IS A SKILL TOO.**