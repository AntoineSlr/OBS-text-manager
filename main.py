import tkinter as tk
import glob
import os

import requests
import wget

root = tk.Tk()

root.resizable(False, False)
# 52

canvasheight = 170
os.chdir(r'texts')
textFiles = glob.glob('*.txt')
for i in range(len(textFiles)):
    if (i % 2) == 0:
        canvasheight = canvasheight
    else:
        canvasheight += 51

root.title("StreamTexts")

canvas1 = tk.Canvas(root, width=280, height=canvasheight)
canvas1.pack()
canvas1.config(background="#262626")
#
P1_Label = tk.Label(root, text="IGN PLAYER 1")
P1_Label.configure(background="#272727", foreground="white")
canvas1.create_window(70, 20, window=P1_Label)

file = open('../assets/player1.txt')
P1 = file.read()
imgP1 = tk.Entry(root)
imgP1.insert(0, P1)
canvas1.create_window(70, 40, window=imgP1)
file.close()
#
P2_Label = tk.Label(root, text="IGN PLAYER 2")
P2_Label.configure(background="#272727", foreground="white")
canvas1.create_window(210, 20, window=P2_Label)

file = open('../assets/player2.txt')
P2 = file.read()
imgP2 = tk.Entry(root)
imgP2.insert(0, P2)
canvas1.create_window(210, 40, window=imgP2)
file.close()
#
P3_Label = tk.Label(root, text="IGN PLAYER 3")
P3_Label.configure(background="#272727", foreground="white")
canvas1.create_window(70, 70, window=P3_Label)
file = open('../assets/player3.txt')
P3 = file.read()
imgP3 = tk.Entry(root)
imgP3.insert(0, P3)
canvas1.create_window(70, 90, window=imgP3)
file.close()
#
P4_Label = tk.Label(root, text="IGN PLAYER 4")
P4_Label.configure(background="#272727", foreground="white")
canvas1.create_window(210, 70, window=P4_Label)

file = open('../assets/player4.txt')
P4 = file.read()
imgP4 = tk.Entry(root)
imgP4.insert(0, P4)
canvas1.create_window(210, 90, window=imgP4)
file.close()
#

buttonList = []

i = 0

width1 = 70
width2 = 210

height1 = 120
height2 = 140

for elements in textFiles:
    file = open('%s' % (elements))
    content = file.read()
    if (i % 2) == 0:
        label1 = tk.Label(root, text=elements.split('.')[0])
        label1.configure(background="#272727", foreground="white")
        canvas1.create_window(width1, height1, window=label1)
        entry1 = tk.Entry(root)
        entry1.insert(0, content)
        buttonList.append(entry1)
        canvas1.create_window(width1, height2, window=entry1)
    elif (i % 2) != 0:
        label2 = tk.Label(root, text=elements.split('.')[0])
        label2.configure(background="#272727", foreground="white")
        canvas1.create_window(width2, height1, window=label2)
        entry2 = tk.Entry(root)
        entry2.insert(0, content)
        buttonList.append(entry2)
        canvas1.create_window(width2, height2, window=entry2)
        height1 += 50
        height2 += 50
    file.close()
    i += 1

def confirm():
    contentList = []
    for i in range(len(buttonList)):
        contentList.append(buttonList[i].get())
    i = 0
    for elements in textFiles:
        file = open('%s' % (elements), 'w')
        file.write(contentList[i])
        file.close()
        i += 1

    if os.path.exists("../assets/player1.png"):
        os.remove("../assets/player1.png")
    if os.path.exists("../assets/player2.png"):
        os.remove("../assets/player2.png")
    if os.path.exists("../assets/player3.png"):
        os.remove("../assets/player3.png")
    if os.path.exists("../assets/player4.png"):
        os.remove("../assets/player4.png")
    wget.download(f"https://mc-heads.net/avatar/{imgP1.get()}.png", out="../assets/player1.png")
    wget.download(f"https://mc-heads.net/avatar/{imgP2.get()}.png", out="../assets/player2.png")
    wget.download(f"https://mc-heads.net/avatar/{imgP3.get()}.png", out="../assets/player3.png")
    wget.download(f"https://mc-heads.net/avatar/{imgP4.get()}.png", out="../assets/player4.png")

    file = open('../assets/player1.txt', 'w')
    file.write(imgP1.get())
    file.close()

    file = open('../assets/player2.txt', 'w')
    file.write(imgP2.get())
    file.close()

    file = open('../assets/player3.txt', 'w')
    file.write(imgP3.get())
    file.close()

    file = open('../assets/player4.txt', 'w')
    file.write(imgP4.get())
    file.close()


button1 = tk.Button(text='Save Data', command=confirm)
canvas1.create_window(width2+30, height2-10, window=button1)

root.mainloop()