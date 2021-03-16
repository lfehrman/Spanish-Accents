from tkinter import *

def cpy_to_clip(character):
    root.clipboard_clear()
    root.clipboard_append(character)
    root.update()
    lblStr = character + " has been copied to clipboard"
    lbl.config(text = lblStr)

root = Tk()
root.geometry('265x310')
root.title("Spanish Accents")

btnHeight = 4
btnWidth = 8

#Á button
button1 = Button(root, text="Á", command=lambda: cpy_to_clip('Á'), height=btnHeight, width=btnWidth)
button1.grid(column=0, row=0)

#á button
button2 = Button(root, text="á", command=lambda: cpy_to_clip('á'), height=btnHeight, width=btnWidth)
button2.grid(column=1, row=0)

#É button
button3 = Button(root, text="É", command=lambda: cpy_to_clip('É'), height=btnHeight, width=btnWidth)
button3.grid(column=2, row=0)

#é button
button4 = Button(root, text="é", command=lambda: cpy_to_clip('é'), height=btnHeight, width=btnWidth)
button4.grid(column=3, row=0)

#Í button
button5 = Button(root, text="Í", command=lambda: cpy_to_clip('Í'), height=btnHeight, width=btnWidth)
button5.grid(column=0, row=1)

#í button
button6 = Button(root, text="í", command=lambda: cpy_to_clip('í'), height=btnHeight, width=btnWidth)
button6.grid(column=1, row=1)

#Ó button
button7 = Button(root, text="Ó", command=lambda: cpy_to_clip('Ó'), height=btnHeight, width=btnWidth)
button7.grid(column=2, row=1)

#ó button
button8 = Button(root, text="ó", command=lambda: cpy_to_clip('ó'), height=btnHeight, width=btnWidth)
button8.grid(column=3, row=1)

#Ú button
button9 = Button(root, text="Ú", command=lambda: cpy_to_clip('Ú'), height=btnHeight, width=btnWidth)
button9.grid(column=0, row=2)

#ú button
button10 = Button(root, text="ú", command=lambda: cpy_to_clip('ú'), height=btnHeight, width=btnWidth)
button10.grid(column=1, row=2)

#Ñ button
button11 = Button(root, text="Ñ", command=lambda: cpy_to_clip('Ñ'), height=btnHeight, width=btnWidth)
button11.grid(column=2, row=2)

#ñ button
button12 = Button(root, text="ñ", command=lambda: cpy_to_clip('ñ'), height=btnHeight, width=btnWidth)
button12.grid(column=3, row=2)

#¿ button
button13 = Button(root, text="¿", command=lambda: cpy_to_clip('¿'), height=btnHeight, width=btnWidth)
button13.grid(column=0, row=3)

#¡ button
button14 = Button(root, text="¡", command=lambda: cpy_to_clip('¡'), height=btnHeight, width=btnWidth)
button14.grid(column=1, row=3)

#Confirmation Label
lbl = Label(text="Click on a button to copy to clipboard", font=("serif-sans", 12))
lbl.grid(row=4, columnspan=4)

root.mainloop()

