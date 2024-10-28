from flask import Flask, render_template, request
import string

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    return strength

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    remarks = ""

    if request.method == "POST":
        password = request.form.get("password")
        strength = check_password_strength(password)

        if strength == 1:
            remarks = "Very weak password."
        elif strength == 2:
            remarks = "Weak password."
        elif strength == 3:
            remarks = "Moderate password."
        elif strength == 4:
            remarks = "Strong password."
        elif strength == 5:
            remarks = "Very strong password!"

        score = strength / 5  # Normalize the score between 0 and 1 for a scale

    return render_template("index.html", score=score, remarks=remarks)

if __name__ == "__main__":
    app.run(debug=True)
