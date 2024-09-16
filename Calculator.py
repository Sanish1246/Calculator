import tkinter as GUI  # Imports the tkinter necessary for the GUI
import math

calculation=""  # Variable to store the actual calculation being done
displayCalc=""  # Variable to store the values that will be displayed
previousCalc="" 
previousDisplay=""
Ans=""

def centerWindow(window, width, height):  # Method to center the GUI on the screen
    screenWidth = window.winfo_screenwidth()  # Otains the width of the screen
    screenHeight = window.winfo_screenheight()# Otains the height of the screen

    xCoordinate = (screenWidth - width) // 2  # Divides by 2 to find the center of the screen
    yCoordinate = (screenHeight - height) // 2

    window.geometry(f"{width}x{height}+{xCoordinate}+{yCoordinate}")  # Defines the size of the window and the center coordinates


def concatenateCalc(character):  # Procedure to concatenate each digit and character in the calcuation
    global calculation  # Declares it as global variable so other methods can use it
    global displayCalc
    calculation+=str(character)  # Concatenation

    if character=="math.sin(math.radians(":   # Changing the appearance of the displayed string based on the operation being done
        displayCalc+="sin(rad("
    elif character=="math.cos(math.radians(":
        displayCalc+="cos(rad("
    elif character=="math.tan(math.radians(":
        displayCalc+="tan(rad("
    elif character=="math.asin(":
        displayCalc+="sin⁻¹("
    elif character=="math.acos(":
        displayCalc+="cos⁻¹("
    elif character=="math.atan(":
        displayCalc+="tan⁻¹("
    elif character=="math.log(":
        displayCalc+="log("
    elif character=="math.sqrt(":
        displayCalc+="√("
    elif character==str(math.pi):
        displayCalc+="π"
    elif character==str(math.e):
        displayCalc+="e"
    elif character=="**":
        displayCalc+="^"
    elif character=="**2":
        displayCalc+="^2"
    elif character=="**3":
        displayCalc+="^3"
    elif character=="10**":
        displayCalc+="10^"
    elif character==Ans:
        displayCalc+="Ans"
    else:
        displayCalc+=str(character)
    
    result.delete(1.0,"end")  # Deletes the text inside the result box and goes back to index 1 of the string
    result.insert(1.0,displayCalc)  # Displays displayCalc starting from the first character
    

def evaluate():
    try:
        global calculation
        global displayCalc
        global previousCalc
        global previousDisplay
        global Ans
        previousCalc=calculation  # Stores the previous calculation and display string
        previousDisplay=displayCalc
        calculation=str(eval(calculation))  # Evaluates using the eval function
        displayCalc=calculation
        Ans=calculation # Stores the Answer
        result.delete(1.0,"end")  # Deletes the text inside the result box and goes back to index 1
        result.insert(1.0,calculation) 
    except:  # For invalid operations
        clearAll()
        result.insert(1.0,"Math Error") 
    

def clearAll():
    global calculation
    global displayCalc
    displayCalc=""
    calculation = ""
    result.delete(1.0,"end")  # Deletes the text inside the result box and goes back to index 1

def clearOne():
    global calculation
    global displayCalc
    calculation=calculation[:-1]  # Removes the last character only
    displayCalc=displayCalc[:-1]  # Removes the last character only

    result.delete(1.0,"end")
    result.insert(1.0,displayCalc)

def goToPrevious():
    global calculation
    global displayCalc
    global previousCalc
    global previousDisplay
    displayCalc = previousDisplay  # Assigns the values of the previous calculation and display strings
    calculation = previousCalc
    result.delete(1.0,"end")  # Deletes the text inside the result box and goes back to index 1
    result.insert(1.0,displayCalc)


frame=GUI.Tk()
centerWindow(frame,450,450)  # Setting the size and position of the calculator frame

result=GUI.Text(frame, height=2, width=25, font=("Arial",25)) # setting the size of the text box to display the values
result.grid(columnspan=6)

# Creating the buttons
# lambda keyword is used here to create an anonymous function that takes no arguments but calls concatenateCalc
# This allows passing the values to the concatenateCalc function when the button is clicked.
# If lambda was absent, each button will automatically call the functions without being clicked instead of waiting for the user to click on them
# The sin, cos, tan, asin, acos and atan functions only works with angles in radians

sin=GUI.Button(frame, text="sin", command=lambda:concatenateCalc("math.sin(math.radians("),width=5, font=("Calibri", 15))
sin.grid(row=2,column=1)
cos=GUI.Button(frame, text="cos", command=lambda:concatenateCalc("math.cos(math.radians("),width=5, font=("Calibri", 15))
cos.grid(row=2,column=2)
tan=GUI.Button(frame, text="tan", command=lambda:concatenateCalc("math.tan(math.radians("),width=5, font=("Calibri", 15))
tan.grid(row=2,column=3)


sinInv=GUI.Button(frame, text="sin⁻¹", command=lambda:concatenateCalc("math.asin("),width=5, font=("Calibri", 15))
sinInv.grid(row=3,column=1)
cosInv=GUI.Button(frame, text="cos⁻¹", command=lambda:concatenateCalc("math.acos("),width=5, font=("Calibri", 15))
cosInv.grid(row=3,column=2)
tanInv=GUI.Button(frame, text="tan⁻¹", command=lambda:concatenateCalc("math.atan("),width=5, font=("Calibri", 15))
tanInv.grid(row=3,column=3)
tenPower=GUI.Button(frame, text="10^", command=lambda:concatenateCalc("10**"),width=5, font=("Calibri", 15))
tenPower.grid(row=3,column=4)
switchOff=GUI.Button(frame, text="Off", command=lambda:exit(),width=5, font=("Calibri", 15))  # Will terminate the program
switchOff.grid(row=3,column=5)  # Lambda is used here or else the program will not start as it will automatically call exit()
    

sqroot=GUI.Button(frame, text="√", command=lambda:concatenateCalc("math.sqrt("),width=5, font=("Calibri", 15))
sqroot.grid(row=4,column=1)
square=GUI.Button(frame, text="x²", command=lambda:concatenateCalc("**2"),width=5, font=("Calibri", 15))
square.grid(row=4,column=2)
cube=GUI.Button(frame, text="x³", command=lambda:concatenateCalc("**3"),width=5, font=("Calibri", 15))
cube.grid(row=4,column=3)


button1=GUI.Button(frame, text="1", command=lambda:concatenateCalc(1),width=5, font=("Calibri", 15))
button1.grid(row=5,column=1)
button2=GUI.Button(frame, text="2", command=lambda:concatenateCalc(2),width=5, font=("Calibri", 15))
button2.grid(row=5,column=2)
button3=GUI.Button(frame, text="3", command=lambda:concatenateCalc(3),width=5, font=("Calibri", 15))
button3.grid(row=5,column=3)
button4=GUI.Button(frame, text="4", command=lambda:concatenateCalc(4),width=5, font=("Calibri", 15))
button4.grid(row=6,column=1)
button5=GUI.Button(frame, text="5", command=lambda:concatenateCalc(5),width=5, font=("Calibri", 15))
button5.grid(row=6,column=2)
button6=GUI.Button(frame, text="6", command=lambda:concatenateCalc(6),width=5, font=("Calibri", 15))
button6.grid(row=6,column=3)
button7=GUI.Button(frame, text="7", command=lambda:concatenateCalc(7),width=5, font=("Calibri", 15))
button7.grid(row=7,column=1)
button8=GUI.Button(frame, text="8", command=lambda:concatenateCalc(8),width=5, font=("Calibri", 15))
button8.grid(row=7,column=2)
button9=GUI.Button(frame, text="9", command=lambda:concatenateCalc(9),width=5, font=("Calibri", 15))
button9.grid(row=7,column=3)
button0=GUI.Button(frame, text="0", command=lambda:concatenateCalc(0),width=5, font=("Calibri", 15))
button0.grid(row=8,column=2)

point=GUI.Button(frame, text=".", command=lambda:concatenateCalc("."),width=5, font=("Calibri", 15))
point.grid(row=8,column=1)
ans=GUI.Button(frame, text="Ans", command=lambda:concatenateCalc(Ans),width=5, font=("Calibri", 15))
ans.grid(row=8,column=3)

expo=GUI.Button(frame, text="^", command=lambda:concatenateCalc("**"),width=5, font=("Calibri", 15))
expo.grid(row=2,column=4)
plus=GUI.Button(frame, text="+", command=lambda:concatenateCalc("+"),width=5, font=("Calibri", 15))
plus.grid(row=5,column=4)
minus=GUI.Button(frame, text="-", command=lambda:concatenateCalc("-"),width=5, font=("Calibri", 15))
minus.grid(row=6,column=4)
times=GUI.Button(frame, text="x", command=lambda:concatenateCalc("*"),width=5, font=("Calibri", 15))
times.grid(row=7,column=4)
divide=GUI.Button(frame, text="÷", command=lambda:concatenateCalc("/"),width=5, font=("Calibri", 15))
divide.grid(row=8,column=4)

OpenBracket=GUI.Button(frame, text="(", command=lambda:concatenateCalc("("),width=5, font=("Calibri", 15))
OpenBracket.grid(row=4,column=4)
CloseBracket=GUI.Button(frame, text=")", command=lambda:concatenateCalc(")"),width=5, font=("Calibri", 15))
CloseBracket.grid(row=4,column=5)

equal=GUI.Button(frame, text="=", command=evaluate, width=10, font=("Calibri", 15))
equal.grid(row=9,column=1, columnspan=2)
clear=GUI.Button(frame, text="C", command=clearAll,width=10, font=("Calibri", 15))
clear.grid(row=9,column=3, columnspan=2)
previous=GUI.Button(frame, text="↺", command=goToPrevious,width=5, font=("Calibri", 15))
previous.grid(row=9,column=5)

backSpace=GUI.Button(frame, text="⌫", command=clearOne,width=5, font=("Calibri", 15))
backSpace.grid(row=2,column=5)
log=GUI.Button(frame, text="log(a,b)", command=lambda:concatenateCalc("math.log("),width=5, font=("Calibri", 14))
log.grid(row=5,column=5)
pi=GUI.Button(frame, text="π", command=lambda:concatenateCalc(str(math.pi)),width=5, font=("Calibri", 15))
pi.grid(row=6,column=5)
e=GUI.Button(frame, text="e", command=lambda:concatenateCalc(str(math.e)),width=5, font=("Calibri", 15))
e.grid(row=7,column=5)
comma=e=GUI.Button(frame, text=",", command=lambda:concatenateCalc(","),width=5, font=("Calibri", 15))
comma.grid(row=8,column=5)


# The program will loop indefinetely
frame.mainloop()