from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

FONT = ("Arial", 20, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text=f"Score: {self.quiz.score}", fg="white")
        self.score.config(bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text="Hello", font=FONT, fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img)
        self.true_button.config(padx=100, pady=100, highlightthickness=0, bd=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img)
        self.false_button.config(padx=100, pady=100, highlightthickness=0, bd=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quiz_text,
                                   text=f"Game over!"
                                        f"\nYou scored {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.check_answer(self.quiz.check_answer(user_answer="True"))

    def false_answer(self):
        self.check_answer(self.quiz.check_answer(user_answer="False"))

    def check_answer(self, is_answer_correct: bool):
        if is_answer_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

