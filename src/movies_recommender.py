"""Simple correlation-based movie recommendation demo.

Copyright (c) 2026 Mohamed Dawood. MIT License; see LICENSE.
"""
from pathlib import Path
import argparse
import pandas as pd

COLUMNS = ["Title", "Director", "Rating"]


def load_movies(path: Path, limit: int = 300) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = set(COLUMNS) - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if "Year" in data.columns:
        data = data.sort_values("Year", ascending=False)
    return data.head(limit).loc[:, COLUMNS].dropna()


def correlation_matrix(data: pd.DataFrame, index: str, columns: str) -> pd.DataFrame:
    matrix = data.pivot_table(index=index, columns=columns, values="Rating").fillna(0)
    return matrix.corr()


def choose(label: str, values: pd.Index) -> int:
    for number, value in enumerate(values):
        print(f"{number:>3}: {value}")
    selected = int(input(f"Choose {label} index: "))
    if selected < 0 or selected >= len(values):
        raise ValueError(f"{label} index is out of range")
    return selected


def show_related(correlations: pd.DataFrame, selected: int, count: int = 10) -> None:
    series = correlations.iloc[:, selected].sort_values(ascending=False)
    print("\n".join(map(str, series.head(count + 1).index)))


def main() -> None:
    parser = argparse.ArgumentParser(description="Correlation-based movie recommendation demo")
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--limit", type=int, default=300)
    args = parser.parse_args()

    movies = load_movies(args.dataset, args.limit)
    by_title = correlation_matrix(movies, "Director", "Title")
    show_related(by_title, choose("movie title", by_title.columns))

    by_director = correlation_matrix(movies, "Title", "Director")
    show_related(by_director, choose("director", by_director.columns))


if __name__ == "__main__":
    main()
