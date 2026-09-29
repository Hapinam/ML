"""Simple correlation-based book recommendation demo.

Copyright (c) 2026 Mohamed Dawood. MIT License; see LICENSE.
"""
from pathlib import Path
import argparse
import pandas as pd

COLUMNS = ["title", "authors", "average_rating"]


def load_books(path: Path, limit: int = 300) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = set(COLUMNS) - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    return (
        data.sort_values("average_rating", ascending=False)
        .head(limit)
        .loc[:, COLUMNS]
        .dropna()
    )


def correlation_matrix(data: pd.DataFrame, index: str, columns: str) -> pd.DataFrame:
    matrix = data.pivot_table(index=index, columns=columns, values="average_rating").fillna(0)
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
    parser = argparse.ArgumentParser(description="Correlation-based book recommendation demo")
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--limit", type=int, default=300)
    args = parser.parse_args()

    books = load_books(args.dataset, args.limit)
    by_title = correlation_matrix(books, "authors", "title")
    show_related(by_title, choose("book title", by_title.columns))

    by_author = correlation_matrix(books, "title", "authors")
    show_related(by_author, choose("author", by_author.columns))


if __name__ == "__main__":
    main()
