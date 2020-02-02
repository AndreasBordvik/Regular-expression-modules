#!/usr/bin/env python3
import argparse
import re


"""
The script is highlighting text based on regex pattern, and
colors the pattern match with a color.
"""


def __readRegexFromFile(inFile):
    """Function for reading a syntax file containing regex's

    Args:
        - inFile (String): File location as string
    Returns:
        - dictionary (dict): A dictionary with common regex
          desctription as key, and regex as value
    """
    dictionary = {}
    with open(inFile) as file:
        line = file.readline().strip()
        while line:
            # Splitter opp hvert element på en linje,
            # og legger de key og val
            (val, key) = line.split(": ")
            dictionary[key] = val
            line = file.readline().strip()
    return dictionary


def __readColorFromFile(inFile):
    """Function for reading a syntax file containing regex's

    Args:
        - inFile (String): File location as string
    Returns:
        - dictionary (dict): A dictionary with common color
          desctription as key matching the regex, and the
          color code as value
    """
    dictionary = {}
    with open(inFile) as file:
        line = file.readline().strip()
        while line:
            (key, val) = line.split(": 0;")
            dictionary[key] = int(val)
            line = file.readline().strip()
    return dictionary


def __regexAndColors(syntax, theme):
    """Function for joing regex and matching color code
        in one common list

    Args:
        - syntax (String): File location as string for the regex file
        - theme (String): File location as string for the theme file
    Returns:
        - regxColList (list): A 2-dim list containing regex at index 0,
          and color code at index 1.
    """
    regex = __readRegexFromFile(syntax)
    color = __readColorFromFile(theme)
    regxColList = []
    for key, value in regex.items():
        if key in color:
            regxColList.append([value[1:-1], color[key]])
    return regxColList


def __readTextFromFile(filename):
    """Function for reading a text file containing text to highlight
    Args:
        - filename (str): File location as string for the text file.
    Returns:
        - text (str): The whole text file as a string
    """
    with open(filename) as file:
        text = file.read()
    return text


def __collectMatches(regxAndColorList, text):
    """Function for collection matches in text based on regex.
        Args:
            - regxAndColorList (list): List containing all regexes and colorcode
            - text (str): The string to look for matches in
        Returns:
            - matches (dict: Dictionary containg start index of match as key,
              and a list of match end index, colorcode, and matching group.
    """
    matches = {}
    for element in regxAndColorList:
        regex = element[0]
        colorCode = element[1]
        for match in re.finditer(regex, text, re.MULTILINE):
            if match:
                if (len(match.groups()) < 1):  # ingen grupper
                    if not matches.get(match.start(0)):
                        matches[match.start(0)] = \
                            [match.end(0), colorCode, match.group(0)]
                    else:
                        matches[match.start(0)].append(
                            [match.end(0), colorCode, match.group(0)])
                        # print("Start time for a match occurs two times")
                else:
                    for i in range(1, len(match.groups())+1):
                        if matches.get(match.start(i)) is None:
                            matches[match.start(i)] = \
                                [match.end(i), colorCode, match.group(i)]
                        else:
                            matches[match.start(i)].append(
                                [match.end(i), colorCode, match.group(i)])
                            # print("Start time for a match occurs two times")
    return matches


def highlighter(regxAndColorList, text):
    """Function that highlight(color formating) text in a file based on
    regex and color codes.
        Args:
            - regxAndColorList (list): List containing all regexes and colorcode
            - text (str): The string to look for matches in
        Returns:
            fullText, matchedText, matchedTextUncolored (tuple):

            - fulltext (str):
              the whole text highlighted based on regex and colorcodes.

            - matchedText (str):
              only the lines where a regex got a match in the text
              (used for grep).

            - matchedTextUncolored (str):
              Same as matchedText but not with colored text.
    """
    coloringIndex = 0
    fullText = ""
    matchedText = ""
    matchedTextUncolored = ""
    matches = __collectMatches(regxAndColorList, text)
    for key in sorted(matches.keys()):
        start = key
        stop = matches[key][0]
        colorCode = matches[key][1]
        matchText = matches[key][2]

        # Handling edge case where the first match coloring
        # is not index 0 of text
        if (coloringIndex == 0 and start > 0):
            fullText += text[0:start]
            if (len(matches) > 0):
                matchedText += text[0:start]
                matchedTextUncolored += text[0:start]
            coloringIndex = start
        if (coloringIndex <= start):
            fullText += text[coloringIndex:start]
            if (len(matches) > 0):
                matchedText += text[coloringIndex:start]
                matchedTextUncolored += text[coloringIndex:start]
            if(not colorCode):
                fullText += matchText
            else:
                matchedTextUncolored += matchText
                matchText = f"\x1b[{colorCode}m" + matchText + "\x1b[0m"
                fullText += matchText
                matchedText += matchText
                coloringIndex = stop

    # Handling edge case at the end after last match coloring
    if(coloringIndex < len(text)):
        if(len(matches) > 0):
            matchedText += text[coloringIndex:]
            matchedTextUncolored += text[coloringIndex:]
        fullText += text[coloringIndex:]
    return fullText, matchedText, matchedTextUncolored


def main():
    """The main function uses argparser to get arguments. Feeds the highlighter
        with arguments and print out the result (color code formated text).
        Arguments are described in help.
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('regex', type=str,
                           help='Regex syntax file')
    argparser.add_argument('code', type=str,
                           help='Color theme file')
    argparser.add_argument('text', type=str,
                           help='Textfile to apply highlight on')
    args = argparser.parse_args()
    regxAndColorsList = __regexAndColors(args.regex, args.code)
    text = __readTextFromFile(args.text)

    fullText, matchedText, matchedTextUncolored = \
        highlighter(regxAndColorsList, text)
    print(fullText)


if __name__ == '__main__':
    main()
