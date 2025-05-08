import untangle
import pandas as pd

# data = untangle.parse("dst_restaurant_2025-05.xml")

# restaurants = data.mgto.restaurant

# print(len(restaurants))

# print(restaurants[0])


df = pd.read_xml("dst_restaurant_2025-05.xml")
print(df)
