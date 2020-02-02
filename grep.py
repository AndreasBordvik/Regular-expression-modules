#!/usr/bin/env python3
import argparse
from highlighter import highlighter

"""
The script is mimicking linux grep. It searches for specific
text within a string and returns the lines that matches the
regex or search pattern comming from input arguments.
"""


def grep(regex, highlight, textFile, addLines):
    """Function mimicking grep in linux. It searches for specific
    text within a string and returns the lines that matches the
    regex or search pattern comming from input arguments.

    Args:
        - regex (String or list of strings): A single regex string, or a list
        of several regex strings.
        - highlight (boolean): True will color the text matching the
        regex.
        - textFile (str): File location as string for the text file
        to search within.
        - addLines (boolean): True will display/print which line
        that matches the regex.

    Returns:
        - grepText (str): A string of the grep result.
    """
    regxAndColorsList = []
    grepText = ""
    text = ""

    regxAndColorsList = list(zip(regex, range(31, 31+len(regex))))

    for lines, lineTxt in enumerate(open(textFile).readlines(), 1):
        line = f"\x1b[36m{lines}:\x1b[0m "
        fullText, matchedText, matchedTextUncolored = \
            highlighter(regxAndColorsList, lineTxt)
        if(addLines):
            fullText = f"{line}{fullText}"
            text += fullText
            if(matchedText != ""):
                matchedText = f"{line}{matchedText}"
                matchedTextUncolored = f"{line}{matchedTextUncolored}"
                grepText += matchedText if highlight \
                    else matchedTextUncolored
        else:
            grepText += matchedText if highlight else matchedTextUncolored
            text += fullText
    return grepText


def main():
    """The main function uses argparser to get arguments. Feeds the grep function
        with arguments and print out the grep result.
        Arguments are described in help.
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--highlight",
                           help="Color the matching parts of the grep",
                           action="store_true")
    argparser.add_argument("-n", "--linenumber",
                           help="Display line number",
                           action="store_true")
    argparser.add_argument('regex', nargs='+', type=str,
                           help='Regex to match for grep')
    argparser.add_argument('textfile', type=str,
                           help='textfile to find matches in')
    args = argparser.parse_args()
    grepText = grep(args.regex, args.highlight, args.textfile, args.linenumber)
    print(grepText)


if __name__ == '__main__':
    main()
