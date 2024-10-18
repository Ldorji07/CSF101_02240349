def compare_files(ref_file, inp_file):
    ref_words = set(open(ref_file).read().split())
    for line_num, line in enumerate(open(inp_file), start=1):
        for word in line.split():
            if word not in ref_words:
                print(f"Line {line_num}, Word '{word}' is incorrect")

compare_files('cleaned_file.txt', 'downloaded_file.txt')
