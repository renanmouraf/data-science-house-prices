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

## Clean the Data, Machine Learning Model, Run API 

The following steps must be executed in sequence.

### Clean the Data

To perform the cleaning process on the raw data:

```
python data_cleaning.py
```

Expected output:

```
Original Data: (1168, 81)
Columns with missing values: 0
Series([], dtype: int64)
After Cleaning: (1168, 73)
```

This will generate the 'cleaned_data.csv'.

### Create the Machine Learning Model

To train the model:

```
python train_model.py
```

Expected output:

```
Train data for modeling: (934, 73)
Test data for predictions: (234, 73)
Training the model ...
Testing the model ...
Average Price Test: 175652.0128205128
RMSE: 11098.009355519898
Model saved at model.pkl
```

This will create the 'train.csv', 'test.csv', and 'model.pkl'.

### Run and test the API

To run the API:

```
uvicorn api:app
```

Expected output:

```
INFO:     Started server process [56652]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

To test the API, on another terminal, activate the virtual environment again (this time you already have the packages installed):

```
source ./venv/bin/activate
```

And then run:

```
python test_api.py
```

Expected output:

```
The actual Sale Price: 109000
The predicted Sale Price: 109000.01144237864
```
