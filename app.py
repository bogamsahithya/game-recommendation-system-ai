from flask import Flask, render_template, request

from game_recommendation import recommend_games

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    filters = {
        "genre": "",
        "platform": "",
        "recommended_for": "",
        "min_rating": 0.0,
        "max_results": 5,
    }

    if request.method == "POST":
        filters["genre"] = request.form.get("genre", "").strip()
        filters["platform"] = request.form.get("platform", "").strip()
        filters["recommended_for"] = request.form.get("recommended_for", "").strip()
        filters["min_rating"] = float(request.form.get("min_rating") or 0.0)
        filters["max_results"] = int(request.form.get("max_results") or 5)

        results = recommend_games(
            genre=filters["genre"] or None,
            platform=filters["platform"] or None,
            recommended_for=filters["recommended_for"] or None,
            min_rating=filters["min_rating"],
            max_results=filters["max_results"],
        )

    return render_template("index.html", results=results, filters=filters)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
