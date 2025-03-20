from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
    <head>
        <title>Temperature Converter</title>
    </head>
    <body>
        <h2>Convert Temperature</h2>
        <form method="post">
            <label>Enter Temperature:</label>
            <input type="text" name="temperature" required>
            <select name="unit">
                <option value="C">Celsius to Fahrenheit</option>
                <option value="F">Fahrenheit to Celsius</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if result is not none %}
            <h3>Converted Temperature: {{ result }}</h3>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def convert():
    result = None
    if request.method == "POST":
        try:
            temp = float(request.form["temperature"])
            unit = request.form["unit"]
            if unit == "C":
                result = (temp * 9/5) + 32
                result = f"{result:.2f} °F"
            else:
                result = (temp - 32) * 5/9
                result = f"{result:.2f} °C"
        except ValueError:
            result = "Invalid Input"
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
