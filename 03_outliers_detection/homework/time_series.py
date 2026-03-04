import pandas as pd
import matplotlib.pyplot as plt

"""
Outlier detection and replacement
using Statistical approach

Outliers are detected both locally and
globally while balancing noise and normal
variability.
"""

df = pd.read_csv("data/outlier.txt")
values = df.iloc[:,0]
new_values = values.copy()

w=90
z_score = 2.7
os=[]
outliers_x = []
outliers_i = []
estimates = []
median = values.rolling(10, center=True).median()

for i, x in enumerate(values):
    if i < w or i >= len(values)-w:
        os.append("blue")
        continue
    window = values.iloc[i-w:i+w+1]

    mean = window.mean()
    std = window.std()

    if -z_score<=(x-mean)/std <= z_score:
        os.append("blue")
    else:
        os.append("red")
        outliers_x.append(x)
        outliers_i.append(i)
        estimates.append(median.iloc[i])



new_values.iloc[outliers_i] = estimates
fig, ax = plt.subplots(ncols=3, figsize=(12,5), sharey = True)

x = range(len(values))
ax[0].plot(x,values)
ax[0].set_title("Original Data")

ax[1].plot(x, values)
ax[1].scatter(outliers_i, outliers_x, color='red')
ax[1].set_title("Outlier Detection")

ax[2].plot(x, new_values)
ax[2].set_title("Outliers replaced")

for a in ax:
    a.set_xlabel("Time")
    a.set_ylabel("Value")
plt.show()
















