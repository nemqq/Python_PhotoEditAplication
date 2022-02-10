import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt
from func import *
import tkinter
from tkinter import filedialog, Text
import os

#test images
img = cv.imread(cv.samples.findFile("pawian.jpg"))
#img = cv.imread(cv.samples.findFile("lenna.png"),)
#img2 = cv.imread(cv.samples.findFile("pawian.jpg"))

#Values
filepath = ''
tab= []
funtab = []
funtab = [grey_img,gauss_img, original_img]
listbox_clear = True
print(type(funtab))

#Functions
def Picture(img, choice):

    for fun in funtab:
        if choice == fun:
            fun(img)


def add_path_list(add):
    button_add_picture_text.set('ADD PICTURE')
    text = 'Add file: ' + add
    global listbox_clear
    if listbox_clear:
        listbox.delete(0)
        listbox_clear = False
    listbox.insert(0, text)



def click_button():
    print('wcisnieto przycisk')
    print(list(tab))


def add_picture_path():
    button_add_picture_text.set('loading...')
    filepath = filedialog.askopenfilename( initialdir = "/", title = "Select File",
                                           filetypes=(("all files","*.*"),("executables",".exe")))

    if filepath != '' :
        tab.append(filepath)
        add_path_list(filepath)
    click_button()




#API START HERE

root = tkinter.Tk()  #creat window
root.geometry('800x700') # window size
root.resizable(width=False, height=False) #block resize
root.config(background='#8E8BFF')
root.title("VqApp")


#frame
# frame1 = tkinter.Frame(root, borderwidth=5)
# #frame1.place(x=510, y=10)
# frame1.pack()
# frame1.config(background='black')


#labels
l = tkinter.Label(root, text='Aplication', font=('Raleway',20), fg='white')     #create label
l.pack()
l.config(background='#8E8BFF')

l2 = tkinter.Label(root, text='list of added photos paths',
                   font=('Raleway', 15), fg='white')
l2.place(x=40,y=60)
l2.config(background='#8E8BFF')


#buttons
button_add_picture_text = tkinter.StringVar()
button_add_picture = tkinter.Button(
    root,textvariable=button_add_picture_text, bg='#7673F3',
    font=('Raleway', 12, 'bold'), fg='white',
    width=12, heigh=2, command=add_picture_path)
button_add_picture.place(x=40, y=260)
button_add_picture_text.set('ADD PICTURE')

b1 = tkinter.Button(root, text='konsola', command=click_button)
b1.pack()

b2 = tkinter.Button(root, text='guzik', command=click_button)
b1.pack(side=tkinter.RIGHT)


#listbox
listbox = tkinter.Listbox(
    root,height=9,width = 30,
    selectmode='extended')

listbox.place(x=40, y=90)
listbox.insert(0,'paths...')



root.mainloop()




# #1 Przeksztalecenia barwne
# coloro()                #ZMIANY RGB
# grey_img()              #MONOCHROMATYCZNE
# inverted_img()          #inwersja
# convert_img()
# cv.destroyAllWindows()
# #2 PUNKT
# brightnesschange_img()  #korekte poziomu jasnosci
# resolution()            #zmiana rodzielczosci
# hist2()                 #HISTOGRAM
# two_in_one()            #dodawanie dwoch obrazow, mnozenie,binaryzacja
# my_LUT()                #tablica LUT
# bin()                   #binaryzacja
# cv.destroyAllWindows()
#
#
# # #3 PRZEKSZTALCENIA GEOMETR
# rotate_angle60()    #rotacja o 60 i odbicie lustrzane
# rotate_img()        #rotacja o 90
# scaleup_img()       #zmiana skali
# scaledown_img()     #zmiana skali
# cv.destroyAllWindows()
#
# # #4 przekształcenia morfologiczne
# gauss_img()
# sepia_img()
# erosion_img()
# dilation_img()
# skeletonization_img()
# cv.destroyAllWindows()
#
#
# # #6 TRANSFORMACJA FOURIERA
# furrier2()
# cv.destroyAllWindows()
#
#
# # #7 KOMPRESJA STRATNA
# compression()
# cv.destroyAllWindows()
#
#
# # #8 PRZETWARZANIE OBRAZOW BINARNYCH  and / or / xor
# andorxor()
# cv.destroyAllWindows()