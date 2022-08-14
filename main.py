BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient = "records")









window = Tk()
window.title("flash card project")
window.configure(background ="#B1DDC6", width= 2000, height = 2000, padx=50, pady = 50)




#======================================================================================================================#





                                         #Commands
def next_card():
    global current_card
    global current_word
    global current_eng
    canvas.itemconfig(front, image=card_front)
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    current_eng = current_card["English"]
    with open("data/user_data.txt", "r") as user_data:
        if current_word in user_data:
            next_card()
        else:
            canvas.itemconfig(language, text= "French" )
            canvas.itemconfig(word, text= f"{current_word}" )
            window.after(4000, flip_card)

def flip_card():
    canvas.itemconfig(front, image=card_back)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=f"{current_eng}")

def save_data():
    with open("data/user_data.txt", "a") as user_data:
        user_data.write(f"\n{current_word}")



#======================================================================================================================#
canvas = Canvas(width=800, height= 526)
canvas.configure(bg= BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file ="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
front = canvas.create_image(400,263, image = card_front,  )
canvas.grid(row = 0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic") )
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold") )

x_button_image = PhotoImage(file="images/wrong.png")
x_button = Button(image= x_button_image, highlightthickness=0)
x_button.grid(row=1, column=0, command = next_card())


check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image= check_button_image, highlightthickness=0, command=lambda: [save_data(), next_card()])
check_button.grid(row=1, column=1)


next_card()




window.mainloop()
