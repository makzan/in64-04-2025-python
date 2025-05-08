import untangle

# Fetch the XML data from the URL
url = "https://xml.smg.gov.mo/c_7daysforecast.xml"
xml_data = untangle.parse(url)

# Extract and format the weather forecast
forecasts = xml_data.SevenDaysForecast.Custom.WeatherForecast
for forecast in forecasts:
    date = forecast.ValidFor.cdata
    low_temp = forecast.Temperature[1].Value.cdata
    high_temp = forecast.Temperature[0].Value.cdata
    weather_status = forecast.WeatherStatus.cdata
    weather_description = forecast.WeatherDescription.cdata

    # Format and print the output
    print(f"{date} {low_temp}–{high_temp}C 間晴 {weather_description}")