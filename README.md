# Time-series-outlier-detection

This project implements a statistical method to detect and replace outliers in time series data.
Outliers are identified using a rolling window Z-score approach, and detected anomalies are replaced using a rolling median estimate to preserve the structure of the signal.

The method detects both local and global anomalies while balancing noise and natural variability in the data. 


**The pipeline produces three visualizations:**

<img width="1200" height="500" alt="outliers" src="https://github.com/user-attachments/assets/3f87f557-7163-4db9-aa0e-c366565f7602" />

1.Original Data – raw time series containing anomalies

2.Outlier Detection – detected outliers highlighted in red

3.Outliers Replaced – cleaned time series after replacing anomalies

**Methodology**

The algorithm works in two stages:

**1. Outlier Detection**

For each observation:

-A rolling window around the current point is created

-The mean and standard deviation of the window are computed

-A Z-score is calculated

If |z| > z theshold, the point is considered an outlier.

Parameters used in this project:
Window: size =	90	Local context around each observation
Z-score threshold: 2.7 Sensitivity for anomaly detection

**2. Outlier Replacement**

Detected outliers are replaced using a rolling median estimate:
-A centered rolling median smooths the signal
-The median value replaces the detected anomaly
-This preserves the trend and seasonality of the series
