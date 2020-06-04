import re
import argparse

def update(header, paragraph, text):
    new_div = "<!-- ADD After THIS -->\n<div class='view'>\n<h3 class='head'>"+header+"</h3>\n"
    new_div += "<p class='para'>"+paragraph+"</p>\n"
    newText = re.sub("<!-- ADD After THIS -->", new_div+"</div>\n", text)

    with open("index.html", 'w') as file:
        file.write(newText)

def main():
    with open("index.html", 'r') as file:
        text = file.read()

    with open("blog.txt", 'r') as blog:
        paragraph = blog.read()

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="header", help="the header", type=str, required=True)
    args = parser.parse_args()

    update(args.header, paragraph, text)

if __name__ == '__main__':
    main()
