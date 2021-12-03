import json
import os
import re

filepath = "data_paper.json"
genpath = "./generated/paper_survey"
fopen = open(filepath, "r")
json_dict = json.load(fopen)

def pick_parentheses(line):
    paren_count = 0
    for char in line:
        if char == "[":
            paren_count += 1
        elif char == "]":
            paren_count -= 1
        if paren_count == 1:
            line[]
    return 

def convert(string):
    pattern = r"\[(.*?)\]"
    while True:
        match = re.search(pattern, string)
        if match:
            res_str = match.group()
            print(res_str)
            if res_str.startswith("[* "): # bold
                res_str = res_str.replace("[* ", "**")
                res_str = res_str.replace("]", "**")
            elif res_str.startswith("[_ "): # underline
                res_str = res_str.replace("[_ ", "<u>")
                res_str = res_str.replace("]", "</u>")
            elif res_str.startswith("[** "): # h3
                res_str = res_str.replace("[** ", "### ")
                res_str = res_str.replace("]", "")
            elif res_str.startswith("[*** "): # h2
                res_str = res_str.replace("[*** ", "## ")
                res_str = res_str.replace("]", "")
            elif res_str.startswith("[**** "): # h1
                res_str = res_str.replace("[**** ", "# ")
                res_str = res_str.replace("]", "")
            elif res_str.startswith("[/ "): # italic
                res_str = res_str.replace("[/ ", "*")
                res_str = res_str.replace("]", "*")
            elif res_str.startswith("[$ "): # math
                line
                res_str = res_str.replace("[$ ", "$")
                blacket_count = res_str.count("[") # 数式中の中括弧の数
                if blacket_count == 0:
                    res_str = res_str.replace("]", "$")
                    break
                else:
                    mathflag = True
            elif mathflag:
                
                mathflag = False
                res_str = res_str.replace("]", "$")
            elif res_str.startswith("[http"): # url
                url = res_str.strip("[").strip("]")
                res_str = "[" + url + "]" + "(" + url + ")"
                break
            else: # throw error
                return ValueError("Unrecognized format")
            string = string.replace(match.group(), res_str)
        else:
            break
    return string


def main():

    os.makedirs(genpath, exist_ok=True)

    for entry in range(len(json_dict["pages"])):
        title = "# " + json_dict["pages"][entry]["title"]
        lines = json_dict["pages"][entry]["lines"]
        del lines[0]
        
        with open(genpath + str(json_dict["pages"][entry]["title"]) + ".md", "w") as f:
            f.write("---\n")
            f.write("title: " + json_dict["pages"][entry]["title"] + "\n")
            f.write("---\n")
            for line in lines:
                f.write(convert(line) + "\n")
                f.write("\n")


if __name__ == "__main__":
    main()