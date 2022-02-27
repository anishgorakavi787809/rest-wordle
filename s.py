from str2int import str2int
from wordgen import worldle_logic

lol = worldle_logic("words.json")
x = lol.get_word_day()
x = x.translate({ord('"'): None})
print(list(x))

