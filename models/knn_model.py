from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

from src.models.base_model import BaseModel

class KNNModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline([
                ('countv', CountVectorizer()),
                ('dt', KNeighborsClassifier(**kwargs, n_neighbors=3))
            ])
        )
