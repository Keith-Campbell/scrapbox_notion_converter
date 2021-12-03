import json
import os
import re

filepath = "data_paper.json"
genpath = "./generated/paper_survey/"
fopen = open(filepath, "r")
json_dict = json.load(fopen)

def outer_parent(string):
    string = string.replace("[$ ", "$")
    paren_count = 0
    char_count = 0
    for char in string:
        print(char + ", str: " + string)
        if char == "[":
            paren_count += 1
        elif char == "]":
            print("paren_count: " + str(paren_count))
            if paren_count != 0:
                paren_count -= 1
            elif paren_count == 0:
                string = string[:char_count] + "$" + string[char_count+1:]
                break
            else:
                raise ValueError("Unmatched parenthesis")
        char_count += 1
    return string

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
                _string = outer_parent(string)
                #res_str = re.search(r"\$(.*?)\$", _string).group()
                return string.replace(string, _string)
            elif res_str.startswith("[http"): # url
                url = res_str.strip("[").strip("]")
                res_str = "[" + url + "]" + "(" + url + ")"
                break
            else:
                res_str = res_str.replace("[", "")
                res_str = res_str.replace("]", "")
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