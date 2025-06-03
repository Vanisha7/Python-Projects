import re
# from tkinter import *

def pass_chckr(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔢 Make it atleast 8 characters long")


    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("🔠 Add atleast 1 uppercase letter [A-Z]")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("🔡 Add atleast 1 lowercase letter [a-z]")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("🔢 Add atleast 1 no. [0-9]")

    if re.search(r'[!@#$%^&*():",.<>|/;?]', password):
        score += 1
    else:
        suggestions.append("Add a special character like @,#,!,$ etc.")

    
    if score >= 5:
        return "Strong 💪", []
    if score >=3:
        return "Moderate ⚠️", suggestions
    else:
        return "Weak ❌", suggestions
    
# # gui

# psc_root = Tk()
# psc_root.geometry("450x350")
# psc_root.resizable(False, False)

# textArea = Label(text="Welcome To 🔐 PASSWORD STRENGTH CHECKER..🔐", bg="cyan", fg="red")
# textArea.pack()

    

print("🔐 PASSWORD STRENGTH CHECKER..🔐")


while True: 
        
    password = input("👉 Enter Password: ")
    strength, suggestions = pass_chckr(password)
    print("🔎 Strength: " + strength)

    if strength == "Strong 💪":
        print("✅ Great! Your password is strong and accepted.")
        break
    else:
        print("Try Again!")
        print("💡 Suggestions to improve your password:")

        for s in suggestions:
            print("- " + s)
        print()



# psc_root.mainloop()
