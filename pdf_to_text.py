import pymupdf

def pdf_to_text(pdf_file_name, txt_file_name = None):
    """ Read a pdf file and convert it to the text file. 
        If the second parameter is missing, the output goes to the string """

    try:
        doc = pymupdf.open(pdf_file_name)           # open pdf file
    except:
        return "Can't open: " + pdf_file_name
    plain_text = ''
    if txt_file_name:
        out = open(txt_file_name, "wb")         # open output text file
    for page in doc:                            # iterate the document pages
        text = page.get_text().encode("utf_16", "ignore") 
        if txt_file_name:    
            out.write(text)                     # write text of page
        else:
            # append page to the string
           plain_text += text.decode("utf_16", "ignore") 
    if txt_file_name:
       out.close()
    return plain_text    
    

# test
# pdf_file_name = input('pdf file name: ')
# txt_file_name = input('txt file name: ')
# print(pdf_to_text(pdf_file_name, txt_file_name))
# print('done')
