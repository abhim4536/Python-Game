from tkinter import *
from tkinter import colorchooser
from random import randint
from PIL import Image, ImageTk


root = Tk()
root.minsize(500, 500)
root.maxsize(500, 500)
p = PhotoImage(file = "calculations.png")
root.iconphoto(True,p)
root.title("Play With Maths")
root.geometry("500x500")


# FUNCTIONS

def div_correct(num1, num2):
    correct = num1 / num2
    round(correct, 2)

    output_correct = StringVar()
    output_incorrect = StringVar()
    output_correct.set('Correct')
    output_incorrect.set('WRONG!  ' + str(num1) + ' / ' + str(num2) + ' = ' + str(correct) )

    if float(div_answer.get(),) == correct:
        div_correct_label.config(text=output_correct.get())
    else:
        div_correct_label.config(text=output_incorrect.get())


    div_answer.delete(0,'end')
    num_1.set(randint(0, 100))
    num_2.set(randint(1, 10))
    div_flash.config(text=str(num_1.get()) + '/' + str(num_2.get()), font=("helvetica", 45))

def divide():
    hide_frame()
    div_frame.pack(fill="both", expand=1)
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 100))
    num_2.set(randint(1, 10))


    global div_flash
    div_flash = Label(div_frame, text=str(num_1.get()) + '/' + str(num_2.get()), font=("helvetica", 45))
    div_flash.pack(pady=50)

    global div_answer
    div_answer = Entry(div_frame)
    div_answer.pack(pady=8)


    global div_correct_label
    div_correct_label = Label(div_frame, text="Enter Your Answer Dude")
    div_correct_label.pack(pady=5)
    
    div_button = Button(div_frame, text="Answer", command=lambda: div_correct(num_1.get(), num_2.get()))
    div_button.pack(pady=10)






def mul_correct(num1, num2):
    correct = num1 * num2

    output_correct = StringVar()
    output_incorrect = StringVar()
    output_correct.set('Correct')
    output_incorrect.set('WRONG!  ' + str(num1) + ' * ' + str(num2) + ' = ' + str(correct) )

    if int(mul_answer.get()) == correct:
        mul_correct_label.config(text=output_correct.get())
    else:
        mul_correct_label.config(text=output_incorrect.get())


    mul_answer.delete(0,'end')
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))
    mul_flash.config(text=str(num_1.get()) + '*' + str(num_2.get()), font=("helvetica", 45))

def multiply():
    hide_frame()
    mul_frame.pack(fill="both", expand=1)
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))


    global mul_flash
    mul_flash = Label(mul_frame, text=str(num_1.get()) + '*' + str(num_2.get()), font=("helvetica", 45))
    mul_flash.pack(pady=50)

    global mul_answer
    mul_answer = Entry(mul_frame)
    mul_answer.pack(pady=8)


    global mul_correct_label
    mul_correct_label = Label(mul_frame, text="Enter Your Answer Dude")
    mul_correct_label.pack(pady=5)

    mul_button = Button(mul_frame, text="Answer", command=lambda: mul_correct(num_1.get(), num_2.get()))
    mul_button.pack(pady=10)





def sub_correct(num1, num2):
    correct = num1 - num2

    output_correct = StringVar()
    output_incorrect = StringVar()
    output_correct.set('Correct')
    output_incorrect.set('WRONG!  ' + str(num1) + ' - ' + str(num2) + ' = ' + str(correct))

    if int(sub_answer.get()) == correct:
        sub_correct_label.config(text=output_correct.get())
    else:
        sub_correct_label.config(text=output_incorrect.get())


    sub_answer.delete(0,'end')
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))
    sub_flash.config(text=str(num_1.get()) + '-' + str(num_2.get()), font=("helvetica", 45))

def subtract():
    hide_frame()
    sub_frame.pack(fill="both", expand=1)
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))


    global sub_flash
    sub_flash = Label(sub_frame, text=str(num_1.get()) + '-' + str(num_2.get()), font=("helvetica", 45))
    sub_flash.pack(pady=50)

    global sub_answer
    sub_answer = Entry(sub_frame)
    sub_answer.pack(pady=8)

    global sub_correct_label
    sub_correct_label = Label(sub_frame, text="Enter Your Answer Dude")
    sub_correct_label.pack(pady=5)


    sub_button = Button(sub_frame, text="Answer", command=lambda: sub_correct(num_1.get(), num_2.get()))
    sub_button.pack(pady=10)





def add_correct(num1, num2):
    correct = num1 + num2

    output_correct = StringVar()
    output_incorrect = StringVar()
    output_correct.set('Correct')
    output_incorrect.set('WRONG!  ' + str(num1) + ' + ' + str(num2) + ' = ' + str(correct) )

    if int(add_answer.get()) == correct:
        add_correct_label.config(text=output_correct.get())
    else:
        add_correct_label.config(text=output_incorrect.get())


    add_answer.delete(0,'end')
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))
    add_flash.config(text=str(num_1.get()) + '+' + str(num_2.get()), font=("helvetica", 45))

def add():
    hide_frame()
    add_frame.pack(fill="both", expand=1)
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 101))
    num_2.set(randint(0, 101))


    global add_flash
    add_flash = Label(add_frame, text=str(num_1.get()) + '+' + str(num_2.get()), font=("helvetica", 45))
    add_flash.pack(pady=50)

    global add_answer
    add_answer = Entry(add_frame)
    add_answer.pack(pady=8)

    global add_correct_label
    add_correct_label = Label(add_frame, text="Enter Your Answer Dude")
    add_correct_label.pack(pady=5)


    add_button = Button(add_frame, text="Answer", command=lambda: add_correct(num_1.get(), num_2.get()))
    add_button.pack(pady=10)





def hide_frame():

    for widget in add_frame.winfo_children():
        widget.destroy()
    for widget in sub_frame.winfo_children():
        widget.destroy()
    for widget in mul_frame.winfo_children():
        widget.destroy()
    for widget in div_frame.winfo_children():
        widget.destroy()
    for widget in start_frame.winfo_children():
        widget.destroy()


    add_frame.pack_forget()
    sub_frame.pack_forget()
    mul_frame.pack_forget()
    div_frame.pack_forget()
    start_frame.pack_forget()


def home():
    
    hide_frame()
    start_frame.pack(fill="both", expand=1)
    load = Image.open("think.png")
    load.thumbnail((99,99))
    render1 = ImageTk.PhotoImage(load)
    img = Label(image=render1)
    img.image = render1
    img.place(x=395, y=395)

    
    start_label = Label(start_frame, text="Welcome To Math's Game", bg = '#c7c7c7', font=('Comic Sans MS', 25)).pack(pady=40)

    a_button = Button(start_frame, text="Addiction", command=add, bg='#c7c7c7').pack(pady=10)
    s_button = Button(start_frame, text="Subtraction", command=subtract, bg='#c7c7c7').pack(pady=15)
    m_button = Button(start_frame, text="Multiplication", command=multiply, bg='#c7c7c7').pack(pady=15)
    d_button = Button(start_frame, text="Division", command=divide, bg='#c7c7c7').pack(pady=15)


# MAIN MENU
my_menu = Menu(root)
root.config(menu=my_menu)

# MENU ITEMS
math_menu = Menu(my_menu, bg = '#c7c7c7')
my_menu.add_cascade(label="Menu", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Home", command=home)
math_menu.add_command(label="Exit", command=root.quit)


#FRAMES

add_frame = Frame(root, width=500, height=500, bg="#196a47")
sub_frame = Frame(root, width=500, height=500, bg="#df3e5d")
mul_frame = Frame(root, width=500, height=500, bg="#901136")
div_frame = Frame(root, width=500, height=500, bg="#8f5c7c")
start_frame = Frame(root, height=500, width=500, bg='#383838')

home()

root.mainloop()