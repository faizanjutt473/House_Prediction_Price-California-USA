import ssl
ssl._create_default_https_context = ssl._create_unverified_context


from sklearn.datasets import fetch_california_housing
import pandas as pd



data = fetch_california_housing()
df = pd.DataFrame(data.data,columns=data.feature_names)
df["price"]=data.target
print("shape", df.shape)
print(df.head())
print(df.describe())
