
# sklearn imports
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_pickle("data/elastic_features.pkl")
y = df['K_VRH'].values
excluded = ["G_VRH", "K_VRH", "elastic_anisotropy", "formula", "material_id", 
            "poisson_ratio", "structure", "composition", "composition_oxid"]

X = df.drop(excluded, axis=1)

# set estimators
n_estimators = 50

rf = RandomForestRegressor(n_estimators, random_state=1)

rf.fit(X, y)
print('training R2 = ' + str(round(rf.score(X, y), 3)))
print('training RMSE = %.3f' % np.sqrt(mean_squared_error(y_true=y, y_pred=rf.predict(X))))

y_pred = rf.predict(X)

plt.figure()
plt.scatter(y, y_pred)
plt.xlabel("K_VRH (GPa)")
plt.ylabel("Predicted K_VRH (GPa)")
plt.title(f"Random Forest(N{n_estimators}) Predicted Bulk Modulus")

min_val = min(y.min(), y_pred.min())
max_val = max(y.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val])

plt.tight_layout()
plt.savefig(f"figs/RF_N{n_estimators}_predict.png", dpi=300)


# lets use Kfold cross validation
# Use 10-fold cross validation (90% training, 10% test)
kfv = KFold(n_splits=10, shuffle=True, random_state=1)
scores = cross_val_score(rf, X, y, cv=kfv, scoring='neg_mean_squared_error')
rmse_scores = [np.sqrt(abs(s)) for s in scores]
r2_scores = cross_val_score(rf, X, y, scoring='r2', cv=kfv, n_jobs=1)

print('Cross-validation results:')
print('Folds: %i, mean R2: %.3f' % (len(scores), np.mean(np.abs(r2_scores))))
print('Folds: %i, mean RMSE: %.3f' % (len(scores), np.mean(np.abs(rmse_scores))))