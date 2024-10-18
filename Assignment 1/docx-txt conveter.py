import docx2txt as d2t

docxfile='dictionary.docx'
txtfiles='dictionary.txt'

doc=d2t.process(docxfile)

with open(txtfiles, 'w') as file:
    file.write(doc)

print('file converted Successfully')