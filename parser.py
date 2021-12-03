import json
import os
import re

filepath = "data.json"
fopen = open(filepath, "r")
json_dict = json.load(fopen)

os.makedirs("./generated", exist_ok=True)

def convert(string):
    pattern = r"\[(.*?)\]"
    while True:
        match = re.search(pattern, string)
        if match:
            res_str = match.group().replace("[", "")
            if res_str.startswith("* "): # bold
                res_str = res_str.replace("* ", "**")
                res_str = res_str.replace("]", "**")
            if res_str.startswith("_ "): # underline
                res_str = res_str.replace("_ ", "<u>")
                res_str = res_str.replace("]", "</u>")
            if res_str.startswith("** "): # h3
                res_str = res_str.replace("** ", "### ")
                res_str = res_str.replace("]", "")
            if res_str.startswith("*** "): # h2
                res_str = res_str.replace("*** ", "## ")
                res_str = res_str.replace("]", "")
            if res_str.startswith("**** "): # h1
                res_str = res_str.replace("**** ", "# ")
                res_str = res_str.replace("]", "")
            if res_str.startswith("/ "): # italic
                res_str = res_str.replace("/ ", "*")
                res_str = res_str.replace("]", "*")
            if res_str.startswith("$ "): # math
                res_str = res_str.replace("$ ", "$")
                res_str = res_str.replace("]", "$")
            string = string.replace(match.group(), res_str)
            print(string)
            input()
        else:
            break
        return string

for entry in range(len(json_dict["pages"])):
    title = "# " + json_dict["pages"][entry]["title"]
    lines = json_dict["pages"][entry]["lines"]
    
    with open("./generated/page" + str(entry) + ".md", "w") as f:
        f.write(title + "\n")
        for line in lines:
            line = convert(line)
            f.write(line + "\n")
            f.write("\n")
