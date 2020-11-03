import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def wordtranslator(word):
    if word in data:
        return data[word]
    elif word not in data:
        mistake = get_close_matches(word, data.keys(), n=4)
        print("did you mean %s" % mistake)
    else:
        print("word does not exist")


while True:
    word = input("Enter any word")
    new = word.lower()
    ans = (wordtranslator(new))
    if type(ans) == list:
        for output in ans:
            print(output)
    else:
        print(ans)

