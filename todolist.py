"""
    @classmethod
    def fromFile(self, fileContents):
        self.todoList = LinkedList()
        self.progressSafe = True
        for line in fileContents:
            line = line.replace("\n", "")
            self.getItemSilent(self, line)
"""

from linkedlist import *
from switchobject import *
from sys import version

#------
class Looper:
    def __init__(self):
        self.looper = True

    def status(self):
        return self.looper

    def setFalse(self):
        self.looper = False

    def setTrue(self):
        self.looper = True

    def flip(self):
        self.looper = not looper
#------
class File:
    def __init__(self):
        self.file = None
        self.title = ""
    
    def openFile(self, titleIn):
        self.title = f"{titleIn}.tdl"
        self.file = open(title, )

    def passFile(self, titleIn):
        self.openFile(titleIn)
        self.output = self.file
        return file
#------
class ToDo:
    def __init__(self, fileContents):
        self.todoList = LinkedList()
        self.progressSafe = True
        if fileContents != 0:
            for line in fileContents:
                line = line.replace("\n", "")
                self.getItemSilent(line)    

    #******
    def printTodo(self):
        print(f"Current To Do List:")
        print('---------------------------------------------------')
        self.todoList.printList()
        print('---------------------------------------------------')
        print('')
        print('')

    #******
    def delTodo(self):
        self.todoList.clearList()
        print('')
        print('List has been deleted.')
        print('')

    #******
    def getListFromFile(self, fileName):
        try:
            file = open(fileName, "rt")
        except:
            print("The file could not be found")
            return
        self.delTodo()
        lineVar = file.readlines()
        for iter in lineVar:
            self.getItemSilent(iter.strip())
        file.close()
        self.sortList()
        self.printTodo()

    #******
    def getItem(self, nextItem):
        nextTrimmed = ''
        tempNext = ''
        trimCounter = 0
        for i in nextItem:
            if i != '*':
                tempNext = tempNext + i
        for i in nextItem:
            if i == '*':
                trimCounter = trimCounter + 1
                if trimCounter <= 5:
                    nextTrimmed = nextTrimmed + i
                elif trimCounter == 6:
                    nextTrimmed = nextTrimmed + ' '
            else:
                while trimCounter <= 5:
                    nextTrimmed = nextTrimmed + ' '
                    trimCounter = trimCounter + 1
                if trimCounter <= 40:
                    nextTrimmed = nextTrimmed + i
                trimCounter = trimCounter + 1
        print(f"\"{tempNext.strip()}\" has been added to your to do list")
        print('')
        self.todoList.append(Node(nextTrimmed))
        self.sortList()
        self.printTodo()
        self.progressSafe is False
        print('')
        print('')

    #******
    def getItemSilent(self, nextItem):   # DO NOT ADD SORTING TO THIS
        nextTrimmed = ''                 # This is a utility specifically FOR
        tempNext = ''                    # ...the sorting function.  Adding sorting
        trimCounter = 0                  # ...WILL break this!!!!!
        for i in nextItem:
            if i != '*':
                tempNext = tempNext + i
        for i in nextItem:
            if i == '*':
                trimCounter = trimCounter + 1
                if trimCounter <= 5:
                    nextTrimmed = nextTrimmed + i
                elif trimCounter == 6:
                    nextTrimmed = nextTrimmed + ' '
            else:
                while trimCounter <= 5:
                    nextTrimmed = nextTrimmed + ' '
                    trimCounter = trimCounter + 1
                if trimCounter <= 40:
                    nextTrimmed = nextTrimmed + i
                trimCounter = trimCounter + 1
        self.todoList.append(Node(nextTrimmed))
        self.progressSafe is False

    #******
    def removeItem(self, choice):
        try:
            self.todoList.delete(int(choice))
        except TypeError:
            print('Please only use an integer to select your to-do-list item')
            return
        except NoValueFound:
            print('The item to be deleted from the list was not found')
            return
        print(f"\"{choice}\" has been removed from your to do list")
        print('')
        self.sortList()
        self.printTodo()
        self.progressSafe is False
        print('')
        print('')

    #******
    def sortLayer(self, input, depth):
        tempArr = []
        nextArr = []
        finalArr = []
        for i in input:
            if i.value[depth] == "*":
                tempArr.append(i)
            else:
                nextArr.append(i)
        if len(tempArr) > 0:
            finalArr = finalArr + self.sortLayer(tempArr, depth + 1)
        finalArr = finalArr + nextArr
        return finalArr

    #******
    def sortList(self):
        current = self.todoList.head
        tempArr = []
        inputArr = []
        nextArr = []
        finalArr = []
        while current != None:
            tempArr.append(current)
            current = current.next
        for i in tempArr:
            if i.value[0] == "*":
                inputArr.append(i)
            else:
                nextArr.append(i)
        if len(inputArr) > 0:
            finalArr = finalArr + self.sortLayer(inputArr, 1)
        finalArr = finalArr + nextArr
        
        self.todoList.clearList()
        for i in finalArr:
            self.getItemSilent(i.value)



    #******

   # def saveList(self):        --> Will save list to a file
   # def loadList(self):        --> Will erase the current unsaved list and will load a list from the file
   # def saveWarning(self):     --> Will warn the user if they are about to erase unsaved work

looper = Looper()
choice = 0
myList = None

addFunc = lambda : myList.getItem(input("Please enter the new list item:    "))
delFunc = lambda : myList.removeItem(input("Please enter the item # for removal:    "))
loadFunc = lambda : myList.getListFromFile(input("Please enter the name of the file to load:    "))
#saveFunc = lambda : 
quitFunc = lambda : looper.setFalse()
defFunc = lambda : print("The selection was not found.  Please try again!")

noList = []
quitParam = []
quitParam.append(looper)

funcs = [addFunc, delFunc, loadFunc, quitFunc, defFunc]
conds = [1, 2, 3, 4, None]
params = [noList, noList, noList, noList, noList]

mySwitch = Switch(conds, funcs, params)

print(version)

while looper.status():
    print('What would you like to do?')
    print('1) Make a new list')
    print('2) Load a list from a file')
    print('3) Quit')
    choice = int(input())
    if choice > 3 or choice < 0:
        print('Invalid choice.  Please try again.')
    else:
        looper.setFalse()

if choice == 1:
    myList = ToDo(int(0))

elif choice == 2:
    fileName = ""
    fileContents = ""
    looper.setTrue()
    myList = ToDo(int(0))
    mySwitch.parse(3)

else:
    print('Goodbye!')
    quit()

choice = 0

looper.setTrue()

while looper.status():
    myList.printTodo()

    print('What would you like to do?')
    print('1) Add an item')
    print('2) Delete an item')
    #print('3) Change an item\'s priority')
   # print('3) Save my list as a file')
    print('3) Open a different to do list')
    print('4) Quit the application')

    mySwitch.parse(int(input("Choose your option:   ")))

print(f"\n\nGoodbye!!\n\n")



"""
    choice = int(input())
    match choice:
        case 1:
            print("Test complete")
        case _:
            print("Default test")


myList = ToDo()


myList.getItem("* Cook chicken")
myList.getItem("** Fold clothes")
myList.getItem("* Wash car")
myList.getItem("**** Wash laundry")

myList.printTodo()

myList.removeItem(4)       # print(f"length test:  {self.length}")

myList.printTodo()

myList.getItem("***** Wash dogs")
myList.getItem("* Clean bathroom")
myList.getItem("***************** Sleep by 9pm")

myList.sortList()

myList.printTodo()

#myOtherList = LinkedList()
#myOtherList.append(Node("the quick brown fox"))
#myOtherList.append(Node("jumped over the slow cow"))

#myOtherList.printList()
"""
