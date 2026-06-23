from pypdf import PdfReader
from pathlib import Path

def extract_text_from_pdf(file_name, get_rid_of_strings):

    """ the name of the function is self-explanatory
        - file_name is the name of pdf file from which we want to extract the text
            e.g. "Jokes.pdf" 
        - get_rid_of_strings is a list of strings we want to remove
            from extracted text """
    
    text = ''
    pdf = PdfReader(Path(file_name))

    for i in range(pdf.get_num_pages()):
        text += pdf.get_page(i).extract_text()

    for string in get_rid_of_strings:
        text = text.replace(string, '')

    return text

# test
# delete_list = ["One Liner Jokes"]
# print(extract_text_from_pdf("Jokes.pdf", delete_list))

