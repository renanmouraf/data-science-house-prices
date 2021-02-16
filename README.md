# Data Science Project: House Prices

## Environment and Packages
Create a virtual environment to isolate your Python project:

```
python3 -m venv venv
```

Activate the virtual environment

```
source ./venv/bin/activate
```

Install the necessary packages:

```
pip install -r requirements.txt
```

## EDA (Exploratory Data Analisys)
To check the EDA (Exploratory Data Analisys):

```
jupyter-notebook Exploratory-Data-Analysis-House-Prices.ipynb
```

Then, with the Jupyter Notebook open go to `Cell > Run All` to run all the commands.

## Clean Data

To perform the cleaning process on the raw data:

```
python data_cleaning.py
```

This will generate the 'cleaned_data.csv'.

## Create the Machine Learning Model

To train the model:

```
python train_model.py
```

This will create the 'train.csv', 'test.csv', and 'model.pkl'.

## Run and test the API

To run the API:

```
uvicorn api:app
```

To test the API, another terminal, activate the virtual environment again (this time you already have the packages installed):

```
source ./venv/bin/activate
```

And then run:

```
python test_api.py
```
