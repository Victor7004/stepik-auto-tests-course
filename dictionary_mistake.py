dictionary = set()
#создаем два словаря
dictionary_lower = set()
for _ in range(int(input())):
    word = input()
    dictionary.add(word)
    dictionary_lower.add(word.lower())
sentence = input().split()
mistake = 0
for word in sentence:
    if (word not in dictionary and word.lower() in dictionary_lower) or (word not in dictionary and word == word.lower()) or len([letter for letter in word if letter == letter.upper()]) > 1:
        mistake += 1
print(mistake)   
