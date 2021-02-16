import pickle
import pandas as pd


class HousePriceModel():

    def __init__(self):
        self.model = self.load_model()
        self.preds = None

    def load_model(self):
        pkl_filename = 'model.pkl'

        try:
            with open(pkl_filename, 'rb') as file:
                pickle_model = pickle.load(file)
        except:
            print(f'Error loading the model at {pkl_filename}')
            return None

        return pickle_model

    def predict(self, data):

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data, index=[0])

        self.preds = self.model.predict(data)
        return self.preds
