import json
dictCon = json.load(open("data.json"))

from difflib import get_close_matches

def wordDef(inpKey):
    inpKey = inpKey.lower()

    if inpKey in dictCon:

        return dictCon[inpKey] #This produces an output.

    elif inpKey.title() in dictCon:
        return dictCon[inpKey.title()]

    elif inpKey.upper() in dictCon:
        return dictCon[inpKey.upper()]

    elif len(get_close_matches(inpKey, dictCon.keys(), n=1, cutoff=0.8)):

        probWord = get_close_matches(inpKey, dictCon.keys(), n=1, cutoff=0.8)[0]

        ans = input("Did you mean {}? If Yes, type Y, if No, type N: ".format(probWord))

        ans = ans.lower()

        if ans == "y":
            return dictCon[probWord]
        elif ans == "n":
            return "Sorry your word could not be found!"
        else:
            return "We did not understand your query."
    else:

        return "Sorry your word could not be found!"

userWord = input("Enter a word to get its definition: ")

output = wordDef(userWord)

if type(output) == list:
    for item in output:
        print("\n" + item + "\n")
else:
    print(output)
