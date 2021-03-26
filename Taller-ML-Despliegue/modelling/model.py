import typing as t

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def build_estimator(hyperparams: t.Dict[str, t.Any]):
    estimator_mapping = get_estimator_mapping()
    steps = []
    for name, params in hyperparams.items():
        estimator = estimator_mapping[name](**params)
        steps.append((name, estimator))
    model = Pipeline(steps)
    return model


def get_estimator_mapping():
    return {
        "regressor": RandomForestRegressor,
    #    "age-extractor": AgeExtractor,
    #    "column-transformer": CustomColumnTransformer,
    #    "simplified-transformer": SimplifiedTransformer,
    }