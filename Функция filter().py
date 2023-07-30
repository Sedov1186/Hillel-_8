input = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
word = lambda word: word.lower() == word.lower()[::-1]
words_of_polydromes = list(filter(word, input))
print(words_of_polydromes)
