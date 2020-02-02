#!/usr/bin/env python3
import argparse
import numpy as np
import sys
sys.path.append('../')


"""
The script is mimicking the linux diff. It uses a algorithm
for finding the Longest Common Subsequence. Based on info
about the Longest Common Subsequence the script prints what
is different between two input files. What is removed, added or
changed.
"""


def __writeDiffToFile(diffOut):
    """Function for writing the diff result to a text file.
    and prints out the diff result.
    Args:
        - diffOut (list): A list of all lines from the result
          of the diff algorithm.
    """
    with open("diff_output.txt", "w+") as out_file:
        for i in range(len(diffOut)):
            diff = diffOut.pop()
            out_file.write(diff)
            print(diff.rstrip())


def __writeSyntaxAndThemeToFile():
    """Function for writing/making a diff syntax file,
    and a diff theme file.
    """
    addedRegex = "\"^(\+.+)|(\+)$\"" + ": added"
    removedRegex = "\"^(\-.+)|(\-)$\"" + ": removed"

    with open("diff.syntax", "w+") as out_file:
        out_file.write(addedRegex + "\n")
        out_file.write(removedRegex + "\n")

    with open("diff.theme", "w+") as out_file:
        out_file.write("added: 0;" + str(92) + "\n")
        out_file.write("removed: 0;" + str(31) + "\n")

    print("\n diff syntaxt and theme are written to files")


def __readTextFromFile(filename):
    """Function for reading a text file containing text to highlight
    Args:
        - filename (str): File location as string for the text file.
    Returns:
        lines (list): A list of strings for all lines read in file
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines


def __lcsMatrix(original, changed):
    """Builds the longest common subsequence (lcs) matrix from
    the input original file and the changed file.
    Args:
        - original (list): A list of all lines from the original file
        - changed (list): A list of all lines from the changed file
    Returns:
        matrix (numpy array): longest common subsequence matrix/array
    """
    matrix = np.zeros((1+len(changed), 1+len(original)))
    for y in range(matrix.shape[0]-1):  # lines in original
        ym = y + 1
        for x in range(matrix.shape[1]-1):  # lines in changed
            xm = x + 1
            if (changed[y] == original[x]):
                diagonalValue = matrix[y][x]
                matrix[ym][xm] = diagonalValue + 1
            else:
                max_s_c = max(matrix[ym][xm - 1], matrix[ym - 1][xm])
                matrix[ym][xm] = max_s_c
    return matrix


def __lcsWithBacktracking(matrix, original, changed):
    """Backtracking along the lcs matrix to find the longest common
    subsequence of lines and stores it. Using info from the matrix to
    collect the correct lines (removed, added, or changed) from the two input
    files.

    Args:
        - matrix (numpy array): Longest common subsequence matrix/array
        - original (list): A list of all lines from the original file
        - changed (list): A list of all lines from the changed file
    Returns:
        lcs, lcsLength, diffResult (tuple):

        - lcs (str): A string representation of the longest common
          subsequence.

        - lcsLength (int): The length of the longest common subsequence

        - diffResult (list): The entire diff result line-by-line stored
          as strings in a list in the correct order.
          Index corresponds to line nb.
    """
    yp = matrix.shape[0] - 1
    xp = matrix.shape[1] - 1
    lcsLength = 0
    lcs = ""
    stack = []

    diffResult = []
    while True:
        left = matrix[yp][xp - 1]
        up = matrix[yp - 1][xp]
        if((yp < 1) or (xp < 1)):
            break
        if (left == up):
            if(matrix[yp][xp] == up):
                yp -= 1  # move up the matrix
                added = f"+ {changed[yp]}"
                if (changed[yp] == "\n"):
                    added = f"+ \n"
                addedInChange = added
                diffResult.append(addedInChange)
            else:
                common = original[xp-1]
                diffResult.append(f"0 {common}")
                stack.append(f"0 {common}")
                lcsLength += 1
                yp -= 1  # move diagonaly up the matrix
                xp -= 1  # move diagonaly up the matrix
        elif (left > up):  # move left the matrix
            xp -= 1
            removedFromoriginal = f"- {original[xp]}"
            diffResult.append(removedFromoriginal)
        elif (left < up):  # move up the matrix
            yp -= 1
            added = f"+ {changed[yp]}"
            if(changed[yp] == "\n"):
                added = f"+ \n"
            addedInChange = added
            diffResult.append(addedInChange)

    # Fixes the last corner case. End in x or y in matrix
    if(xp > 0):
        for i in range(xp):
            xp -= 1
            removedFromoriginal = f"- {original[xp]}"
            diffResult.append(removedFromoriginal)
    elif(yp > 0):
        for j in range(yp):
            yp -= 1
            added = f"+ {changed[yp]}"
            if (changed[yp] == "\n"):
                added = f"+ \n"
            diffResult.append(added)

    for j in range(len(stack)):
        lcs += stack.pop()
    return lcs, lcsLength, diffResult


def superdiff(originalFile, changedFile):
    """The function reads inn text from two files, and
    finds out what is differant/changed in the changed file.
    Finally it writes the differance to a output file.
    Args:
        - originalFile (str): File location as string for the
          original original file
        - changedFile (str): File location as string for the
          changed file
    """
    original = __readTextFromFile(originalFile)
    changed = __readTextFromFile(changedFile)
    matrix = __lcsMatrix(original, changed)
    lcs, lcsLength, diff = __lcsWithBacktracking(matrix, original, changed)
    __writeDiffToFile(diff)
    __writeSyntaxAndThemeToFile()


def main():
    """The main function uses argparser to get arguments.
    Feeds the superdiff function
    with arguments. Arguments are described in help.
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('originalFile', type=str,
                           help='File to check for changes against')
    argparser.add_argument('changedFile', type=str,
                           help='File to check for changes in')
    args = argparser.parse_args()
    superdiff(args.originalFile, args.changedFile)


if __name__ == '__main__':
    main()
