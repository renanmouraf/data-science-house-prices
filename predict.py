import pickle
import pandas as pd


class HousePriceModel():

    def __init__(self):
        """Create the HousePriceModel object

        Args:
            model_dir (str): directory where the model is stored
            models_path (str): path to models directory
        """
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

    def get_input_example(self):
        """Get an input example for the model

        Returns:
            Dataframe: a dataframe with a set of examples
        """
        input_template = "test.csv"
        input_example = pd.read_csv(input_template, keep_default_na=False).reset_index(drop=True)
        print(input_example.iloc[0].to_dict())
        return input_example

    def get_input_features(self):
        """Get the input features for the model

        Returns:
            list: a list with all features expected by the model
        """
        input_features = self.get_input_example().columns

        return list(input_features)


def main():

    model = HousePriceModel()
    test = model.get_input_example()

    input_features = model.get_input_features()
    print(f"Input features: {input_features}")
    print(f"Predictions: {model.predict(test.to_dict())}")

if __name__ == '__main__':
    main()