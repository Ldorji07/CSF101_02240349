import re

def clean_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
        
            cleaned_line = re.sub(r'\b[A-Za-z0-9]+\b', '', line) 
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line) 
            cleaned_line = cleaned_line.strip()  
            outfile.write(cleaned_line + '\n')


input_file = 'dictionary.txt'  
output_file = 'cleaned_file.txt'    

clean_file(input_file, output_file)