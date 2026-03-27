import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the cache and session
cache_session = requests_cache.CachedSession('demo_cache', expire_after_days=30)
retry_session = retry(cache_session, retries=5)

# Make the request
openmeteo = openmeteo_requests.Client(session=retry_session)

# Set location
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation"],
    "timezone": "Asia/Jakarta"
}

# The user's previous code:
# responses = openmeteo.weather_forecast(params=params)

responses = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=params)

# Process results
if responses:
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m ASL")
    print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")
    
    # Process Hourly data
    if response.Hourly():
        hourly = response.Hourly()
        data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            )
        }
        
        # The variables are in a list
        for i in range(hourly.VariablesLength()):
            var = hourly.Variables(i)
            # Find the variable name from params or use SDK metadata
            # For simplicity, just adding them as variable_{i}
            data[f"variable_{i}"] = var.ValuesAsNumpy()
            
        hourly_df = pd.DataFrame(data)
        print("\nHourly Forecast:")
        print(hourly_df.head())

    # Process Daily data
    if response.Daily():
        daily = response.Daily()
        data = {
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s"),
                end=pd.to_datetime(daily.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            )
        }
        for i in range(daily.VariablesLength()):
            var = daily.Variables(i)
            data[f"variable_{i}"] = var.ValuesAsNumpy()
            
        daily_df = pd.DataFrame(data)
        print("\nDaily Forecast:")
        print(daily_df.head())