#!/usr/bin/env python3
import argparse
from highlighter import highlighter

"""
Demofile for testing out diff
"""
def function1(regex, textFile):
    """Function 1
    """
    grepText = ""
    lines = 1
    regxAndColorsList = list(zip(regex, range(31, 31+len(regex))))
    with open(textFile) as file:
        lineTxt = file.readline()
        while lineTxt:
            line = "\x1b[{}m".format(36) + f"{lines}:" + "\x1b[0m"
            if(addLines):
    return grepText

def function2():
	print("Hello World")

def main():
    """The main function
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('regex', nargs='+', type=str,
                           help='Regex to match for grep')
    argparser.add_argument('textfile', type=str,
                           help='textfile to find matches in')
    args = argparser.parse_args()
    grepText = function(args.regex, args.textfile)
    print(grepText)


if __name__ == '__main__':
    main()
