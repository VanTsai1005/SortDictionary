#! coding : utf-8

from FileDialog import *

def openFile1():
    fd1 = LoadFileDialog(win)
    sourEdit.delete(0, 100)
    sourEdit.insert(10,fd1.go())

def openFile2():
    fd2 = LoadFileDialog(win)
    destEdit.delete(0, 100)
    destEdit.insert(10, fd2.go())

def formCancel():
    exit()

def formClear():
    sourEdit.delete(0, 100)
    destEdit.delete(0, 100)

def formOk():
    sourPath = sourEdit.get()
    destPath = destEdit.get()
    if sourPath == "" or destPath == "":
        print "source or destination path error !!"
    else:
        if os.path.isfile(sourPath) == False:
            print "Source must have a value ..."
        else:
            sourList = open(sourPath, "r").readlines()
            print "Source File : " + str(len(sourList))

            if os.path.isfile(destPath):
                destFile = open(destPath, "r")
                destList = destFile.readlines()
                destFile.close()
                print "Dest File : " + str(len(destList))

                resultSet = set()
                for item in destList:
                    resultSet.add(item)
                for item in sourList:
                    resultSet.add(item)

                resultList=[]
                for item in resultSet:
                    resultList.append(item)

                resultList.sort()

                destFile = open(destPath, "w")
                for item in resultList:
                    destFile.write(item)

                print "Total : "+str(len(resultSet))
                destFile.close()
            else:
                destFile = open(destPath, "w")
                sourList.sort()
                for item1 in sourList:
                    destFile.write(item1)

                print "Total : " + str(len(sourList))
                destFile.close()

win = Tk()
win.geometry("500x100")
sourLabel = Label(win, text="Source File : ")
sourEdit = Entry(win, text="", width="40")
destLabel = Label(win, text="Destination File : ")
destEdit = Entry(win, text="", width="40")
sourButton = Button(win, text="Load", width="10", command=openFile1)
destButton = Button(win, text="Load", width="10", command=openFile2)
okButton = Button(win, text="Ok", width="10", command=formOk)
cancelButton = Button(win, text="Cancel", width="10", command=formCancel)
clearButton = Button(win, text="Clear", width="10", command=formClear)

sourLabel.grid(column=0, row=0)
sourEdit.grid(column=1, row=0, columnspan=10)
sourButton.grid(column=15, row=0)
destLabel.grid(column=0, row=1)
destEdit.grid(column=1, row=1, columnspan=10)
destButton.grid(column=15, row=1)
okButton.grid(column=10, row=3)
cancelButton.grid(column=5,row=3)
clearButton.grid(column=0,row=3)
win.mainloop()
