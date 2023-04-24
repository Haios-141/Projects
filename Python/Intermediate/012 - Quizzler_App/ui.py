from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Default Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=correct_img, bd=0, highlightthickness=0, activebackground=THEME_COLOR,
                                  command=self.true_button)
        self.correct_btn.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_img, bd=0, highlightthickness=0, activebackground=THEME_COLOR,
                                command=self.false_button)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.buttons_state(DISABLED)

    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def buttons_state(self, state):
        self.correct_btn.config(state=state)
        self.wrong_btn.config(state=state)

    def give_feedback(self, is_right):
        self.buttons_state(DISABLED)
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, func=self.get_next_question)
