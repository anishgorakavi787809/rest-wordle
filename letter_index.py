class letterIndex:
    def __init__(self,char):
        self.char = char

    def lower_prev(self):

        prev_letters_lower = {
        "b":"a",
        "c":"b",
        "d":"c",
        "e":"d",
        "f":"e",
        "g":"f",
        "h":"g",
        "i":"h",
        "j":"i",
        "k":"j",
        "l":"k",
        "m":"l",
        "n":"m",
        "o":"n",
        "p":"o",
        "q":"p",
        "r":"q",
        "s":"r",
        "t":"s",
        "u":"t",
        "v":"u",
        "w":"v",
        "x":"w",
        "y":"x",
        "z":"y"
        }
        vars = ""
        try:
            vars = prev_letters_lower[self.char]
        except:
            vars = "error: from the range from b to z "
        return vars

    def upper_prev(self):


        prev_letters_upper = {
        "B":"A",
        "C":"B",
        "D":"C",
        "E":"D",
        "F":"E",
        "G":"F",
        "H":"G",
        "I":"H",
        "J":"I",
        "K":"J",
        "L":"K",
        "M":"L",
        "N":"M",
        "O":"N",
        "P":"O",
        "Q":"P",
        "R":"Q",
        "S":"R",
        "T":"S",
        "U":"T",
        "V":"U",
        "W":"V",
        "X":"W",
        "Y":"X",
        "Z":"Y"
        }
        vars = ""
        try:
            vars = prev_letters_upper[self.char]
        except:
            vars = "error: from the range from B to Z "
        return vars
    def lower_next(self):
       next_letter_lower = {
           "a":"b",
           "b":"c",
           "c":"d",
           "d":"e",
           "e":"f",
           "f":"g",
           "g":"h",
           "h":"i",
           "i":"j",
           "j":"k",
           "k":"l",
           "m":"n",
           "n":"o",
           "o":"p",
           "p":"q",
           "q":"r",
           "r":"s",
           "s":"t",
           "t":"u",
           "u":"v",
           "v":"w",
           "w":"x",
           "x":"y",
           "y":"z"
       }
       vars = ""
       try:
            vars = next_letter_lower[self.char]
       except:
            vars = "error: from the range from B to Z "
       return vars

def upper_next(self):
    next_letter_upper = {
           "A":"B",
           "B":"C",
           "C":"D",
           "D":"E",
           "E":"F",
           "F":"G",
           "G":"H",
           "H":"I",
           "I":"J",
           "J":"K",
           "K":"L",
           "M":"N",
           "N":"O",
           "O":"P",
           "P":"Q",
           "Q":"R",
           "R":"S",
           "S":"T",
           "T":"U",
           "U":"V",
           "V":"W",
           "W":"X",
           "X":"Y",
           "Y":"Z"
       }
    vars = ""
    try:
            vars = next_letter_upper[self.char]
    except:
            vars = "error: from the range from B to Z "
    return vars