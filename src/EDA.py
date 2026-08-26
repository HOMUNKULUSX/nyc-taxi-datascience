import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from checking import df



#df = pd.read_csv("data/taxi.csv")
lookup = pd.read_csv("data/taxi_zone_lookup.csv")

pd.set_option(
    "display.max_columns",
    None
)

show = True

# What the range of the most trips?
# Is certain a mount repeated too much?
df["trip_distance"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TRIP DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/trip_distribution.png"
    )


# How long do the trips usually take?
df["duration_min"] = (
     df["trip_duration"].dt.total_seconds() / 60
)

df["duration_min"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TIME DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/time_distribution.png"
    )

# What is the cost of the most trips?
df["fare_amount"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("FARE AMOUNT DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/fare_amount_distribution.png"
    )

# Do people usually tip, and how much do they tip?
df["tip_amount"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TIP DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/tip_distribution.png"
    )

# Looking for any relation or better say correlation between tip, amount, duration, passenger count
corr = df[["tip_amount", "fare_amount", "trip_duration", "passenger_count", "average_speed"]].corr()

plt.figure(figsize=(12, 12))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='0.2f'
)

plt.title("TIP AND AMOUNT")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/heatmap_tipandamount.png"
    )

# checking this by scatter
sns.scatterplot(
    x="tip_amount",
    y="fare_amount",
    data=df
)

plt.title("TIP AND AMOUNT")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/scatter_tipandamount.png"
    )

# to be more accurate let found out what percentage of total income comes from tips?
df["tip_percentage"] = (
    df["tip_amount"] / df["fare_amount"] * 100
)

sns.scatterplot(
    x="total_amount",
    y="tip_percentage",
    data=df
)

plt.title("TOTAL AMOUNT AND TIP PERCENTAGE")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/scatter_tippercentage.png"
    )

# What part of days most trips happen?
# 24H
df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour

df["pickup_hour"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("HOUR DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/hour_distribution.png"
    )

# Which day of a week most trips happen?
df["pickup_day"] = df["tpep_pickup_datetime"].dt.dayofweek

df["pickup_day"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("DAY DISTRINUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/hour_distribution.png"
    )

# check, the relation between distance and amount
sns.scatterplot(
    x='trip_distance',
    y='fare_amount',
    data=df
)

plt.title("RELATION BETWEEN AMOUNT AND DISTANCE")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/amount_and_distance.png"
    )

# Is there any relation between cost of trip and count of passengers?
sns.scatterplot(
    x='fare_amount',
    y='passenger_count',
    data=df
)

plt.title("RELATION BETWEEN AMOUBT AND NUMBER OF PASSENGERS")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/amount_and_passengers.png"
    )



# Until now we've worked on most features except PULocation and DuLocation or for short
# Location_id, as you know location_id is just a number which point a specific area in New York
# To know what these numbers are really abount,I am going to use taxi_zone_lookup dataset.
    
# PULocation: where the passengers pick up
df = df.merge(
    lookup,
    left_on='PULocationID',
    right_on='LocationID',
    how='left'
)

# DOLocation: where the passengers drop off
df = df.merge(
    lookup,
    left_on='DOLocationID',
    right_on='LocationID',
    how='left'
)

TopPUL = df.groupby("Zone_x")["total_amount"].sum()
TopPUL.plot(kind='bar', figsize=(12, 12))

# Attention that is not about most expensive areas beacuse some of them just happen much more than others
plt.title("The sum of total cost for each PULocation")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/some_of_totalamount.png"
    )


TopDOL = df.groupby("Zone_x")["total_amount"].sum()
TopDOL.plot(kind='bar', figsize=(12, 12))

# Attention that is not about most expensive areas beacuse some of them just happen much more than others
plt.title("The sum of total cost for each DOLocation")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/some_of_totalamount2.png"
    )


