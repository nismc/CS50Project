from tkinter import *
from tkinter import messagebox
import csv

window = Tk()
window.geometry("500x500")
window.configure(bg="black")
window.title("Login")


def main():
    label = Label(window,
                  text="Enter username and password",
                  font=("Arial", 30),
                  fg="#00FF00",
                  bg="black",
                  padx=20,
                  pady=20)
    label.pack()

    username_label = Label(window,
                           text="Username: ",
                           font=("Arial", 30),
                           fg="#00FF00",
                           bg="black",
                           padx=20,
                           pady=20)
    username_label.pack()

    username_entry = Entry(window,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black")
    username_entry.pack()

    password_label = Label(window,
                           text="Password: ",
                           font=("Arial", 30),
                           fg="#00FF00",
                           bg="black",
                           padx=20,
                           pady=20)
    password_label.pack()

    password_entry = Entry(window,
                           font=("00FF00", 20),
                           show="*",
                           bg="black")
    password_entry.pack()

    def enter():
        username = username_entry.get()
        password = password_entry.get()
        if check_credentials(username, password):
            program = Tk()
            program.geometry("500x500")
            program.configure(bg="black")
            program.title("Program")
            success = Label(program,
                            text="You have successfully entered the program 😃",
                            font=("Arial", 20),
                            fg="#00FF00",
                            bg="black",
                            padx=20,
                            pady=20)
            success.place(x=100, y=100)
            success.pack()
        else:
            messagebox.showinfo("Error", "Wrong username and/or password")

    enter_button = Button(window,
                          text="Enter",
                          command=enter)
    enter_button.pack(side=RIGHT)

    signup_button = Button(window,
                           text="Sign up",
                           command=signup)
    signup_button.pack(side=LEFT)


def save_credentials(username, password):
    try:
        with open("credentials.csv", mode="a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
    except Exception as x:
        print(f"Error: {x}")


def check_credentials(username, password):
    with open("credentials.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                return True
        return False


def signup():
    signup_window = Tk()
    signup_window.geometry("500x500")
    signup_window.configure(bg="black")
    signup_window.title("Signup")
    label = Label(signup_window,
                  text="Create username and password",
                  font=("Arial", 30),
                  fg="#00FF00",
                  bg="black",
                  padx=20,
                  pady=20)

    def save_signup():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        password2 = conf_password_entry.get()
        if new_username.strip() and new_password.strip():
            if new_password == password2:
                if not check_username_existence(new_username):
                    save_credentials(new_username, new_password)
                    signup_window.destroy()
                    messagebox.showinfo("Success", "Signup successful! You can now log in")
                else:
                    messagebox.showinfo("Error", "Username already exists")
            else:
                messagebox.showinfo("Error", "The passwords don't match")
        else:
            messagebox.showinfo("Error", "You did not type in a username and a password")

    enter_button = Button(signup_window,
                          text="Enter",
                          command=save_signup)
    enter_button.pack(side=RIGHT)

    label.pack()

    username_label = Label(signup_window,
                           text="Username: ",
                           font=("Arial", 30),
                           fg="#00FF00",
                           bg="black",
                           padx=20,
                           pady=20)
    username_label.pack()

    new_username_entry = Entry(signup_window,
                               font=("Arial", 20),
                               fg="#00FF00",
                               bg="black")
    new_username_entry.pack()

    password_label = Label(signup_window,
                           text="Password: ",
                           font=("Arial", 30),
                           fg="#00FF00",
                           bg="black",
                           padx=20,
                           pady=20)
    password_label.pack()

    new_password_entry = Entry(signup_window,
                               font=("Arial", 20),
                               fg="#00FF00",
                               show="*",
                               bg="black")
    new_password_entry.pack()

    conf_password_label = Label(signup_window,
                                text="Confirm password: ",
                                font=("Arial", 30),
                                fg="#00FF00",
                                bg="black",
                                padx=20,
                                pady=20)
    conf_password_label.pack()

    conf_password_entry = Entry(signup_window,
                                font=("Arial", 20),
                                fg="#00FF00",
                                show="*",
                                bg="black")
    conf_password_entry.pack()


def check_username_existence(username):
    with open("credentials.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] == username:
                return True
        return False


main()
window.mainloop()
