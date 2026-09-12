import pandas as pd

from game_recommendation import recommend_games, load_games


def test_load_games_reads_dataset():
    df = load_games()
    assert not df.empty
    assert set(df.columns) == {"Game", "Genre", "Rating", "Platform", "Difficulty", "Recommended_For"}


def test_recommend_games_filters_and_sorts():
    results = recommend_games(genre="Shooting", platform="PC", min_rating=4.5, max_results=3)
    assert results[0]["Game"] == "Valorant"
    assert [item["Game"] for item in results] == ["Valorant", "Call of Duty"]
