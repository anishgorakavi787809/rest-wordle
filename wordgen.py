
from datetime import *
import requests
import json
from random_word import RandomWords


class worldle_logic:
    def __init__(self,json_file:str):
        self.json_file = json_file

    def generate_words_json(self,count_day:int) -> str:
        list_of_words = []
        counter = 1
        r = RandomWords()
        while counter <= count_day:
          word_data = r.get_random_word(minLength=5, maxLength=5)
          if word_data == None or word_data == "None":
              continue
          if word_data.isspace():
              continue
          
          print(word_data.lower())
          list_of_words.append(word_data.lower())
          counter += 1 

      
        file = open(self.json_file,"w")
        constructed = {
            "year": date.today().year,
            "month":date.today().month,
            "day":date.today().day,
            "words":list_of_words
        }
        json.dump(constructed,file)

        print("Made list of wordle words")

    def get_word_day(self) -> str:
        with open(self.json_file) as file:
            data = json.load(file)
            file_date = date(int(data["year"]),int(data["month"]),int(data["day"]))

            today_date = date(date.today().year,date.today().month,date.today().day)
            diff = today_date - file_date
            return data["words"][diff.days]
          
    def letter_find(self, user_input:str):
      
        word_of_day = self.get_word_day()
        one = word_of_day[0]
        two = word_of_day[1]
        three = word_of_day[2]
        four = word_of_day[3]
        five = word_of_day[4]
        yellow = {}
        green = {}
        gray = {}
        vars = [False,False,False,False,False]
        char_index = 1
        with open("allowed-words.json") as file:
            data = json.load(file)
            if not user_input in data["words"]:
                return {"error":"Invaild word"}
        for index in user_input :

            if index == one and not vars[0]:
              if char_index == 1:
                  green[f"char {char_index}"] = index
                  char_index += 1
                  vars[0] = True
                  continue
              else:
                  yellow[f"char {char_index}"] = index
                  char_index += 1
                  continue

            if index == two and not vars[1]:
                if char_index == 2:
                      green[f"char {char_index}"] = index
                      char_index += 1
                      vars[1] = True
                      continue
                else:
                    yellow[f"char {char_index}"] = index
                    char_index += 1
                    continue

            if index == three and not vars[2]:
                if char_index == 3:
                      green[f"char {char_index}"] = index
                      char_index += 1
                      vars[2] = True
                      continue
                else:
                    yellow[f"char {char_index}"] = index
                    char_index += 1
                    continue

            if index == four and not vars[3]:
                if char_index == 4:
                      green[f"char {char_index}"] = index
                      char_index += 1
                      vars[3] = True
                      continue
                else:
                    yellow[f"char {char_index}"] = index
                    char_index += 1
                    continue
            
            if index == five and not vars[4]:
                if char_index == 5:
                      green[f"char {char_index}"] = index
                      char_index += 1
                      vars[0] = True
                      continue
                else:
                    yellow[f"char {char_index}"] = index
                    char_index += 1
                    continue
            gray[f"char {char_index}"] = index
            char_index += 1
            continue
        constructed = {
        "green":green,
        "yellow":yellow,
        "gray":gray
       }
        return constructed