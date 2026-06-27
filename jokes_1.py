from tkinter.filedialog import test

from pypdf import PdfReader
from pathlib import Path
import re
import random
import math
import tkinter as tk

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

def text_to_parts(text):
    """ remove enumeration and split the text """
    parts = []
    # This pattern matches one or more digits and following '.'
    pattern = r"\d+\."
    matches = re.split(pattern, text)
    for item in matches:
        parts.append(item.strip())
    return parts

# test
remove_list = ["One Liner Jokes"]
text = extract_text_from_pdf("Jokes.pdf", remove_list)
parts = text_to_parts(text)


def get_random_joke(parts):
    """ return a random joke from the list of jokes """
    random.seed()
    return random.choice(parts)
print(get_random_joke(parts))

