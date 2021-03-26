import typing as t
import typing_extensions as te
import datetime

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class DatasetReader(te.Protocol):
    def __call__(self) -> pd.DataFrame:
        ...


SplitName = te.Literal["train", "test"]


def get_dataset(reader: DatasetReader, splits: t.Iterable[SplitName]):
    df = reader()
#    df = clean_dataset(df)
    y = df["cnt"]
    X = df.drop(columns=["instant", "dteday", "casual","registered", "cnt"])
    X_train, y_train = X[X["yr"]==0], y[X["yr"]==0]
    X_test, y_test = X[X["yr"]==1], y[X["yr"]==1]
    X_train = X_train.drop(columns="yr")
    X_test = X_test.drop(columns="yr") 

    split_mapping = {"train": (X_train, y_train), "test": (X_test, y_test)}
    return {k: split_mapping[k] for k in splits}

def genera_registros_faltantes (df):
    df['hr']=df.hr.astype(str)

    for i in range(df['hr'].shape[0]):
        if len(df['hr'][i])<2:
            df['hr'][i] = "0"+ df['hr'][i]

    df.index = df['dteday'] + ' '+ df['hr'] +':00:00'
    df.index = pd.to_datetime(df.index, infer_datetime_format=True)
    df = df.reindex(pd.date_range(df.index[0], df.index[-1], freq='1H'))

    return df

def fix_dates (df):
    df.yr   = pd.DatetimeIndex(df.index).year
    df.mnth = pd.DatetimeIndex(df.index).month
    df.hr   = pd.DatetimeIndex(df.index).hour
    df.weekday = pd.DatetimeIndex(df.index).weekday+1
    df.yr[df.yr == 2011] = 0
    df.yr[df.yr == 2012] = 1
    return df

def complete_data (df):
    df['weekday_hr'] = df['weekday'].astype(str) +"_" + df['hr'].astype(str)
    median_weekday_hr = df[df.dteday.notnull()].groupby('weekday_hr').median()['cnt']

    for i in range (df.shape[0]):
        if df.dteday.isnull()[i]:
            df.season[i] = df.season[i-1]
            df.weathersit[i] = df.weathersit[i-1]
            df.temp[i] = df.temp[i-1]
            df.atemp[i] = df.atemp[i-1]
            df.hum[i] = df.hum[i-1]
            df.windspeed[i] = df.windspeed[i-1]
            df.cnt[i] = median_weekday_hr[df.weekday_hr[i]]
            df.holiday[i] = 0.0
            df.workingday[i] = 0.0

    df.season = df.season.astype(str)
    df.holiday = df.holiday.astype(str)
    df.workingday = df.workingday.astype(str)
    df.weathersit = df.weathersit.astype(str)
    df.windspeed = df.windspeed.astype(int)
    df.temp = df.temp.astype(int)
    df.hum = df.hum.astype(int)
    return df
