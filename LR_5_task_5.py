{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPvpmEqyp0zK1/LalI4JTl2"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":3,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"6n5q3YZ8Qrw7","executionInfo":{"status":"ok","timestamp":1734903281007,"user_tz":-120,"elapsed":4307,"user":{"displayName":"Ярослав Білотіл","userId":"06797585363548962278"}},"outputId":"139cd02b-8596-46c9-aeca-8ea0dc5d2935"},"outputs":[{"output_type":"stream","name":"stdout","text":["Mean absolute error: 7.42\n","Predicted traffic: 26\n"]},{"output_type":"stream","name":"stderr","text":["<ipython-input-3-7c223885615c>:52: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)\n","  test_datapoint_encoded[i] = int(label_encoder[count].transform([test_datapoint[i]]))  # Fixed the index error\n","<ipython-input-3-7c223885615c>:52: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)\n","  test_datapoint_encoded[i] = int(label_encoder[count].transform([test_datapoint[i]]))  # Fixed the index error\n","<ipython-input-3-7c223885615c>:52: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)\n","  test_datapoint_encoded[i] = int(label_encoder[count].transform([test_datapoint[i]]))  # Fixed the index error\n","<ipython-input-3-7c223885615c>:52: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)\n","  test_datapoint_encoded[i] = int(label_encoder[count].transform([test_datapoint[i]]))  # Fixed the index error\n"]}],"source":["import numpy as np\n","import matplotlib.pyplot as plt\n","from sklearn.metrics import classification_report, mean_absolute_error\n","from sklearn.model_selection import train_test_split\n","from sklearn.preprocessing import LabelEncoder\n","from sklearn.ensemble import ExtraTreesRegressor\n","\n","input_file = 'traffic_data.txt'\n","data = []\n","with open(input_file, 'r') as f:\n","    for line in f.readlines():\n","        items = line[:-1].split(',')  # Fixed the typo\n","        data.append(items)\n","\n","data = np.array(data)\n","\n","# Conversion of string data to numeric\n","label_encoder = []\n","X_encoded = np.empty(data.shape)\n","\n","for i, item in enumerate(data[0]):\n","    if item.isdigit():\n","        X_encoded[:, i] = data[:, i]\n","    else:\n","        label_encoder.append(LabelEncoder())\n","        X_encoded[:, i] = label_encoder[-1].fit_transform(data[:, i])\n","\n","X = X_encoded[:, :-1].astype(int)\n","y = X_encoded[:, -1].astype(int)\n","\n","# Splitting data into training and test sets\n","X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)\n","\n","# A regressor based on marginally random forests\n","params = {'n_estimators': 100, 'max_depth': 4, 'random_state': 0}  # Fixed the syntax error\n","regressor = ExtraTreesRegressor(**params)\n","regressor.fit(X_train, y_train)\n","\n","# Calculation of performance characteristics of the regressor on the test data\n","y_pred = regressor.predict(X_test)\n","print(\"Mean absolute error:\", round(mean_absolute_error(y_test, y_pred), 2))\n","\n","# Testing coding on a single example\n","test_datapoint = ['Saturday', '10:20', 'Atlanta', 'no']\n","test_datapoint_encoded = [-1] * len(test_datapoint)\n","count = 0\n","\n","for i, item in enumerate(test_datapoint):\n","    if item.isdigit():\n","        test_datapoint_encoded[i] = int(test_datapoint[i])\n","    else:\n","        test_datapoint_encoded[i] = int(label_encoder[count].transform([test_datapoint[i]]))  # Fixed the index error\n","    count += 1\n","\n","test_datapoint_encoded = np.array(test_datapoint_encoded)\n","\n","# Prediction of the result for a test data point\n","print(\"Predicted traffic:\", int(regressor.predict([test_datapoint_encoded])[0]))\n"]}]}