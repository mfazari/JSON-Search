# Search Challenge

Introduction
------------

The following program was written as part of a challenge. A redacted (due to copyright reasons) JSON dataset with brand name, product name and id of different products as keys is used. Aim of this challenge was to develop a search algorithm.
## Libaries

To keep it simple and due to time constraints, this project doesn't use any libraries outside the Python standard library besides pytest for testing purposes. However, the following is used:

1. sys
2. json

## Run
Query via a standard argument:

```
python search.py "Apple"
```

The program loads the database, takes the query and compares it with every entry while adding a relevancy score to those entries based on a simple Edit Distance algorithm. At last, the updated database is sorted based on the calculated score.

### Example Output:
Only the first 10 results are output. One looks like this:

[{'id': 32300, 'name': 'iPhone', 'brand': 'Apple', 'score': 1}, {'id': 31000, 'name': 'AirPods', 'brand': 'Apple', 'score': 1}, ... etc.

## Tests
The following command can be used for testing:

```
pytest
```
## Improvements
A more accurate and sophisticated algorithm. An algorithm that gives more relevance to the brand name. I've never developed a search algorithm before, so I had to familiarize myself with edit distances quickly. I combined brand and name key before comparing them with the search query and calculating the score. It's less accurate, but more efficient.


Authors
------------
Massimo Fazari 2021.