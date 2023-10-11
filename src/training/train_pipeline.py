from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

from src.constants import RAW_DATASET_PATH, MODELS_PATH, REPORTS_PATH, LABELS_MAP
from src.constants import RAW_DATASET_PATH, MODELS_PATH, REPORTS_PATH, LABELS_MAP, PROCESSED_DATASET_PATH
from src.models.naive_bayes_model import NaiveBayesModel
from src.models.svc_model import SVCModel
from src.models.xgbc_model import XGBCModel
from src.models.decision_tree_model import DecisionTreeModel
from src.models.knn_model import KNNModel
from src.models.random_forest_model import RandomForestModel
from src.utils.plot_utils import PlotUtils


class TrainingPipeline:
    def __init__(self):
        df = pd.read_csv(RAW_DATASET_PATH)
        df = pd.read_csv(PROCESSED_DATASET_PATH)

        text = df['resume']
        y = df['label']
@@ -25,31 +29,43 @@ def __init__(self):
        self.model = None

    def train(self, serialize: bool = True, model_name: str = 'model'):
        self.model = NaiveBayesModel()
        if model_name == "Naive Bayes":
            self.model = NaiveBayesModel()
        elif model_name == "SVC":
            self.model = SVCModel()
        elif model_name == "XGBC":
            self.model = XGBCModel()
        elif model_name == "Decision Tree":
            self.model = DecisionTreeModel()
        elif model_name == "KNN":
            self.model = KNNModel()
        elif model_name == "Random Forest":
            self.model = RandomForestModel()

        self.model.fit(
            self.x_train,
            self.y_train
        )

            
        model_path = MODELS_PATH / f'{model_name}.joblib'
        if serialize:
            self.model.save(
                model_path
            )

    def get_model_perfomance(self) -> tuple:
    def get_model_performance(self) -> tuple:
        predictions = self.model.predict(self.x_test)
        return accuracy_score(self.y_test, predictions), f1_score(self.y_test, predictions, average='weighted')

    def render_confusion_matrix(self, plot_name: str = 'cm_plot'):
    def render_confusion_matrix(self, plot_name: str = 'cm_plot', model_name: str = 'model'):
        predictions = self.model.predict(self.x_test)
        cm = confusion_matrix(self.y_test, predictions)
        plt.rcParams['figure.figsize'] = (14, 10)

        PlotUtils.plot_confusion_matrix(
            cm,
            classes=list(LABELS_MAP.values()),
            title='Naive Bayes'
            title=model_name
        )

        plot_path = REPORTS_PATH / f'{plot_name}.png'
@@ -60,6 +76,6 @@ def render_confusion_matrix(self, plot_name: str = 'cm_plot'):
if __name__ == "__main__":
    tp = TrainingPipeline()
    tp.train(serialize=True)
    accuracy, f1_score = tp.get_model_perfomance()
    accuracy, f1_score = tp.get_model_performance()
    tp.render_confusion_matrix()
    print(f'ACCURACY = {accuracy}, F1 SCORE = {f1_score}')
