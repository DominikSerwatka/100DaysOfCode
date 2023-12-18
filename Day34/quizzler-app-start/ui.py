from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#D0F288"
RED = "#DF826C"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)
        my_image_yes = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=my_image_yes, highlightthickness=0, command=self.yes_answer)
        self.button_yes.grid(column=0, row=2, pady=10)
        my_image_no = PhotoImage(file="images/false.png")
        self.button_no = Button(image=my_image_no, highlightthickness=0, command=self.no_answer)
        self.button_no.grid(column=1, row=2, pady=10)
        self.question_text = self.canvas.create_text(150, 125, text="test tu bedzie pytanie", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), width=280)
        self.label_score = Label(text="Score: 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_no.config(state="disabled")
            self.button_yes.config(state="disabled")

    def yes_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def no_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        color = ""
        if is_right:
            color = GREEN
        else:
            color = RED
        self.canvas.configure(bg=color)
        self.window.after(1000, self.change_to_white)

    def change_to_white(self):
        self.canvas.configure(bg="white")
        self.get_next_question()


