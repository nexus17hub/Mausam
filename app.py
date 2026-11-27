
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/interests", methods=["GET", "POST"])
def interests():

    selected_interests = []
    error = None
    submitted = False

    if request.method == "POST":

        selected_interests = request.form.getlist("interests")

        if not selected_interests:
            error = "Please select at least one interest."
        else:
            submitted = True

            print("Selected interests:", selected_interests)

    return render_template(
        "interests.html",
        selected_interests=selected_interests,
        error=error,
        submitted=submitted
    )


if __name__ == "__main__":
    app.run(debug=True)
