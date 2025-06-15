import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Generate dummy data: 100 samples, 5 features
X = np.random.randint(0, 2, (100, 5))
y = np.random.choice([-1, 1], 100)

model = RandomForestClassifier()
model.fit(X, y)

with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to model/phishing_model.pkl")