# https://xml.smg.gov.mo/c_actual_brief.xml
# Use untangle to parse the xml
# And get back the current temperature value

import untangle

url = "https://xml.smg.gov.mo/c_actual_brief.xml"
data = untangle.parse(url)

# Get the first Temperature value
Temperature = data.ActualWeatherBrief.Custom.Temperature

# Check if Temperature is list or Element
if type(Temperature) == list:
    temp = Temperature[0].Value.cdata
else:
    temp = Temperature.Value.cdata


print(f"当前温度是{temp}°C")

