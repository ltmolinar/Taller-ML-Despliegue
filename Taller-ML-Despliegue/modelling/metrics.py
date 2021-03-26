from sklearn.metrics import mean_absolute_error, make_scorer
import numpy as np

def bike_number_error(y_true, y_pred, understock_price=0.6, overstock_price=0.4):
    error=np.zeros(y_true.shape[0])
    error = y_true - y_pred
    error [error >=0] =error*understock_price
    error [error <0] =error*overstock_price*(-1)
    score = error.mean()
    return score


def get_metric_name_mapping():
    return {metric(): bike_number_error}


def get_metric_function(name: str, **params):
    mapping = get_metric_name_mapping()

    def fn(y, y_pred):
        return mapping[name](y, y_pred, **params)

    return fn


def get_scoring_function(name: str, **params):
    mapping = {
        metric(): make_scorer(bike_number_error, **params)
    }
    return mapping[name]


def metric():
    return "bike_number_error"

