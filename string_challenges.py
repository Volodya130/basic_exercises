# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])
print('#########')
# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.upper().count('А'))
print('#########')

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
letters = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]

counter = 0

for let in word.lower():
    if let in letters:
        counter += 1
print(counter)
print('#########')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split(" ")))
print('#########')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???

words = sentence.split(" ")
for word in words:
    print(word[0])
print('#########')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???

new_list = sentence.split(' ')
count = len(new_list)
length = 0
for word in new_list:
    length += len(word)
print(length/count)
print('#########')