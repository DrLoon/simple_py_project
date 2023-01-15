import argparse
import zipfile

import numpy as np
import pandas as pd


def load(path: str) -> pd.DataFrame:
    assert path
    with zipfile.ZipFile(path) as z:
        with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
            df = pd.read_csv(f, parse_dates=["dt"])
    df = df[df['dt'] >= '1950-01-01']
    df = df.reset_index()
    return df


def find_hotest_city(df: pd.DataFrame, year: int):
    assert isinstance(year, int)
    df['dt_year'] = df['dt'].map(lambda x: x.year == year)
    df_year = df[df['dt_year'] == True].drop(columns=['dt_year'])
    cities = df_year['City'].drop_duplicates().values
    months = df_year['dt'].drop_duplicates().values
    temps = [df_year[df_year['dt'] == month].AverageTemperature.mean() for month in months]

    res_month = str(pd.to_datetime(months[np.argmax(temps)]).date())

    res_cities = []
    for city in cities:
        if df_year[df_year['City'] == city]['AverageTemperature'].max() >= max(temps):
            res_cities.append(city)

    return res_month, res_cities


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data analysis')
    parser.add_argument('indir', type=str, help='Input dir for data')
    parser.add_argument('year', type=int, help='Year')

    args = parser.parse_args()
    df = load(args.indir)
    print(find_hotest_city(df, args.year))
