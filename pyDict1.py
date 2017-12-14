def wordDef(inpKey):
    inpKey = inpKey.lower()

    import json
    dictCon = json.load(open("data.json"))

    from difflib import get_close_matches

    if inpKey in dictCon:
        return dictCon[inpKey]
    elif len(get_close_matches(inpKey, dictCon.keys(), n=1, cutoff=0.8)):

        probWord = get_close_matches(inpKey, dictCon.keys(), n=1, cutoff=0.8)[0]

        ans = input("Did you mean {}? If Yes, type Y, if No, type N: ".format(probWord))

        if ans == "Y" or ans == "y":
            return dictCon[probWord]
        else:
            return "Sorry your word could not be found!"
    else:

        return "Sorry your word could not be found!"

userWord = input("Enter a word to get its definition: ")

print(wordDef(userWord))
