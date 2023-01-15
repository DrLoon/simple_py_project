import argparse
import zipfile

import matplotlib.pyplot as plt
import pandas as pd


def load(path: str):
    with zipfile.ZipFile(path) as z:
        with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
            df = pd.read_csv(f, parse_dates=["dt"])
    df = df[df['dt'] >= '1950-01-01']
    df = df.reset_index()
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data analysis')
    parser.add_argument('indir', type=str, help='Input dir for data')
    parser.add_argument('year', type=int, help='Year')

    args = parser.parse_args()
    print(args.indir, args.year)
    print(load("C:/Users/aleka/Downloads/archive.zip").head())
