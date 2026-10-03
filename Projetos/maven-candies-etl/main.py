from transform import transform_data
from load import load_data

df_products, df_orders, df_customers = transform_data()
load_data(df_products, df_orders, df_customers)