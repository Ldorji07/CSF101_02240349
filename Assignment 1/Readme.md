# Dzongkha Spell Checker

## Project Overview
This project targets developing a spell checker that will recognize and report spelling mistakes in the Dzongkha dictionary.txt. The program will use a input.txt file that reads Dzongkha words given by respected sir and checks them against entries from dictionary.txt and specifies which words are misspelled together with their position such as the line number and the word position.

## Table of Contant 
- [Usage]
- [Implementation Details]
- [Data Structures]
- [Algorithms]
- [Challenges and Solutions]
- [Future Improvements]
- [References]

## Usage
1. Prepare Files:
- Dictionary.txt: This file should contain a cleaned list of correct Dzongkha words, one word per line. We have been Provied with dictionary.docx which cannot be read by in python so to convrt into txt i have to install pip3 install docx2txt. This Python code uses the docx2txt library to convert a .docx file into a plain text file. It imports the module, defines the input (dictionary.docx) and output (dictionary.txt) file paths, and uses docx2txt.process() to extract the text from the Word document. The extracted text is then written to the output file, and a confirmation message is printed upon successful conversion.
- Input.txt: This is the input file with Dzongkha text that had been send by sir using our last 3 number to check spelling. Each line can contain multiple words and some of which may have spelling errors. so i have used some code where i have to requred install pip3 install requests to run the code which is used for making HTTP requests in Python.

2. Save the Code:
Save the Python code for the Dzongkha spell checker in a file named dzongkha_spell_checker.py.
I have made the code comparing the two file and finding the difference word which is not in the dictionary.txt and making it as an incorrect word.

3. Review the Output:
The program will compare each word in Input.txt against the valid Dzongkha words in dictionary.txt.
If any word is incorrect, it will print a message indicating the line number, word and is incorrect word.

...bash
python dzongkha_spell_checker.py input_file.txt
 ...

## Implementation Details
- Downloading the Dictionary.docx and after downloading the docx i have to convert it into .txt file so it can read it at python so for that i have to install docx2txt application at terminal which helps to extarxt words form docx to txt. and after installing i have import the application and used file oppreation method 
- Downloding input file from URL to do that again i have to install pip3 requests application where it helps to requests to run the code which is used for making HTTP requests in Python. and i used the same method to run my code.
- And Cleaning English word from dictionary.txt and creating new output.txt file 
- And lastly Creating spell checker by comparing two txt file and finding the difference between the txt file and running it as an incorrect word by showing line number and the word 

## Data Structure
- spelling_checker.py
Set: For storing unique reference words from the cleaned dictionary for fast lookup.
List: For holding words extracted from each line of the input file during iteration.
String: For handling and processing the lines read from the input file.

- docx-txt conveter.py
Strings: For storing file names and the content extracted from the .docx file.

- txt input.py
Strings: For storing the URL and the text content of the HTTP response.

- cleaner.py
Strings: For storing file names and the content of each line from the input file.

## Algorithms
Checks for incorrect words by loading unique words from cleaned_file.txt into a set called reference_words for quick lookups. It processes the input file downloaded_file.txt line by line, checking each word against this set. If a word isn’t found, it’s marked as incorrect, and the algorithm prints the line number and the wrong word, helping to find spelling errors in the Dzongkha text.

## Performance Analysis 
- The Dzongkha spell checker processes files with a time complexity of O(n * m), where it checks each word against the dictionary, which is stored in a set for quick lookups. Its space usage is O(k) for the dictionary and O(n) for the input file. While it works well for most cases, it may slow down with larger files, so using buffered reading could help. Future improvements could include real-time checking and better handling of larger texts.

## Challenges and solutions
- Challenge: Handling Non-English Characters
Dzongkha uses its own script, making it challenging to process and clean the data, as typical tools are more suited for languages like English.

- Solution:
Ensure that text processing supports UTF-8 encoding to correctly handle Dzongkha characters. Use Python's built-in file handling functions with the utf-8 encoding to process the files without losing character integrity.

- Challenge: Converting DOCX to TXT
The dictionary.docx needs to be converted to a clean text file for use in the spell checker. Handling this conversion while ensuring that special formatting, noise, and unnecessary text are removed is a key issue.

- Solution:
Use libraries like docx2txt to convert DOCX files to text and process the text file by removing English words and number using regular expressions (re application).

- Challenge: Real-Time Error Reporting
Identifying incorrect words along with their positions and line numbers tracking to ensure the output is accurate.

- Solution:
Use Python's enumerate() function to track line numbers and word positions while processing the text.

## Future Improvements
- Grammar Checking
Extend the functions beyond spell checking to include grammar checks, ensuring proper sentence structure and syntax in Dzongkha text.
- Enhanced Dictionary
Expanding the dictionary to include more words, slang, and regional variations in Dzongkha would improve the spell checker's accuracy.

## References
-Youtube => https://www.youtube.com/watch?v=Mi3j54ZMxOc&pp=ygUkaG93IHRvIGNvbnZlcnQgZG9jeCB0byB0eHQgaW4gcHl0aG9u
         
=> https://www.youtube.com/watch?v=FNOpWah3saA&pp=ygUkaG93IHRvIGNvbnZlcnQgdXJsIHRvIHR4dCAgaW4gcHl0aG9u

=> https://www.youtube.com/watch?v=uPT-LkYSP_o&pp=ygUcZGVmIGZ1bmN0aW9uIHVzaW5nIGVudW1lcmF0ZQ%3D%3D

-git book (UNIT 2)

-w3 School

-Chat GPT
