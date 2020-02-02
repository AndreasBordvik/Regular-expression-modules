# Assignment 5 - IN4110
#### By David Andreas Bordvik

### Summary: Assignment5 contains modules for a highlighting, grep and diff that are based on regex. 

### Scripts:
* `highlighter.py`: Regex based highlighting of file based on syntax and theme files.
* `grep.py`: Finding words or regex-expressions in files.
* `diff.py`: Printing differences between two files.



### 5.1 - Highlighter:
The script is highlighting contents in a file based on regex patterns, and
colors the text based on pattern match.


#### Usage:
The highlighter takes three arguments:
- A Regex syntax file for patterns of where to highlight.
- A Colorcode file (theme file). Each regex pattern has its own colorcode.
- The text file to apply highlight on.

For help on how to run the script:
`python3 highlighter.py -h`

Example usage:
`python3 highlighter.py <syntaxfile> <themefile> <textfile to highlight>`


### 5.2 - Python syntax:
Two demo files are are included for testing the highlighter. 

Run python demo files:
`python3 highlighter.py python.syntax python.theme python_demo1.py`,
`python3 highlighter.py python.syntax python.theme python_demo2.py`

Alternatively run the highligther using the second theme file called python2.theme

##### Python syntax (python.syntax) and theme (python.theme(2)) files content:
The files contain regex (syntax) and colorcodes (theme files) for the following:
- comment
- multi-line-comment
- for
- elif
- if-else
- in
- def
- class
- string
- import
- while
- def-name
- True-False-None
- try-except
- return
- decorator
- from
- range


### 5.3 - Java syntax:
Run the java demo file:
`python3 highlighter.py java.syntax java.theme java_demo1.java`


### 5.4 - Grep:
The script is mimicking the grep in linux. It searches for spesific
text within a text file and returns the lines that matches the
regex or search pattern from the input arguments. 


#### Usage:
The grep requires two arguments, and has two extra optional:
- Optional flag 1: `--highlight` Colors the text where the pattern is matching
- Optional flag 2: `-n` Displays the line number within the text where for the search match.
- One search word or regular expressions, or an arbitrary number of patterns.
- A text file to search for matches in.

For help on how to run the script:
`python3 grep.py -h`


Example usage:
`python3 grep.py --highlight -n simple hello.ny`,
`python3 grep.py --highlight -n "is" "(?<=print\().+(?=\))" "NNNN\s" "(stat.+?\s)" hello.ny`





### 5.5 - Diff:
The script is mimicking the linux diff, and it uses the Longest Common Subsequence 
algorithm (implemented from scratch). Based on the Longest Common Subsequence 
the script prints differences between the two input files. What is removed, added,
changed, or common.


#### Usage:
The grep requires two arguments. When run the diff script and prints the differences 
and writes the difference to a output file (diff_output.txt). It also writes one file 
for syntax/regex and one file for theme(color codes). 
Arguments:
- The original source file.
- A modified version of the original source file.

For help on how to run the script:
`python3 diff.py -h`

General example on usage:
`python3 diff.py <original file> <modified version>`


Multiple original and changed files are added to the assignment folder.
Example usage:
`python3 diff.py diff_original0.txt diff_changed0.txt`, 
`python3 diff.py diff_original1.txt diff_changed1.txt`, 
`python3 diff.py diff_original2.py diff_changed2.py`


### 5.6 - Coloring diff:
The diff script outputs a diff.syntax, diff.theme, and diff_output.txt.
These three files can be used with the highligter script from 5.1 to 
color the diff.


Usage:
`1: Run diff.py on two files`, 
`2: Use the output from diff.py with highlighter.py`


Example usage:
`python3 diff.py diff_original1.txt diff_changed1.txt`, 
`python3 highlighter.py diff.syntax diff.theme diff_output.txt`