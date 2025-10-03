from load import load_wind_data
from statistics import calc_stats, resample_monthly, resample_quarterly, resample_annual
from plot import plot_time_series, plot_bar
from armia import arima_forecast
import matplotlib.pyplot as plt

# Config
data_file = 'time_series_60min_singleindex.csv file location'
col = 'ES_wind_onshore_generation_actual'
region = 'Spain'
zoom = '2020-01'

# Load
timestamps, wind = load_wind_data(data_file, col)

# Hourly plot
hours = []
for i in range(len(wind)):
    hours.append(i)
    
stats = calc_stats(wind)
plot_time_series(
    hours, wind,
    region + " Wind (Hourly)",
    "Hour index", "Power (MW)",
    stats
)

# Monthly Plot (in Hours)
subset = []
for i in range(len(timestamps)):
    if timestamps[i].startswith(zoom):
        subset.append((timestamps[i], wind[i]))
        
if len(subset) > 0:
    # Split into two lists
    zoom_vals = []
    for item in subset:
        zoom_vals.append(item[1])
    
    hours2 = []
    for i in range(len(zoom_vals)):
        hours2.append(i)
        
    stats2 = calc_stats(zoom_vals)
    plot_time_series(
        hours2, zoom_vals,
        region + " " + zoom,
        "Hour index", "Power (MW)",
        stats2
    )

# Quarterly and Annual bars
periods, mvals = resample_monthly(timestamps, wind)

# Quarterly
t_q, v_q = resample_quarterly(periods, mvals)
stats_q = calc_stats(v_q)
plot_bar(
    t_q, v_q,
    region + " Quarterly Total", "Quarter", "MWh",
    stats_q
)

# Annual
t_a, v_a = resample_annual(periods, mvals)
stats_a = calc_stats(v_a)
plot_bar(
    t_a, v_a,
    region + " Annual Total", "Year", "MWh",
    stats_a
)

# ARIMA plot
# Split data into training and testing sets
split = int(0.9 * len(mvals))
train = []
for i in range(split):
    train.append(mvals[i])
    
test = []
for i in range(split, len(mvals)):
    test.append(mvals[i])

# Split periods similarly
train_p = []
for i in range(split):
    train_p.append(periods[i])
    
test_p = []
for i in range(split, len(periods)):
    test_p.append(periods[i])

# Get forecast
forecast = arima_forecast(train, steps=len(test))
stats_f = calc_stats(forecast)

# Create figure for plot
plt.figure(figsize=(10,6))

# Plot training data
plt.plot(train_p, train, label="Train")

# Plot test data
plt.plot(test_p, test, label="Test")

# Plot prediction
plt.plot(test_p, forecast, "--", label="Prediction")

# Add title and labels
plt.title(region + " Monthly Forecast (ARIMA)")
plt.xlabel("Months")
plt.ylabel("MWh")

# Create x-axis ticks
ticks = []
for i in range(0, split + len(test), 10):
    ticks.append(i)
    
# Create labels for ticks
labels = []
for i in ticks:
    labels.append(str(i) + " ")

# rotate the ticks
plt.xticks(ticks, labels, rotation=90)

# Add statistics
stats_text = "Mean=" + str(round(stats_f[0], 1))
stats_text += "\nStd=" + str(round(stats_f[1], 1))
stats_text += "\nSkew=" + str(round(stats_f[2], 1))

# text position
plt.text(0.95, 0.05, stats_text, 
         horizontalalignment='right', 
         verticalalignment='bottom', 
         transform=plt.gca().transAxes)

# Add legend and fix layout
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
