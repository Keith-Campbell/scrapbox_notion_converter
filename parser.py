import json
import os

filepath = "atshhandelssohn-54351265.json"
fopen = open(filepath, "r")
json_dict = json.load(fopen)

os.makedirs("./generated", exist_ok=True)

def convert(string):
        string = string.replace("[** ", "### ").replace("]", "") # h3
        string = string.replace("[*** ", "## ").replace("]", "") # h2
        string = string.replace("[**** ", "# ").replace("]", "") # h1
        string = string.replace("[* ", "**").replace("]", "**") # bold
        string = string.replace("[/ ", "*").replace("]", "*") # italic
        string = string.replace("[_ ", "<u>").replace("]", "</u>") # bold
        string = string.replace("[$ ", "$").replace("]", "$") # math
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
