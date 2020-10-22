import pandas as pd
import numpy as np

#Reading in the .json file#
df_b = pd.read_json('yelp_academic_dataset_business.json', lines=True)

#Drop useless categories
df_b = df_b[df_b['is_open'] == 1] #Only need the restaurants that are open
drop_columns = ['hours','is_open', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude'] #Dropping these categories cause we dont need it. Could be more.
df_b = df_b.drop(drop_columns, axis=1)

#This sets the output to show only one row. I just wanted to see the different column names.
#pd.set_option("display.max_rows", 1, "display.max_columns", None)

#A dataframe containing ONLY places that have the restaurant category.
restaurants = df_b[df_b['categories'].str.contains('Restaurants', case = False, na = False)]

#This will let you see ALL the restaurant categories(Asian, Mexican, Fast Food, etc.)
#df_explode = restaurants.assign(categories = restaurants.categories.str.split(', ')).explode('categories')
#print(df_explode.categories.value_counts())

#This should return a dataframe containing any and all asian restaurants. Rinse and repeat for all other groups.
asian_restaurants = restaurants[restaurants['categories'].str.contains('Chinese|Japanese|Sushi Bars|Asian Fusion|Indian|Thai|Vietnamese|Korean|Bubble Tea|Ramen|Dim Sum|Taiwanese|Hot Pot|Pan Asian|Szechuan|Malaysian|Indonesian', case=False, na=False)]
