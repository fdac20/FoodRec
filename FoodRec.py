import pandas as pd
import numpy as np

#Reading in the .json file#
df_b = pd.read_json('yelp_academic_dataset_business.json', lines=True)

#Drop useless categories

drop_columns = ['hours','is_open', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude'] #Dropping these categories cause we dont need it. Could be more.
df_b = df_b.drop(drop_columns, axis=1)

#This sets the output to show EVERYTHING. If you only want to see one row, set the first 'None' to 1. I just wanted to see the different column names.
pd.set_option("display.max_rows", None , "display.max_columns", None)

#A dataframe containing ONLY places that have the restaurant category.
restaurants = df_b[df_b['categories'].str.contains('Restaurants', case = False, na = False)]

#This will let you see ALL the restaurant categories(Asian, Mexican, Fast Food, etc.)
df_explode = restaurants.assign(categories = restaurants.categories.str.split(', ')).explode('categories')
print(df_explode.categories.value_counts())


#This should return a dataframe containing any and all asian restaurants. Rinse and repeat for all other groups.
#template name = restaurants[restaurants['categories'].str.contains('',case=False,na=False)]
asian = restaurants[restaurants['categories'].str.contains('Chinese|Japanese|Sushi Bars|Asian Fusion|Indian|Thai|Vietnamese|Korean|Bubble Tea|Ramen|Dim Sum|Taiwanese|Hot Pot|Pan Asian|Szechuan|Malaysian|Indonesian|Poke', case=False, na=False)]
american = restaurants[restaurants['categories'].str.contains('American|Burgers|Breakfast|Chicken Wings|Barbeque|Steakhouses|Diners|Hot Dogs|Fast Food|Sandwiches|Cheesesteaks',case=False,na=False)]
italian = restaurants[restaurants['categories'].str.contains('Pizza|Italian',case=False,na=False)]
bars = restaurants[restaurants['categories'].str.contains('Nightlife|Bars|Sports Bars|Pubs|Beer|Wine Bars|Juice Bars|Beer Bar|Hookah Bars|Cocktail Bars',case=False,na=False)]
fast_food = restaurants[restaurants['categories'].str.contains('Fast Food',case=False,na=False)]
diners = restaurants[restaurants['categories'].str.contains('Diners',case=False,na=False)]
dessert = restaurants[restaurants['categories'].str.contains('Bakeries|Desserts|Ice Cream|Donuts|Creperies|Patisserie|Waffles',case=False,na=False)]
sandwiches = restaurants[restaurants['categories'].str.contains('Sandwiches|Delis|Bagels|Hot Dogs',case=False,na=False)]
coffee = restaurants[restaurants['categories'].str.contains('Coffee|',case=False,na=False)]
japanese = restaurants[restaurants['categories'].str.contains('Japanese|Sushi|Ramen',case=False,na=False)]
korean = restaurants[restaurants['categories'].str.contains('Korean',case=False,na=False)]
indian = restaurants[restaurants['categories'].str.contains('Indian',case=False,na=False)]
chinese = restaurants[restaurants['categories'].str.contains('Chinese|Dim Sum|Cantonese|Szechuan',case=False,na=False)]
mediterranean = restaurants[restaurants['categories'].str.contains('Mediterranean',case=False,na=False)]
vegetable_people = restaurants[restaurants['categories'].str.contains('Salad|Vegetarian',case=False,na=False)]
thai = restaurants[restaurants['categories'].str.contains('Thai',case=False,na=False)]
vietnamese = restaurants[restaurants['categories'].str.contains('Vietnamese',case=False,na=False)]
halal = restaurants[restaurants['categories'].str.contains('Halal',case=False,na=False)]

mexican = restaurants[restaurants['categories'].str.contains('Mexican|Tacos|Tex-Mex|Latin American',case=False,na=False)]
mexican = mexican[~mexican.categories.str.contains("Fast Food") ]


