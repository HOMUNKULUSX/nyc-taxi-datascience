import pandas as pd
import matplotlib.pyplot as plt
from checking import df



#df = pd.read_csv("data/taxi.csv")

show = True

# What the range of the most trips?
# Is certain a mount repeated too much?

df["trip_distance"].plot(kind='hist', bins=10, figsize=(12, 12))
plt.title("TRIP DISTRIBUTION")

if show:
    plt.show()
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
plt.savefig(
    "figures/time_distribution.png"
)






