import numpy
from sklearn import linear_model
from sklearn import preprocessing

# Read data
nb_features, n = map(int, input().split())
training_data = numpy.array([input().split() for _ in range(n)], numpy.float)
t = int(input())
test_data = numpy.array([input().split() for _ in range(t)], numpy.float)

# Prepare our model
model = linear_model.LinearRegression()
poly = preprocessing.PolynomialFeatures(degree=3, include_bias=False)

# Train our model
training_features = training_data[:, :-1]
training_prices = training_data[:, -1]
model.fit(poly.fit_transform(training_features), training_prices)

# Predict the prices for the test data
predicted_prices = model.predict(poly.fit_transform(test_data))
print(*predicted_prices, sep='\n')
