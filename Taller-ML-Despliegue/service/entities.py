import typing as t
import typing_extensions as te

from pydantic import BaseModel, Field, ConstrainedInt, PositiveInt, PositiveFloat, ConstrainedFloat


mnthLiteral = te.Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hrLiteral = te.Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
"13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
seasonLiteral = te.Literal["1", "2", "3", "4"]
generalLiteral = te.Literal["0", "1"]
weekdayLiteral = te.Literal["0", "1", "2", "3", "4", "5", "6"]
weathersitLiteral = te.Literal["1", "2", "3", "4"]

class generalInteger(ConstrainedFloat):
    ge: 0.1
    le: 1

class ModelInput(BaseModel):
    yr: generalLiteral
    mnth: mnthLiteral
    hr: hrLiteral
    season: seasonLiteral
    holiday: generalLiteral
    weekday: weekdayLiteral
    workingday: generalLiteral
    weathersit: weathersitLiteral
    temp: generalInteger
    atemp: generalInteger
    hum: generalInteger
    windspeed: generalInteger


#NeighborhoodLiteral = te.Literal[
#    "Blmgtn",
#    "Blueste",
#    "BrDale",
#    "BrkSide",
#    "ClearCr",
#    "CollgCr",
#    "Crawfor",
#    "Edwards",
#    "Gilbert",
#    "IDOTRR",
#    "Meadow",
#    "Mitchel",
#    "Names",
#    "NoRidge",
#    "NPkVill",
#    "NridgHt",
#    "NWAmes",
#    "OldTwon",
#    "SWISU",
#    "Sawyer",
#    "SawyerW",
#    "Somerst",
#    "StoneBr",
#    "Timber",
#    "Veenker",
#]
#HouseStyleLiteral = te.Literal[
#    "1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"
#]


# class ModelInput(BaseModel):
#     YrSold: PositiveInt
#     YearBuilt: PositiveInt
#     YearRemodAdd: PositiveInt
#     GarageYrBlt: PositiveInt
#     LotArea: PositiveFloat
#     Neighborhood: NeighborhoodLiteral
#     HouseStyle: HouseStyleLiteral


#class YearInteger(ConstrainedInt):
#    ge = 1800
#    le = 2020


#class ModelInput(BaseModel):
#    YrSold: YearInteger
#    YearBuilt: YearInteger
#    YearRemodAdd: YearInteger
#    GarageYrBlt: YearInteger
#    LotArea: PositiveFloat
#    Neighborhood: NeighborhoodLiteral
#    HouseStyle: HouseStyleLiteral