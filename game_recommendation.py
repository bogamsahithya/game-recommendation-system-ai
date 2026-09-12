from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).with_name("game_dataset.xlsx")


def load_games() -> pd.DataFrame:
    df = pd.read_excel(DATA_FILE)
    return df.copy()


def recommend_games(
    genre: str | None = None,
    platform: str | None = None,
    min_rating: float = 0.0,
    max_results: int = 5,
    recommended_for: str | None = None,
) -> list[dict]:
    df = load_games()

    if genre:
        df = df[df["Genre"].str.lower() == genre.lower()]
    if platform:
        df = df[df["Platform"].str.lower() == platform.lower()]
    if recommended_for:
        df = df[df["Recommended_For"].str.lower() == recommended_for.lower()]

    df = df[df["Rating"] >= min_rating].sort_values(by="Rating", ascending=False)

    results = df.head(max_results).to_dict(orient="records")
    return [
        {
            "Game": row["Game"],
            "Genre": row["Genre"],
            "Rating": row["Rating"],
            "Platform": row["Platform"],
            "Difficulty": row["Difficulty"],
            "Recommended_For": row["Recommended_For"],
        }
        for row in results
    ]


if __name__ == "__main__":
    print("Game Recommendation System")
    print("=" * 28)

    sample_recommendations = recommend_games(genre="Action", platform="PC", min_rating=4.5, max_results=3)
    if not sample_recommendations:
        print("No matching games found.")
    else:
        for item in sample_recommendations:
            print(f"{item['Game']} | {item['Genre']} | Rating: {item['Rating']} | {item['Platform']} | {item['Difficulty']} | {item['Recommended_For']}")
