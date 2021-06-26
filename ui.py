from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # quiz_brain: QuizBrain adds datatype of QuizBrain to quiz_brain

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Text",
            font=("Ariel", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.send_true)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.send_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz"
                                                            f"\nFinal score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def send_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def send_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)