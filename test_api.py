import requests
from predict import HousePriceModel


sample_input = {'MSSubClass': 20, 'MSZoning': 'RL', 
'LotArea': 7922, 'Street': 'Pave', 
'LotShape': 'Reg', 'LandContour': 'Lvl', 
'Utilities': 'AllPub', 'LotConfig': 'Inside', 
'LandSlope': 'Gtl', 'Neighborhood': 'NAmes', 
'Condition1': 'Norm', 'Condition2': 'Norm', 
'BldgType': '1Fam', 'HouseStyle': '1Story', 
'OverallQual': 5, 'OverallCond': 7, 
'YearBuilt': 1953, 'YearRemodAdd': 2007, 
'RoofStyle': 'Gable', 'RoofMatl': 'CompShg', 
'Exterior1st': 'VinylSd', 'Exterior2nd': 'VinylSd', 
'MasVnrType': 'None', 'ExterQual': 3,
'ExterCond': 4, 'Foundation': 'CBlock', 
'BsmtQual': 3, 'BsmtCond': 3, 
'BsmtExposure': 'No', 'BsmtFinType1': 'GLQ', 
'BsmtFinSF1': 731, 'BsmtFinType2': 'Unf', 
'BsmtFinSF2': 0, 'BsmtUnfSF': 326, 
'TotalBsmtSF': 1057, 'Heating': 'GasA', 
'HeatingQC': 3, 'CentralAir': 'Y', 
'Electrical': 'SBrkr', '1stFlrSF': 1057, 
'2ndFlrSF': 0, 'LowQualFinSF': 0, 
'GrLivArea': 1057, 'BsmtFullBath': 1, 
'BsmtHalfBath': 0, 'FullBath': 1, 
'HalfBath': 0, 'BedroomAbvGr': 3, 
'KitchenAbvGr': 1, 'KitchenQual': 4, 
'TotRmsAbvGrd': 5, 'Functional': 'Typ', 
'Fireplaces': 0, 'FireplaceQu': 0, 
'GarageType': 'Detchd', 'GarageFinish': 'Unf',
'GarageCars': 1, 'GarageArea': 246, 
'GarageQual': 3, 'GarageCond': 3, 
'PavedDrive': 'Y', 'WoodDeckSF': 0, 
'OpenPorchSF': 52, 'EnclosedPorch': 0, 
'3SsnPorch': 0, 'ScreenPorch': 0, 
'PoolArea': 0, 'MiscVal': 0, 'MoSold': 1,
'YrSold': 2010, 'SaleType': 'WD', 
'SaleCondition': 'Abnorml'}

def run_prediction_from_sample():

    url="http://127.0.0.1:8000/predict"
    headers = {"Content-Type": "application/json", "Accept":"text/plain"}

    response = requests.post(url, headers=headers, json=sample_input)
    print("The actual Sale Price: 109000")
    print(f"The predicted Sale Price: {response.text}")


if __name__ == "__main__":
    run_prediction_from_sample()