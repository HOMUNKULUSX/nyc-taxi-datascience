import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as sql
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
plt.title("DISTANCE DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/trip_distance_distribution.png"
    )
    plt.close()


# How long do the trips usually take?
df["duration_min"] = (
     df["trip_duration"].dt.total_seconds() / 60
)

df["duration_min"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TIME_DURATION DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/time_distribution.png"
    )
    plt.close()

# What is the cost of the most trips?
df["fare_amount"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("FARE AMOUNT DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/fare_amount_distribution.png"
    )
    plt.close()

# Do people usually tip, and how much do they tip?
df["tip_amount"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TIP DISTRIBUTION")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/tip_distribution.png"
    )
    plt.close()

# Looking for any relation or better say correlation between tip, amount, duration, passenger count
corr = df[["tip_amount", "fare_amount", "trip_duration", "passenger_count", "average_speed"]].corr()

plt.figure(figsize=(12, 12))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='0.2f'
)

plt.title("RELATION OF MAIN FEATURES")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/heatmap_relation.png"
    )
    plt.close()

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
    plt.close()

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
    plt.close()

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
    plt.close()

# How much money we made for every hours?
hor = df.groupby("pickup_hour")["total_amount"].sum()
hor.plot(kind="line", figsize=(12, 12))

plt.title("HOW MUCH MONEY MADE IN EACH HOUR")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/moneyforhour.png"
    )
    plt.close()

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
    plt.close()

# How much money made it in each day?
dayo = df.groupby("pickup_day")["total_amount"].sum()
dayo.plot(kind='line', figsize=(12, 12))

plt.plot("HOW MUCH MONEY MADE IT IN EACH DAY")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/moneymadeitindays.png"
    )
    plt.close()


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
    plt.close()

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
    plt.close()



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
        "figures/sum_of_totalamount.png"
    )
    plt.close()


TopDOL = df.groupby("Zone_y")["total_amount"].sum()
TopDOL.plot(kind='bar', figsize=(12, 12))

# Attention that is not about most expensive areas beacuse some of them just happen much more than others
plt.title("The sum of total cost for each DOLocation")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/sum_of_totalamount2.png"
    )
    plt.close()


# Now to compare the cost of zones and number of zones:

top_zones_x = df["Zone_x"].value_counts().head(10).index

data = df[df["Zone_x"].isin(top_zones_x)].groupby("Zone_x").agg(
    total_amount=("total_amount", "sum"),
    trip_count=("Zone_x", "size")
).loc[top_zones_x]

fig, ax1 = plt.subplots()

ax1.plot(data.index, data["total_amount"], color="blue", marker="o", label="Total amount")

ax2 = ax1.twinx()
ax2.plot(data.index, data["trip_count"], color="red", marker="o", label="Counter")

plt.xticks(rotation=90)

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.title("compare the size and cost of PULocation")

plt.tight_layout()


if show:
    plt.show()
else:
    plt.savefig(
        "figures/compare_sizeandtotalamount_for_PUL.png"
    )
    plt.close()


# same thing on DOLucation:

top_zones_y = df["Zone_y"].value_counts().head(10).index

data = df[df["Zone_y"].isin(top_zones_y)].groupby("Zone_y").agg(
    total_amount=("total_amount", "sum"),
    trip_count=("Zone_y", "size")
).loc[top_zones_y]

fig, ax3 = plt.subplots()

ax3.plot(data.index, data["total_amount"], color="blue", marker="o", label="Total amount")

ax4 = ax3.twinx()
ax4.plot(data.index, data["trip_count"], color="red", marker="o", label="Counter")

plt.xticks(rotation=45)

ax3.legend(loc="upper left")
ax4.legend(loc="upper right")

plt.title("compare the size and cost of PULocation")

plt.tight_layout()


if show:
    plt.show()
else:
    plt.savefig(
        "figures/compare_sizeandtotalamount_for_DOL.png"
    )
    plt.close()




# what the payment type of thoese who do not tip?

conn = sql.connect('df.db')

df.to_sql(
    'df',
    conn,
    if_exists='replace',
    index=False
)

q = """
SELECT
    "payment_type",
    COUNT (*) AS COUNTER
FROM df
WHERE "tip_amount" == 0
GROUP BY "payment_type" 
"""

result = pd.read_sql_query(q, conn)

result.plot(
    y='COUNTER',
    kind='bar',
    figsize=(12, 12)
)
plt.title("These who don't tip, how they pay?")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/paytypeandtip.png"
    )
    plt.close()

# How much each payment types earn?
r = df.groupby("payment_type")["total_amount"].sum()
r.plot(kind='bar', figsize=(12, 12))

plt.title("total earn of each payment types")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/paymenttype_amount.png"
    )
    plt.close()


respo = df.groupby("pickup_hour").agg(
    total_amount=("total_amount", "sum"),
    count=("total_amount", "size")

)

fig, ax5 = plt.subplots()

ax5.plot(respo.index, respo['total_amount'], color='blue', marker='o', label='total amount')
ax6 = ax5.twinx()

ax6.plot(respo.index, respo['count'], color='red', marker='o', label='counter')

ax5.legend(loc="upper right")
ax6.legend(loc="upper left")

plt.title("Compare the size and the cost of each hour")

if show:
    plt.show()
else:
    plt.savefig(
        "figures/comparization.png"
    )
    plt.close()

