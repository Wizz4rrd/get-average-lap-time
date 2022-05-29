import pandas as pd

df = pd.read_csv("lap_times.csv")

# force the column's data into timestamp variables
df["lap time"] = pd.to_datetime(df["lap time"], infer_datetime_format=True)

#  get the average (mean) and median of the 'lap time' column
df_mean = df["lap time"].mean()
df_median = df["lap time"].median()


print(
    f"""

mean (average) lap time = {df_mean}
median lap time = {df_median}

"""
)
