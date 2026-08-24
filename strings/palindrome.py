

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


words = ["madam", "level", "python", "racecar"]

for word in words:
    if is_palindrome(word):
        print(word, "-> Palindrome")
    else:
        print(word, "-> Not a palindrome")



word = "Nivetha"

if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
