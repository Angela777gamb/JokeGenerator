""" remove 'One Liner Jokes' strings from the text 
    and break the result to its enumerated parts """

import re
from pathlib import Path

# This pattern matches one or more digits and following '.'
pattern = r"\d+\."

fname = input("filename: ")
path = Path(fname)
contents = path.read_text("utf-16")
contents = contents.replace('One Liner Jokes', '')
matches = re.split(pattern, contents)
for item in matches:
    print(item.lstrip())
