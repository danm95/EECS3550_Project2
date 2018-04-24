from tkinter import filedialog
from tkinter import *
import subprocess


class Interface:

    fileNames = []
    fileSave = "Select a save location"

    def __init__(self, master):

        master.title("EECS:3540_Project2")

        self.label_1 = Label(master, text="Select C++ Standard:")
        self.label_1.grid(row=0, column=0, sticky=E)

        self.variable = StringVar(master)
        self.variable.set("c++98")  # default value

        self.stdOption = OptionMenu(master, self.variable, "c++98", "c++11", "c++14", "c++17")
        self.stdOption.grid(row=0, column=1, sticky=W)

        self.CB = StringVar(master)
        self.CB.set(0)  # default value

        self.debugMode = Checkbutton(master, text="Enable Debugging", variable=self.CB)
        self.debugMode.grid(row=1, column=0, sticky=W)

        self.compileButton = Button(master, text="Compile")
        self.compileButton.grid(row=2, column=0, sticky=W+E+N+S)

        self.quitButton = Button(master, text="Quit", command=master.quit)
        self.quitButton.grid(row=2, column=1, sticky=W+E+N+S)

        self.saveFileButton = Button(master, text="Save File", command=self.saveFile)
        self.saveFileButton.grid(row=0, column=2, padx=10)

        self.label_1 = Label(master, text="Please select a file")
        self.label_1.grid(row=0, column=3, padx=20)

        self.addFileButton = Button(master, text="Add File", command=self.addFile)
        self.addFileButton.grid(row=1, column=2, padx=10, sticky=W+E+N+S)

        self.label_2 = Label(master, text="Please select a file")
        self.label_2.grid(row=1, column=3, padx=20)

    def addFile(self):
        self.fileNames.append(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("C++ Source", "*.cpp"), ("C/C++ Header", "*.h"), ("all files", "*.*"))))
        print(self.fileNames)
        self.fileListUpdate()

    def fileListUpdate(self):

        filelistLen = len(self.fileNames)
        print(filelistLen)
        lb = Label(root, text=self.fileNames[filelistLen-1])
        lb.grid(row=(filelistLen+1), column=3)

    def saveFile(self):
        self.fileSave = filedialog.asksaveasfilename(initialdir="/", title="Select file")
        print(self.fileNames)
        self.label_1.config(text=self.fileSave)


def compile(event, fileNames, savelocation, std, debug):
    g = ""
    std = "-std=" + std.get()
    savelocation = "-o " + savelocation
    fileString = ""
    output = ""

    for i in range(len(fileNames)):
        fileString = fileNames[i] + " "

    if debug.get() == "1":
        g = "-g"

    compileCommand = "g++ " + std + " " + g + " " + savelocation + " " + fileString

    try:
        output = subprocess.check_output(compileCommand, shell=True,  stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("Something " + str(e.returncode))

    print("Compile Command: " + compileCommand)


root = Tk()

GUI = Interface(root)

GUI.compileButton.bind("<Button-1>", lambda event: compile(event, GUI.fileNames, GUI.fileSave, GUI.variable, GUI.CB))

root.mainloop()