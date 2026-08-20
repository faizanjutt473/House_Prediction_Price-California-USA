from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
import pandas as pd
import joblib


print("loading data set")
data = fetch_california_housing()
x=pd.DataFrame(data.data,columns=data.feature_names)
y=data.target

print(f"total records:{x.shape[0]}")

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=42)


#model train
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
    
)
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(Y_test,y_pred)
r2 = r2_score(Y_test ,y_pred)


print(f"averge erro :${mae * 100000:,.0f}")


joblib.dump(model,"house_model.joblib")
joblib.dump(list(x.columns),"house_features.joblib")