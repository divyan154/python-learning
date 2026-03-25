# Can import yield from differen generators just like from different functions you can get different values
def languages():
    yield "Japanese"
    yield "English"

def languages_want_to_learn():
    yield "French"
    yield "Russian"

def all_languages():
    yield from languages()
    yield from languages_want_to_learn()

for lang in all_languages():
    print(lang)