from tkinter import *

pass_root = Tk()                      #root is an instance of tk class

pass_root.geometry("950x450")                # width x height

pass_root.maxsize(750,550)                    # width, height
pass_root.minsize(450,250)                      # width, height
pass_root.title("Password Strength Chckr")


text_area = Label(text = "WELCOME! to password strength checker..")
text_area.pack()

para_Label = Label(text='''A password strength checker evaluates the security 
                   level of a password based on various criteria like length,
                    use of uppercase/lowercase letters, numbers, and special characters.

here's a simple implementation of a Password Strength Checker using HTML, CSS, and JavaScript:

 Minimum 8 characters

At least one digit

 At least one uppercase letter

 At least one lowercase letter

 At least one special character, 

Let me know if you want a GUI version with Tkinter or a CLI that gives detailed feedback.''', 
bg="pink", fg ="red", padx=44, pady=54)

para_Label.pack()



pass_root.mainloop()                  #eventloop