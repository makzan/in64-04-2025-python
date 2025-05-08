# This file reads the dst_restaurant.xml
# using DataFrame

import pandas as pd
import numpy as np

# The main program
if __name__ == "__main__":
    df = pd.read_xml("dst_restaurant.xml")
    target_columns = ["id", "name_cn", "dish_name_zh"]
    
    # Randomly pick one row
    row = df[target_columns].sample(1)
    name = row['name_cn'].values[0]
    dish = row['dish_name_zh'].values[0]
    if dish == None:
        print(f"今晚一於去{name}吃啦！")
    else:
        print(f"今晚一於去{name}吃{dish}菜啦！")

    