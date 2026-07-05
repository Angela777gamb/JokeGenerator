from tkinter.filedialog import test

from pypdf import PdfReader
from pathlib import Path
import re
import random
import math
import tkinter as tk
from collections import deque

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
    """ remove enumeration and split the text separated by enumeration """
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

# #YO MAKE ME A WINDOW
# root = tk.Tk()
# root.title("TheWillOfTheCity")
# #GET INFO RAHHH 
# root.configure(bg='black')
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# #ACTUALLY MAKE THE WINDOW 
# root.geometry(f'{screen_width}x{screen_height}')

# label = tk.Label(root, text=get_random_joke(parts), bg= 'black', fg= 'RoyalBlue3', font=("Helvetica", 24), wraplength = screen_width-100)
# label.place(relx=0.5, rely=0.5, anchor='center')
# button = tk.Button(root, text="Get New Joke", command=lambda: label.config(text=get_random_joke(parts)), font=("Helvetica", 16), bg='black', fg='RoyalBlue3', activebackground='black', activeforeground='RoyalBlue3', highlightbackground='black', highlightcolor='black', highlightthickness=0, bd=0)
# button.place(relx=0.5, rely=0.6, anchor='center')
# button.config(borderwidth=0, highlightthickness=0)
# glow = tk.Label(root, text="The will of the city", bg='black', fg='RoyalBlue3', font=("Helvetica", 12))
# glow.place(relx=0.5, rely=0.9, anchor='center')
# #KEEP MY SHI OPEN 
# root.mainloop()

class PulsingGlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prescript device")
        background_color = "black"
        self.root.configure(bg=background_color)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        root.geometry(f'{screen_width}x{screen_height}')

        self.glow_colors = ["royalblue", "royalblue1", "royalblue2", "royalblue3", "royalblue4", "royalblue3", "royalblue2", "royalblue1", "royalblue"]
        self.color_index = 0
        self.direction = 1  # 1 for brightening, -1 for dimming

        # Label widget
        self.label = tk.Label(root, text="get random joke(parts)", font=("Helvetica", 24), bg="black")
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.button = tk.Button(root, text="Get New Joke", command=lambda: self.label.config(text=get_random_joke(parts)), font=("Helvetica", 16), bg='black', fg='royalblue', activebackground='black', activeforeground='royalblue', highlightbackground='black', highlightcolor='black', highlightthickness=0, bd=0)
        self.button.place(relx=0.5, rely=0.6, anchor='center')
        glow = tk.Label(root, text="The will of the city", bg='black', fg='royalblue', font=("Helvetica", 12))
        glow.place(relx=0.5, rely=0.9, anchor='center')
        # addphoto = tk.PhotoImage(file="Index") 
        # self.tk.call('INDEX.png', 'iconphoto', root._w, addphoto)  # Set window icon
        # self.add_button = tk.Label(root, image=addphoto, command=self.add_joke, bg='black', activebackground='black', highlightbackground='black', highlightcolor='black', highlightthickness=0, bd=0)
        # self.add_button.image = addphoto  # Keep a reference to the image
        # self.add_button.place(relx=0.9, rely=0.1, anchor='center')
        # Start animation loop
        self.animate_glow()

    def animate_glow(self):
        # Update text color
        current_color = self.glow_colors[self.color_index]
        self.label.config(fg=current_color)

        # Reverse direction if we hit the gradient boundaries
        if self.color_index >= len(self.glow_colors) - 1:
            self.direction = -1
        elif self.color_index <= 0:
            self.direction = 1

        self.color_index += self.direction

        # Call this function again after 100 milliseconds
        self.root.after(100, self.animate_glow)

if __name__ == "__main__":
    root = tk.Tk()
    app = PulsingGlowApp(root)
    root.mainloop()

