from flask import Flask, render_template, request
import re

app = Flask(__name__)


def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    length_ok = len(password) >= 8
    upper_ok = bool(re.search(r"[A-Z]", password))
    lower_ok = bool(re.search(r"[a-z]", password))
    digit_ok = bool(re.search(r"\d", password))
    special_ok = bool(re.search(r"[^A-Za-z0-9]", password))

    if length_ok:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_ok:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_ok:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_ok:
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_ok:
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength_levels[score], feedback


@app.route("/", methods=["GET", "POST"])
def index():
    import os
    print("Templates folder:", os.listdir("templates"))
    print("CWD:", os.getcwd())

    result = None
    feedback = []

    if request.method == "POST":
        password = request.form.get("password")
        result, feedback = check_password_strength(password)

    return render_template("index.html", result=result, feedback=feedback)


if __name__ == "__main__":
    app.run(debug=True)
