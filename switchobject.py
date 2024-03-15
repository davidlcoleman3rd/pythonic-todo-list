
from linkedlist import *

class Bundle:
    def __init__(self, function, condition, dependencies):
        self.method = function
        self.trigger = condition
        self.parameters = []

        for i in dependencies:
            self.parameters.append(i)

class Switch:
    def __init__(self, conditionsIn, functionsIn, dependenciesIn):
        self.functionList = LinkedList()
        self.tempItem = None

        for item, condition, dependency in zip(functionsIn, conditionsIn, dependenciesIn):
            self.functionList.append(Node(Bundle(item, condition, dependency)))

    def parse(self, inputQuery):
        found = False
        iter = 1
       # print(f"length - {self.functionList.length}")
        while not found and iter <= self.functionList.length:
            self.tempItem = self.functionList.iterate(iter)
           # print(f"func = {self.tempItem.method}")
           # print(f"trigger = {self.tempItem.trigger}")
          #  print(f"param = {self.tempItem.parameters}")
            if inputQuery == self.tempItem.trigger:
                found = True
               # print("found it")
            iter += 1
        if len(self.tempItem.parameters) == 0:
            self.tempItem.method()
        else:
            self.tempItem.method(self.tempItem.parameters)