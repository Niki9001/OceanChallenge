
# Re-importing the necessary libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

# Re-loading the data
file_path = 'occ by year.csv'
data = pd.read_csv(file_path)
data_cleaned = data.drop(columns=['Unnamed: 0'])
yearly_counts = data_cleaned.groupby(['year', 'scientificName']).size().unstack(fill_value=0)
species_data = yearly_counts['Gadus morhua']

# The ARIMA model requires a stationary time series. We first check for stationarity.
# Using Augmented Dickey-Fuller test to check stationarity
adf_test = sm.tsa.stattools.adfuller(species_data)

# Creating a function to interpret the results of the ADF test
def interpret_adf_test(adf_test):
    p_value = adf_test[1]
    if p_value < 0.05:
        return "Stationary (Reject the null hypothesis)"
    else:
        return "Non-Stationary (Fail to reject the null hypothesis)"

stationarity_result = interpret_adf_test(adf_test)

# Differencing the data if it's non-stationary
differenced_data = species_data.diff().dropna() if "Non-Stationary" in stationarity_result else species_data

# Displaying the stationarity test result and the first few rows of the (possibly differenced) data
print(stationarity_result, differenced_data.head())
# Re-importing matplotlib for plotting
import matplotlib.pyplot as plt

# Plotting ACF and PACF plots for the differenced data to help choose ARIMA parameters
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
sm.graphics.tsa.plot_acf(differenced_data, lags=20, ax=ax1)
sm.graphics.tsa.plot_pacf(differenced_data, lags=20, ax=ax2)
#plt.show()
####################################
# Trying the ARIMA(2,1,2) model based on the ACF and PACF plots

# Fitting the ARIMA model with the new parameters
arima_model_new = ARIMA(species_data, order=(2, 1, 2))
arima_result_new = arima_model_new.fit()

# Displaying the summary of the new model
print(arima_result_new.summary())
