from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

from src.models.base_model import BaseModel
@@ -7,5 +8,8 @@
class SVCModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline([('svc', SVC(**kwargs))])
            model=Pipeline([
                ('countv', CountVectorizer()),
                ('svc', SVC(**kwargs))
            ])
        )
