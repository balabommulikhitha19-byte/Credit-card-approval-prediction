from flask import Flask, request, render_template_string
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Credit Card Approval Prediction</title>
</head>
<body>

<h2>Credit Card Approval Prediction</h2>

<form method="POST">

<label>Income:</label><br>
<input type="number" name="income" required><br><br>

<label>Age:</label><br>
<input type="number" name="age" required><br><br>

<input type="submit" value="Predict">

</form>

{% if result %}
<hr>
<h3>{{ result }}</h3>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        income = float(request.form["income"])
        age = float(request.form["age"])

        sample = pd.DataFrame({
            "income": [income],
            "age": [age]
        })

        prediction = model.predict(sample)

        if prediction[0] == 1:
            result = "✅ Credit Card Approved"
        else:
            result = "❌ Credit Card Rejected"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
