from tkinter import *
from PIL import Image, ImageTk
from random import randint

#Resize Images
def resize_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

#main window
root = Tk()
root.title("Rock Paper Scissors")
root.config(background= "#ADD8E6")

fixed_size = (200,200)

rock_img_comp = resize_image("rock_comp.png", fixed_size)
paper_img_comp = resize_image("paper_comp.png", fixed_size)
scissor_img_comp = resize_image("scissor_comp.png", fixed_size)

rock_img = resize_image("rock_user.png", fixed_size)
paper_img = resize_image("paper_user.png", fixed_size)
scissor_img = resize_image("scissor_user.png", fixed_size)


#insert picture
comp_label = Label(root,image = scissor_img_comp, bg= "#ADD8E6")
user_label = Label(root,image = scissor_img, bg="#ADD8E6")

comp_label.grid(row = 1, column= 0)
user_label.grid(row=1,column=4)

#scores
comp_score = Label(root,text=0,font=100,bg="#ADD8E6",fg="black")
user_score = Label(root,text=0,font=100,bg="#ADD8E6",fg="black")

comp_score.grid(row=1,column=1)
user_score.grid(row=1,column=3)

#indicators
user_indicator = Label(root, font=50, text="USER",bg="#ADD8E6",fg="black")
comp_indicator = Label(root, font=50, text="COMPUTER",bg="#ADD8E6",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)


#msgs
msg = Label(root, font= 50, bg="#ADD8E6", fg="black", text= "Let's Play!")
msg.grid(row=3,column=2)

#update msg
def updateMsg(x, colour):
    msg["text"] = x
    msg["fg"] = colour

#update User score
def updateUserScore():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)

#update Computer score
def updateCompScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

#Check Winner
def checkWin(user,comp):
    if user == comp:
        updateMsg("It's a tie!", "blue")
    elif user == 'rock':
        if comp == 'paper':
            updateMsg("You lose!", "red")
            updateCompScore()
        else:
            updateMsg("You win!", "green")
            updateUserScore()
    elif user == 'paper':
        if comp == scissors:
            updateMsg("You lose!","red")
            updateCompScore()
        else:
            updateMsg("You win!", "green")
            updateUserScore()
    elif user == 'scissors':
        if comp == 'rock':
            updateMsg("You lose!", "red")
            updateCompScore()
        else:
            updateMsg("You win!", "green")
            updateUserScore()
    

choices = ["rock", "paper","scissors"]
#update choice
def updateChoice(userChoice):
    #for comp
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.config(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.config(image=paper_img_comp)
    else:
        comp_label.config(image=scissor_img_comp)

    #for user
    if userChoice == "rock":
        user_label.config(image=rock_img)
    elif userChoice == "paper":
        user_label.config(image=paper_img)
    else:
        user_label.config(image=scissor_img)

    checkWin(userChoice,compChoice)
    


#buttons
rock = Button(root, width=20, height= 2, text= "ROCK",bg="#D3D3D3",fg="black", command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root, width=20, height= 2, text= "PAPER",bg="#FFFFE0",fg="black",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors = Button(root, width=20, height= 2, text= "SCISSORS",bg="#F08080",fg="black",command=lambda:updateChoice("scissors")).grid(row=2,column=3)

root.mainloop()