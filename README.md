# Predicting Next-Day Mean Temperature in Boston

A project for **DATA 1030, Fall 2026, Brown University**.

## Team

**Team name:** Null

**Team members:**

- Siqi Chen
- Luehan Wang
- Xinxiong Zhao

## Project Overview

This project predicts the next day's mean temperature in Boston using mean temperature, total precipitation, maximum wind speed, and snowfall from the preceding three days. We investigate whether regression models using these recent local weather variables can predict tomorrow's temperature more accurately than assuming it will equal today's.

We plan to compare **Linear Regression, Ridge Regression, and Random Forest** with a **persistence baseline**, which predicts that tomorrow's mean temperature will equal today's. Performance will be evaluated primarily using **mean absolute error (MAE)**, with **root mean square error (RMSE)** as a supplementary metric.

## Data

Data were collected using a Python script through the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), using ERA5 reanalysis data for Boston from **January 1, 2006, through December 31, 2025**.

The raw dataset contains **7,305 daily records**. Constructing three days of lagged features produces **7,302 samples**, each with **12 features** and a target of daily mean temperature in °C. Data checks found no duplicate dates, calendar gaps, or missing values.

### Data Description

| Column | Description | Unit / Format |
| --- | --- | --- |
| `time` | Date of the daily record | YYYY-MM-DD |
| `temperature_2m_mean` | Daily mean air temperature at 2 m above ground | °C |
| `precipitation_sum` | Total daily precipitation | mm |
| `wind_speed_10m_max` | Daily maximum wind speed at 10 m above ground | km/h |
| `snowfall_sum` | Total daily snowfall | cm |

Data are split chronologically by target date:

| Split | Years | Samples |
| --- | --- | --- |
| Training | 2006–2017 | 4,380 |
| Validation | 2018–2021 | 1,461 |
| Test | 2022–2025 | 1,461 |

Exploratory analysis uses only the training period. See the midterm report for data documentation, exploratory figures, the literature review, and the proposed application and limitations.

## Environment and Setup

We use the **same environment setup as the DATA 1030 course**. The environment and packages were copied from the course setup. See [`environment.yml`](environment.yml) for the specific **Python and package versions**.
