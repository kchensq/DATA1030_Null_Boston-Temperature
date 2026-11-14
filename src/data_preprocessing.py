import pandas as pd

weather = (
    pd.read_csv("boston_weather_raw.csv", parse_dates=["time"])
    .set_index("time")
    .sort_index()
    .asfreq("D")
)

features = [
    "temperature_2m_mean",
    "precipitation_sum",
    "wind_speed_10m_max",
    "snowfall_sum",
]

def create_lagged_df(weather, n_days):
    df = pd.concat(
        [
            weather[features].shift(lag).add_suffix(f"_lag{lag}")
            for lag in range(1, n_days + 1)
        ],
        axis=1,
    )

    df["temperature_today"] = weather["temperature_2m_mean"]
    return df.dropna()

df_1day = create_lagged_df(weather, 1)
df_3day = create_lagged_df(weather, 3)
df_7day = create_lagged_df(weather, 7)

# Keep the same target dates for all three datasets.
common_dates = df_7day.index
df_1day = df_1day.loc[common_dates].copy()
df_3day = df_3day.loc[common_dates].copy()

df_1day.to_csv("boston_weather_1day.csv", index_label="time")
df_3day.to_csv("boston_weather_3day.csv", index_label="time")
df_7day.to_csv("boston_weather_7day.csv", index_label="time")