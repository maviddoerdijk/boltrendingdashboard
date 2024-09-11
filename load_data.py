import json
import pandas as pd

def load_data():
    with open('mock_data.json', 'r') as file:
        data = json.load(file)
        
        
    
    # Converteer JSON-secties naar dataframes
    distribution_centers_df = pd.DataFrame(data['distribution_centers'])
    top_search_terms_df = pd.DataFrame(data['top_search_terms'])
    seasonal_search_volume_df = pd.DataFrame(data['seasonal_search_volume'])
    product_margins_df = pd.DataFrame(data['product_margins'])
    top_products_no_stock_df = pd.DataFrame(data['top_products_no_stock'])
    longest_delivery_times_df = pd.DataFrame(data['longest_delivery_times'])
    
    
    
     
    return {
        "distribution_centers": distribution_centers_df,
        "top_search_terms": top_search_terms_df,
        "seasonal_search_volume": seasonal_search_volume_df,
        "product_margins": product_margins_df,
        "top_products_no_stock": top_products_no_stock_df,
        "longest_delivery_times": longest_delivery_times_df
    }
