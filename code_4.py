import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

lower_file = big_mac_file.lower()

df = pd.read_csv(lower_file)


def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{country_code.upper()}' and date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query)
    mean_price_country = (round(df_result['dollar_price'].mean(),2))
    return mean_price_country

def get_big_mac_price_by_country(country_code):
    query_2 = f"(iso_a3 == '{country_code.upper()}')"
    df_result_2 = df.query(query_2)
    mean_price_country_2 = (round(df_result_2['dollar_price'].mean(),2))
    return mean_price_country_2

def get_the_cheapest_big_mac_price_by_year(year):
    query_3 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    cheap_year = df.query(query_3)
    cheap_min_idx = cheap_year['dollar_price'].idxmin()
    cheap_price = (round(cheap_year['dollar_price'].min(),2))
    return f"{cheap_year.loc[cheap_min_idx]['name']}({cheap_year.loc[cheap_min_idx]['iso_a3']}): ${cheap_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query_4 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    expensive_year = df.query(query_4)
    exp_price = (round(expensive_year['dollar_price'].max(),2))
    exp_min_idx = expensive_year['dollar_price'].idxmax()
    return f"{expensive_year.loc[exp_min_idx]['name']}({expensive_year.loc[exp_min_idx]['iso_a3']}): ${exp_price}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2012,'arg')
    print(result_a)
    result_b = get_big_mac_price_by_country('jpn')
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2011)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)