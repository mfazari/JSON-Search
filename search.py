import sys
import json


def load_file():
    with open('search_dataset.json') as json_file:
        dataset = json.load(json_file)
    return dataset


def find(dataset, search_query):
    for x in range(len(dataset)):
        brand = dataset[x]["brand"]
        name = dataset[x]["name"]
        term = brand + " " + name
        score = calc_score(search_query, term)
        dataset[x]["score"] = score
    return dataset


def sort(unsorted_result_list):
    sorted_list = sorted(unsorted_result_list, key=lambda k: k['score'])
    with open('sorted_list.json', 'w') as f:
        json.dump(sorted_list, f)
    return sorted_list


def calc_score(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    distance = [[0 for i in range(len1 + 1)]
          for j in range(2)]

    for i in range(0, len1 + 1):
        distance[0][i] = i

    for i in range(1, len2 + 1):
        for j in range(0, len1 + 1):
            if j == 0:
                distance[i % 2][j] = i
            elif str1[j - 1] == str2[i - 1]:
                distance[i % 2][j] = distance[(i - 1) % 2][j - 1]
            else:
                distance[i % 2][j] = (1 + min(distance[(i - 1) % 2][j],
                                        min(distance[i % 2][j - 1],
                                            distance[(i - 1) % 2][j - 1])))
    return distance[len2 % 2][len1]


# main
if __name__ == '__main__':
    dataset = load_file()
    search_query = sys.argv[1]
    unsorted_result_list = find(dataset, search_query)
    sorted_result_list = sort(unsorted_result_list)

    # return 1 to 10
    first_ten_items = list(sorted_result_list)[:10]
    print(first_ten_items)
