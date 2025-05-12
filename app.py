from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = load_model('ddos_model.h5')

# Features used in training
top_features = [
    'Dst Port', 'Tot Fwd Pkts', 'Tot Bwd Pkts', 'Flow Duration',
    'Fwd Pkt Len Max', 'Bwd Pkt Len Max', 'Bwd Pkt Len Min',
    'Pkt Len Var', 'Bwd Seg Size Avg', 'Init Fwd Win Byts',
    'Flow IAT Min', 'Flow IAT Max'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                data = pd.read_csv(file)
                data.drop(['Timestamp'], axis=1, inplace=True, errors='ignore')
                data.replace([np.inf, -np.inf], np.nan, inplace=True)
                data.dropna(inplace=True)
                X = data[top_features]

                scaler = MinMaxScaler()
                X_scaled = scaler.fit_transform(X)

                predictions = model.predict(X_scaled)
                binary_preds = (predictions > 0.5).astype(int).flatten()

                result = "DDoS Detected" if 1 in binary_preds else "No DDoS Detected"
            except Exception as e:
                result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
