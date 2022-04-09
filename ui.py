from tkinter import *

THEME_COLOR = "#375362"

FONT = ("Arial", 20, "italic")


class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text=f"Score: {0}", fg="white")
        self.score.config(bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, text="Hello", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img)
        self.true_button.config(padx=100, pady=100, highlightthickness=0, bd=0)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img)
        self.false_button.config(padx=100, pady=100, highlightthickness=0, bd=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
