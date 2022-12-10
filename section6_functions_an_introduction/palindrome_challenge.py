def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():  # hvis denne er True, dvs hvis vi har bokstav eller tall (dvs ikke et tegn)
            string += char  # så legges tallet eller bokstaven til
#    return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("{} is a palindorme".format(word))
else:
    print("{} is not a palindrome".format(word))
