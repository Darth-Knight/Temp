
import re
from turtledemo.penrose import f

log_file_path = "/Users/rakshitchoudhary/Downloads/auth.log"
regex = '(<property name="(.*?)">(.*?)<\/property>)'
read_line = True

def logger_function():
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print
                    match_text
        else:
            data = f.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    file.close()

def myfun():
    print("hello")


myfun()
logger_function()


