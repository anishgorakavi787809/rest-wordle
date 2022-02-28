from datetime import *
import requests
import json
from random_word import RandomWords
from str2int import str2int

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

        year = 0
        month = 0
        day = 0
        date_list = str2int(str(date.today()))

        print(date_list)
        counter = 1
        for l in date_list:
            if counter == 1:
                year = l
            if counter == 2:
                month = abs(int(l))
            else:
                day = abs(int(l))
            counter += 1
            
        file = open(self.json_file,"w")
        constructed = {
            "year": year,
            "month":month,
            "day":day,
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
        yellow = []
        green = []
        gray = []
        
        for index in user_input:
            if index == one:
