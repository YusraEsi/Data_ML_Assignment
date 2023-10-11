from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

from src.models.base_model import BaseModel

class RandomForestModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline([
                    ('countv', CountVectorizer()),
                    ('nbc', RandomForestClassifier(**kwargs))
                ])
        )
