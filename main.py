import json
def decorator(func):
    def wrapper(path):
        sufix=path.split(".")[-1]
        if sufix == "json":
            return func(path)
        else:
            return "Json fayl emas"
    return wrapper

@decorator
def readJson(path):
    with open(path) as f:
        data =json.load(f)
    return data
print(readJson("data.csv"))