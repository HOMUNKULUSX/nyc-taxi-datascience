# Exploratory Data Analysis Report

## 1. Introduction

This report presents the Exploratory Data Analysis (EDA) performed on the taxi trip dataset used in this project. The purpose of the analysis was to understand the structure and behavior of the data, identify meaningful patterns and relationships, examine unusual values, and determine which features may be useful for the later machine-learning stage.

The analysis focused on trip distance, fare, duration, payment method, tips, passenger count, time, and pickup/drop-off locations. All monetary values in this report are expressed in **US dollars (USD)**.

The dataset contains 200 recorded trips. Because this is a relatively small sample, the findings should be interpreted as observations about this dataset rather than general conclusions about all taxi trips in New York City.

---

## 2. Trip Distance

### Question
What is the distribution of trip distances, and what does it tell us about the trips in the dataset?

### Findings

`trip_distance` represents the recorded distance of each taxi trip.

- No null values were found.
- Data type: `float64`
- Minimum: 0.16
- Maximum: 22
- Mean: 3.72
- Number of distinct values: 145 out of 200 records.

The `trip_distance_distribution` histogram shows that most recorded trips have relatively short distances. The largest concentration is between approximately 0.16 and 3 miles, with more than 120 observations in this range. The frequency then drops substantially for longer trips.

This suggests that the dataset is dominated by relatively short, urban taxi journeys.

---

## 3. Fare Amount

### Question
How much do passengers typically pay for a taxi trip, excluding optional tips?

### Findings

`fare_amount` represents the fare paid for the trip before considering the tip.

- No null values were found.
- Data type: `float64`
- Number of distinct values: 60
- Minimum: $3
- Maximum: $120
- Mean: $15.40

The `fare_amount_distribution` histogram shows that fares between approximately $3 and $16 account for the majority of observations, with around 140 records in this range.

There are no recorded trips with fares between approximately $75 and $109, while a small number of trips have fares between $110 and $120. This distribution is consistent with the earlier observation that most trips in the dataset are relatively short and inexpensive.

---

## 4. Trip Duration

### Question
How long do the recorded taxi trips usually take?

### Findings

A new feature named `trip_duration` was created by subtracting the pickup datetime from the drop-off datetime.

- No null values were found.
- Data type: `timedelta64`
- Number of distinct values: 189
- Minimum: 1 minute 32 seconds
- Maximum: 1 hour 42 minutes 16 seconds
- Mean: 16 minutes 32 seconds

The `time_distribution` histogram shows that the largest concentration of trips lasts less than approximately 15 minutes, with around 100 observations. Trips lasting up to 20 minutes are also common, while longer trips become progressively less frequent.

There are no recorded trips in approximately the 80–90 minute range, although a few trips last more than 90 minutes.

Overall, the dataset is characterized mainly by short trips with relatively low fares and durations commonly around 20 minutes or less.

---

## 5. Trips by Day of the Week

### Question
Does the number of recorded taxi trips vary substantially across the days of the week?

### Findings

The weekday distribution shows relatively similar activity on most days. Approximately 30–35 trips are recorded on each of the main weekdays, while the two weekend days contain considerably fewer observations, approximately 15–20 each.

This indicates a noticeable reduction in recorded trips during the weekend within this sample.

---

## 6. Payment Methods and Tipping

### Questions

- Which payment methods are represented in the dataset?
- Does payment method appear to be associated with tipping behavior?

### Findings

The `paymenttype_amount` and `paytypeandtip` visualizations show two payment methods in the dataset:

- Cash
- Credit card

Credit card payments are substantially more common than cash payments. The total value of trips paid by credit card is approximately $3,000, while the corresponding total for cash payments is roughly one third of that amount.

The analysis also shows that most recorded trips contain no tip. Among trips without a tip, almost all were paid for by credit card.

These observations do not establish that payment method causes changes in tipping behavior. The dataset is small, and other factors may influence tipping. They do, however, provide useful relationships for further investigation.

---

## 7. Tip and Trip Cost

### Question
Is there a relationship between the amount paid for a trip and the tip received by the driver?

### Findings

The `scatter_tipandamount` and `scatter_tippercentage` visualizations were used to investigate the relationship between trip cost and tipping.

At first glance, the plots may suggest some positive association between trip cost and tip amount. However, a large number of trips have zero tips across different trip costs, distances, and durations.

Because of this large concentration of zero-tip observations, the available data does not provide enough evidence to conclude that increasing trip cost consistently causes either higher or lower tip amounts.

The `tip_percentage` analysis also does not provide sufficient evidence for a clear relationship between trip cost and the proportion of the fare represented by the tip.

---

## 8. Trip Distance and Cost

### Question
Does trip distance have a relationship with the total cost of a trip?

### Findings

The `amount_and_distance` visualization shows a clear positive relationship between trip distance and total trip cost.

As trip distance increases, the total amount generally increases as well. This is consistent with the expected structure of taxi fares and indicates that distance is an important factor associated with trip cost.

This relationship is relevant to the later machine-learning stage. However, because the project's prediction scenario is **before the trip begins**, the actual distance traveled will not be used as an input feature.

---

## 9. Passenger Count and Cost

### Question
Does the number of passengers appear to affect the total cost of a trip?

### Findings

The `amount_and_passengers` visualization does not show a clear relationship between passenger count and total trip cost.

Most trips in the dataset contain one passenger. Passenger count therefore appears to have limited explanatory value for the observed trip costs in this sample.

---

## 10. Correlation Analysis

### Question
How are several numerical features related to one another?

### Findings

The `heatmap_relation` visualizations were used to examine relationships among passenger count, tip amount, total trip cost, average speed, and trip duration.

The heatmap largely supports observations made in the individual analyses. Passenger count and tip amount do not show strong relationships with the other examined numerical features, while trip duration shows a relationship with trip cost.

The correlation analysis was primarily used as supporting evidence rather than as the sole basis for conclusions.

---

## 11. Revenue by Hour

### Question
During which hours of the day is the highest total recorded trip revenue observed?

### Findings

The `moneyforhour` visualization shows noticeable changes in total recorded trip revenue throughout the day.

The period from approximately 10:00 to 12:00 has the highest recorded total revenue, reaching roughly $400 in the dataset. Revenue then decreases to approximately $150 around 14:00 before increasing again between approximately 14:30 and 16:00, reaching around $350.

The dataset contains trips across all 24 hours of the day. Several periods of increasing revenue appear around typical working hours, although the small sample size means these patterns should not be generalized to all New York taxi activity.

---

## 12. Revenue by Day of the Week

### Question
How does total recorded revenue change across the days of the week?

### Findings

The `moneymadeitindays` visualization shows changes in total revenue across the week.

Revenue increases from Sunday into Monday, with Monday producing the highest recorded total revenue in the sample. Revenue then decreases on Tuesday, increases again on Wednesday, and falls sharply on Thursday.

These changes are partly influenced by the number of trips recorded on each day. Therefore, total revenue alone should not be interpreted as evidence that individual trips were more expensive on a particular day.

---

## 13. Revenue Versus Number of Trips by Hour

### Question
Does a period with high total revenue necessarily contain the most expensive trips?

### Findings

The `comparization` visualization compares total revenue with the number of trips in different time periods.

The 10:00–12:00 period records approximately $400 in total revenue and contains around 13 trips. This makes it the highest-revenue period in the sample, but not necessarily the period with the most expensive individual trips.

Two periods stand out when considering revenue relative to the number of trips:

- Around 16:00, approximately $350 is generated by around 11 trips.
- Around midnight, approximately $220 is generated by only around 7 trips.

By comparison, around 20:00, approximately $250 is generated by around 18 trips.

This demonstrates why total revenue should be interpreted together with trip count when comparing different time periods.

---

## 14. Pickup and Drop-off Locations

### Question
Which locations generate the highest total recorded trip amounts?

### Findings

The `sum_of_totalamount` and `sum_of_totalamount2` bar charts were used to compare total recorded trip amounts associated with pickup and drop-off locations.

For pickup locations, **JFK Airport** is the highest-revenue location in the dataset, with more than $500 in recorded total trip amounts. **LaGuardia Airport** follows with less than $300.

For drop-off locations, **LaGuardia Airport** is also among the highest, with approximately $300 in recorded total trip amounts. **JFK Airport** is another major destination, with approximately $170.

However, total revenue alone cannot identify the locations with the most expensive individual trips. A location may have a high total simply because it occurs frequently.

---

## 15. Location Revenue Versus Trip Frequency

### Question
Are high-revenue locations actually associated with more expensive trips, or do they simply contain more trips?

### Findings

The `campare_sizeandtotalamount_for_DOL` and `compare_sizeandtotalamount_for_PUL` visualizations compare the number of trips with the total amount associated with the corresponding locations.

For pickup locations, JFK Airport records more than $500 across approximately 8 trips. This makes it a particularly high-value pickup location in this sample.

For drop-off locations, Union Sq is notable because approximately $105 in total revenue is associated with only around 5 trips.

These comparisons demonstrate the importance of considering both **trip frequency** and **total revenue** when interpreting location-based revenue.

---

## 16. Overall EDA Conclusions

The exploratory analysis produced several important observations about the dataset:

1. Most recorded trips are relatively short, with a large concentration of distances below approximately 3 miles.
2. Most fares are relatively low, with the majority concentrated between approximately $3 and $16.
3. Trip durations are also generally short, with many trips lasting less than 20 minutes.
4. Credit card payments are substantially more common than cash payments.
5. Zero-tip trips are very common, and the available data does not provide sufficient evidence for a clear relationship between trip cost and tipping.
6. Trip distance has a clear positive relationship with total trip cost.
7. Passenger count does not show a clear relationship with total trip cost in this sample.
8. Revenue varies considerably across hours and days, but total revenue must be interpreted alongside the number of trips.
9. Airport locations, particularly JFK Airport and LaGuardia Airport, account for substantial recorded revenue in the sample.
10. Comparing total revenue with trip frequency provides a more informative view of location-based revenue than total revenue alone.

Overall, the EDA provides a clearer understanding of the dataset and helps identify features that may be useful for the next stage of the project.

---

## 17. Transition to Machine Learning

The next stage of the project will focus on supervised machine learning.

The goal is to predict two outcomes **before a taxi trip begins**:

- **Trip duration**
- **Total trip cost**

The model will use information available at the beginning of the trip, including:

- Pickup location
- Drop-off location
- Pickup hour
- Day of the week

Variables that become known only after the trip has taken place, such as actual trip distance, trip duration, tip amount, and final cost, will not be used as input features for the pre-trip prediction models. This prevents data leakage and ensures that the prediction scenario reflects a realistic pre-trip use case.
