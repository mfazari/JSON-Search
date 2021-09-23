from search import load_file, sort, calc_score


def test_load_file():
    assert type(load_file()) is list


def test_sort():
    a = [{
        "score": 2
    },
        {
            "score": 1
        }]
    b = [{
        "score": 1
    },
        {
            "score": 2
        }]
    assert sort(a) == b


def test_calc_score():
    string1 = "hello world"
    string2 = "hello world"
    assert calc_score(string1, string2) == 0
