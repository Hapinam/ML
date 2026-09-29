# Content-Based Book and Movie Recommender Demos

Two small Python/pandas learning projects that explore correlation-based recommendations using public book and movie metadata.

## Projects

- `src/books_recommender.py` ranks related book titles and authors from a Goodreads-style dataset using average ratings.
- `src/movies_recommender.py` ranks related movie titles and directors from an IMDb-style dataset using movie ratings.

These are educational demonstrations rather than production recommendation engines. They do not model individual user-rating histories or implement collaborative filtering.

## Requirements

Python 3.10+ and pandas.

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python src/books_recommender.py books.csv
python src/movies_recommender.py IMDB-Movie-Data.csv
```

Each program displays the available indexed items and asks which title and creator should be used as the recommendation seed.

## Data

The repository includes the historical CSV datasets used by the original learning project. Dataset rights remain with their respective data providers; the MIT license in this repository applies to the original source code and documentation, not third-party datasets.

## Limitations

The demonstrations intentionally use a small subset of each dataset and simple Pearson correlations over pivot tables. Sparse metadata and aggregate ratings can make the results unstable or less meaningful than modern recommender approaches.

## License

Source code and original documentation are released under the MIT License.

Copyright (c) 2026 Mohamed Dawood.
