import json
from random import randint

with open('typing_tests_mock.json') as file:
    typing_tests_mock = json.load(file)


with open('highscores.json') as file:
    highscores = json.load(file)


def get_all_typing_tests():
    return typing_tests_mock

def get_typing_test_by_id(type_id):
    typing_tests = [typing_test for typing_test in typing_tests_mock if typing_test["id"] == type_id]
    if (len(typing_tests) == 0):
        return None
    return typing_tests[0]

def get_random_typing_test():
    random_id = randint(0, len(typing_tests_mock) - 1)
    return get_typing_test_by_id(random_id)


def get_all_highscores(type_id):
    if (get_typing_test_by_id(type_id) is None):
        return None

    type_id = str(type_id)
    if (type_id not in highscores):
        return []
    return highscores[str(type_id)]

def submit_highscore(type_id, highscore):
    if (get_typing_test_by_id(type_id) is None):
        return False

    type_id = str(type_id)
    if (type_id not in highscores):
        highscores[type_id] = []
    
    exists = [highscore_ for highscore_ in highscores[type_id] if highscore["name"] == highscore_["name"]]
    if (len(exists) > 0):
        if (exists[0]["time"] > highscore["time"]):
            exists[0]["time"] = highscore["time"]
    else:
        highscores[type_id].append(highscore)

    return True