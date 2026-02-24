import numpy as np
from sklearn.linear_model import LogisticRegression

# Dummy training data
X = np.array([
    [80, 90],
    [60, 70],
    [30, 40],
    [85, 95],
    [50, 60],
    [20, 30]
])

y = np.array([1, 1, 0, 1, 1, 0])  # 1 = Pass, 0 = Fail

model = LogisticRegression()
model.fit(X, y)

def predict_performance(marks, attendance):
    prediction = model.predict([[marks, attendance]])

    if prediction[0] == 1:
        return "Pass"
    return "Fail"