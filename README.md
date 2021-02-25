# Data Science Project: House Prices

This repository implements a Data Science and Machine Learning project applied to a House Prices dataset from the Kaggle competition [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

**>>>[You can also watch how to run this project on Youtube](https://youtu.be/xEfCyb-0Wsk)<<<**

In this repository you will find:

* requirements.txt: The packages you need to install using pip
* raw_data.csv: The raw data we are using on this project
* Exploratory-Data-Analysis-House-Prices.ipynb: The Jupyter Notebook with the Exploratory Data Analysis
* data_cleaning.py: The script that clean the data
* train_model.py: The script to train the Machine Learning Model using the cleaned data
* predict.py: The file with the HousePriceModel class that we use to load the ML model and make the predictions
* api.py: The API was created with the framework [FastAPI](https://fastapi.tiangolo.com/)
* test_api.py: The script to test the API

To use the data and code in the repository, follow the steps in the next sections.

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

You should see a message similar to this at the end:

```
Successfully installed Babel-2.9.0 Jinja2-2.11.3 MarkupSafe-1.1.1 Pygments-2.8.0 Send2Trash-1.5.0 anyio-2.1.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.3.0 certifi-2020.12.5 cffi-1.14.5 chardet-4.0.0 click-7.1.2 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 fastapi-0.63.0 h11-0.12.0 idna-2.10 ipykernel-5.4.3 ipython-7.20.0 ipython-genutils-0.2.0 jedi-0.18.0 joblib-1.0.1 json5-0.9.5 jsonschema-3.2.0 jupyter-client-6.1.11 jupyter-core-4.7.1 jupyter-server-1.3.0 jupyterlab-3.0.7 jupyterlab-pygments-0.1.2 jupyterlab-server-2.2.0 mistune-0.8.4 nbclassic-0.2.6 nbclient-0.5.2 nbconvert-6.0.7 nbformat-5.1.2 nest-asyncio-1.5.1 notebook-6.2.0 numpy-1.20.1 packaging-20.9 pandas-1.2.2 pandocfilters-1.4.3 parso-0.8.1 pexpect-4.8.0 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.16 ptyprocess-0.7.0 pycparser-2.20 pydantic-1.7.3 pyparsing-2.4.7 pyrsistent-0.17.3 python-dateutil-2.8.1 pytz-2021.1 pyzmq-22.0.3 requests-2.25.1 scikit-learn-0.24.1 scipy-1.6.0 six-1.15.0 sniffio-1.2.0 starlette-0.13.6 terminado-0.9.2 testpath-0.4.4 threadpoolctl-2.1.0 tornado-6.1 traitlets-5.0.5 urllib3-1.26.3 uvicorn-0.13.3 wcwidth-0.2.5 webencodings-0.5.1
```

## EDA (Exploratory Data Analysis)
To check the EDA (Exploratory Data Analysis):

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
