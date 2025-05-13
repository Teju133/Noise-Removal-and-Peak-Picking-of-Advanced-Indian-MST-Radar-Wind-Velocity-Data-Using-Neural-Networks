# Noise Removal and Peak Picking of MST Radar Wind Velocity Data Using Neural Networks**

This project focuses on processing and analyzing wind velocity data from the Advanced Indian MST (Mesosphere-Stratosphere-Troposphere) Radar using deep learning techniques. The main goals are:

* **Noise Removal**: Eliminate unwanted noise and irregularities in the radar signal data using neural networks.
* **Peak Picking**: Accurately identify significant peaks in the cleaned data that correspond to meaningful wind velocity patterns.

### 🔍 Problem Statement

Radar wind profiles often contain noise due to atmospheric interference and hardware limitations. Identifying true peaks from such noisy data is crucial for accurate meteorological analysis. Traditional methods struggle with noisy environments. This project leverages the power of neural networks for effective denoising and reliable peak detection.

### 🧠 Technologies & Tools

* **Python**
* **NumPy**, **Pandas**, **Matplotlib**
* **Scikit-learn**
* **TensorFlow** / **Keras**
* **Jupyter Notebook**

### 📊 Dataset

The dataset is derived from MST Radar wind velocity measurements, consisting of time-series data representing vertical and horizontal wind velocities at different altitudes and timestamps.

> *(Note: Dataset access may be restricted due to institutional or government regulations. If applicable, mention how to request or simulate the data.)*

### 🧪 Model Overview

* Preprocessing: Data normalization, outlier removal.
* Denoising: Custom neural network model trained to separate signal from noise.
* Peak Detection: Post-processed signal is analyzed to detect wind velocity peaks using thresholding and derivative analysis.

### ✅ Results

* Achieved significant noise reduction compared to traditional filters.
* Improved accuracy of peak detection by \[insert accuracy % if known].
* Visual plots confirming the effectiveness of the approach.





