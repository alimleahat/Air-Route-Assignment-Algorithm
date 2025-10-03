from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(train, steps):
    model = ARIMA(train, order=(5,3,1)).fit()
    return model.forecast(steps=steps)