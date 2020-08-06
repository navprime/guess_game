import tkinter as tk
from random import randint


TOTAL_CHANCES = 5

chances_remaining = TOTAL_CHANCES
number_of_attempts = 0
random_number = randint(1, 10)
print(random_number)


def check_guessed_number(num):
    if num > random_number:
        return "Guess a lower number"
    elif num < random_number:
        return "Guess a higher number"
    else:
        return "You have guessed correct number"


def submit_button_handler():
    global chances_remaining, number_of_attempts
    # print("Submit button clicked !")
    if chances_remaining == 0:
        guess_attempt.config(text="Sorry! You have no more chances left !")
        return

    guessed_str = box.get()
    box.delete(0, 'end')
    try:
        guessed_number = int(guessed_str)
    except ValueError:
        hint_text.config(text=f"{guessed_str} is not a valid number")
        return
    if 0 > guessed_number or guessed_number > 10:
        hint_text.config(text="Type a number between 1 and 10")
        return

    hint_message = check_guessed_number(guessed_number)
    chances_remaining -= 1
    number_of_attempts += 1
    guess_count.config(text=f"No. of attempts: {number_of_attempts}")
    guess_attempt.config(text=f"No. of chances left: {chances_remaining}")

    hint_text.config(text=hint_message)


def reset_button_handler():
    global chances_remaining, number_of_attempts, random_number

    random_number = randint(1, 10)
    print(random_number)

    chances_remaining = TOTAL_CHANCES
    number_of_attempts = 0
    guess_count.config(text=f"No.of attempts:{ number_of_attempts}")
    guess_attempt.config(text=f"No. of chances left: {chances_remaining}")

    hint_text.config(text="guess a number")


root = tk.Tk()
root.title("Guessing Game")
root.geometry("600x200")
root.resizable(0, 0)
#frame = tk.Frame()
# frame.pack()


guess_count = tk.Label(root, text="No. of attempts: 0",
                       font=("black", 18), borderwidth=3, relief="raised")

guess_attempt = tk.Label(root, text=f"No of chances left: {chances_remaining}",
                         font=("red", 18), borderwidth=3, relief="raised")

guess_range = tk.Label(root, text="Guess a no. from 1 to 10:-",
                       relief="flat", font="green")

hint_text = tk.Label(root, text=" ", relief="flat", font=("green",))


box = tk.Entry(root, width=10, fg="red", font=(
    "verdana", 20, "bold"), justify=tk.CENTER)  # , bg="black")


guess_count.grid(row=0, column=0, padx=(20, 10), pady=20)
guess_attempt.grid(row=0, column=1, padx=(10, 20), pady=20)
guess_range.grid(row=1, column=0, padx=(20, 0), pady=(10, 20), )
box.grid(row=1, column=1)

hint_text.grid(row=2, column=0)

submit_button = tk.Button(root, text="Submit ",
                          command=submit_button_handler).grid(row=2, column=1, padx=20, sticky='E')
reset_button = tk.Button(root, text="Reset ",
                         command=reset_button_handler).grid(row=2, column=1, padx=20, sticky='W')


#submit_button.grid(row=1, column=0, padx=20, sticky='W')


root.mainloop()
