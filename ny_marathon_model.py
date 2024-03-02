import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

#zamiana czasu w postaci hh:mm:ss na liczbę sekund
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_seconds = (h * 3600) + (m * 60) + s
    return total_seconds


data = pd.read_csv('cleared_runners_data.csv')
data.dropna(inplace=True)

data['Result'] = data['Result'].apply(time_to_seconds)

# data = data.tail(1000)

#transformacja danych nienumerycznych na wartości naturalne
le = LabelEncoder()
data['Country'] = le.fit_transform(data['Country'])
data['Sex'] = le.fit_transform(data['Sex'])

X = data[['Age', 'Country', 'Sex']]
Y = data['Result']

#podział danych ba testowe i treningowe
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#potencjalne modele
model = LinearRegression()
# model = make_pipeline(PolynomialFeatures(degree=50), LinearRegression())
# model = DecisionTreeRegressor()
# model = RandomForestRegressor()
# model = SVR(kernel='rbf')

model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

mae = mean_absolute_error(Y_test, Y_pred)
print("Średni błąd bezwzględny (MAE):", mae/60 ," minut")


