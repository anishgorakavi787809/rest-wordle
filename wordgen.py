from datetime import *
import requests
import json
from str2int import str2int

class worldle_logic:
    def __init__(self,json_file):
        self.json_file = json_file

    def generate_words_json(self,count_day:int):
        list_of_words = []
        counter = 1

        while counter <= count_day:
          word_data = requests.get("https://random-word-api.herokuapp.com/word?number=1")
          word_data = word_data.text.strip("[]")
          list_of_words.append(word_data)
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

        return "Made list of wordle words"

    def get_word_day(self):
        with open(self.json_file) as file:
            data = json.load(file)
            file_date = date(int(data["year"]),int(data["month"]),int(data["day"]))

            today_date = date(date.today().year,date.today().month,date.today().day)
            diff = today_date - file_date
            return data["words"][diff.days]