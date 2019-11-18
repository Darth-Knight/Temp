
import re
from turtledemo.penrose import f

log_file_path = "/Users/rakshitchoudhary/Downloads/auth.log"
regex = 'example-server sshd\[[0-9]*\]'
read_line = True

string = 'Apr 29 06:56:48 example-server sshd[38254]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=123.183.209.132  user=root'
string = 'Failed password for root from 122.226.181.164 port 55720 ssh2'

def temp_function():
    date = string[0:6]
    if re.finditer("Failed password", string, re.S):
        if re.finditer("root", string, re.S):
            print(re.split("root from ", string)[1].split('port')[0])
        print(date)
        print(re.split(regex,string))

def logger_function():
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                print(line)
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
temp_function()


