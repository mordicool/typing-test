from flask import jsonify
import dal

DEFAULT_TOP_ANSWERS = 5

def get_specific_typing_test(type_id):
    specific_typing_test = dal.get_typing_test_by_id(type_id)
    return jsonify(specific_typing_test)

def get_random_typing_test():
    random_typing_test = dal.get_random_typing_test()
    return jsonify(random_typing_test)

def get_all_highscores(type_id):
    highscores = dal.get_all_highscores(type_id)
    return jsonify(highscores)

def get_top_highscores(type_id, top_answers):
    if (top_answers < 1 or top_answers > 30):
        top_answers = DEFAULT_TOP_ANSWERS
    highscores = dal.get_all_highscores(type_id)

    sorted_highscores = sorted(highscores, key=lambda s: s['time'])
    return jsonify(sorted_highscores[:top_answers])

def submit_highscore(type_id, highscore):
    result = dal.submit_highscore(type_id, highscore)
    return result
