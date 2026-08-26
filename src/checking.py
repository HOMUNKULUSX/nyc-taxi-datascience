import pandas as pd




df = pd.read_csv("data/taxi.csv")


df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

# new features

df["trip_duration"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"])

df["average_speed"] = (
    df["trip_distance"] / (
        df["trip_duration"].dt.total_seconds() / 3600
    )
)



pd.set_option(
    "display.max_columns",
    None
)

with open(
    "report/checkig_data_report.TXT",
    "w",
    encoding="utf-8"
) as file:
    
    file.write(
        "DATA UNDRESTANDING REPORT \n"
    )
    file.write("=" * 50 + "\n\n")

    file.write(
        "Data Shape:\n"
    )
    file.write(str(df.shape))
    file.write("\n\n")

    file.write(
        "Columns Name:\n"
    )
    file.write(str(df.columns.tolist()))
    file.write("\n\n")

    file.write(
        "Data Type:\n"
    )
    file.write(str(df.dtypes))
    file.write("\n\n")

    file.write(
        "Unique Values:\n"
    )
    file.write(str(df.nunique()))
    file.write("\n\n")

    file.write(
        "NULL Values:\n"
    )
    file.write(str(df.isnull().sum()))
    file.write("\n\n")

    file.write(
        "Duplicate Rows:\n"
    )
    file.write(str(df.duplicated().sum()))
    file.write("\n\n")

    file.write(
        "Desciptive Statistics:\n"
    )
    file.write(str(df.describe()))
    file.write("\n\n")


    ## checking if there is unlogical values in the columns or not!

    file.write(
        "Checking the min values of the following columns:\n"
    )
    min_values = df.select_dtypes(include=['int64', 'float64']).min()
    min_check = min_values <= 0

    file.write(str(min_values))
    file.write("\n\n")

    file.write(
        "Minimum Values <= 0\n"
    )
    file.write(str(min_check))
    file.write("\n\n")

    file.write(
        "Data Quality Findings _ report \n"
    )
    file.write(
        """
        PASSENGER COUNT
        ________

        -- 4 records have passenger_count = 0.
        -- These records contain valid information
        -- The records were retained because there is not enough
        evidence to classify them as invalid trips.

        __________________________________________________

        TRIP TIME VALIDATION
        ________________

        No trips were found where the drop-off time
        was before the pickup time.

        ___________________________________________________

        TRIP DISTANCE & DURATION AND AVERAGE SPEED VALIDATION
        _________________________________________

        No negative trip_duration values were found.
        No unrelistic relationship between trip_distance and 
        trip_diration was found.
        No trip with average speed above 100 mph were found.
        The 99th percentile of average speed was 35.06 mph,
        indicating no unusually high speeds in the dataset.
        """
    )



#print(df[df["passenger_count"] == 0].shape)
#print(df[df["passenger_count"] == 0])


invalid_trips = [
    df["tpep_dropoff_datetime"] < df["tpep_pickup_datetime"]
]

#print(invalid_trips)
#print(df[["trip_distance", "trip_duration"]])


#print(df[df["average_speed"] > 100][["trip_distance", "trip_duration", "average_speed"]])

#print(df["average_speed"].quantile([0.01, 0.05, 0.50, 0.95, 0.99]))



