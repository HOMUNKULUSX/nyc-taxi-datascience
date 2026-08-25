import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from checking import df



#df = pd.read_csv("data/taxi.csv")

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

# There is any relation between the cost of trip and tip?
corr = df[["tip_amount", "fare_amount"]].corr()

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






