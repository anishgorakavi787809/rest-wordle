from pyparsing import Word
from wordgen import worldle_logic

x = worldle_logic("words.json")
print(x.letter_find("pinto"))