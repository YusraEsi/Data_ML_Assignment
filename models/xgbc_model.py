import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

from src.models.base_model import BaseModel


class XGBCModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline([('xgbc', xgb.XGBClassifier(**kwargs))])
            model=Pipeline([
                ('countv', CountVectorizer()),
                ('xgbc', xgb.XGBClassifier(**kwargs))
            ])
        )
