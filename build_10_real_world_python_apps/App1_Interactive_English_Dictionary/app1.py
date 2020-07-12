import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8))>0:
        yn = input('Did you mean %s instead? Enter Y if yes, or N if no: ' % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == 'N':
            return 'The word DNE, pls dbcheck it.'
        else:
            return "We didn't understant your entry."
    else:
        return 'The word DNE, pls dbcheck it.'

# print(SequenceMatcher(None,'rainn','rain').ratio())

# print(get_close_matches('rainn', data.keys(), n=1))

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output: 
        print(item)
else:
    print(output)