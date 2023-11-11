import json


def task(path) -> float:
    with open(path, 'r') as f:
        data = json.load(f)

    sum_of_products = sum([element["score"] * element["weight"] for element in data])

    return round(sum_of_products, 3)


print(task("input.json"))
