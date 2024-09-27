
import math
import sys

class Teque:

    def __init__(self):
        #constructor builds list
        self.liste = []

    def push_back(self,i):
        #adds to end of list
        self.liste.append(i)

    def push_front(self,i):
        #adds to front of list
        index = 0
        self.liste.insert(index,i)

    def push_middle(self,i):

        #calulates middle and inserts value in list
        k = len(self.liste)
        j = math.floor((k+1)/2)

        #checks to make sure element to insert is valid
        if i is not None:
            self.liste.insert(j,i)

    def get(self,i):
        #if the index is valid it prints the value at that index
        #if i in range(len(self.liste)+1):
        print(self.liste[i])
        #else:
            #print('Index out of bounds.')

def main():

    with open(sys.argv[0], 'r') as file:
        lines = file.readlines()

    #variable to hold number of instructions 
    #instructions = int(input())

    #new Teque object
    teque = Teque()

    for i in range(0,1):
        instructions = lines[:1]

    #reads 
    for line in lines[1:]:
        line = line.strip().split(' ')
        command = line[0]
        tall = int(line[1])

        if command == 'push_back':
            teque.push_back(tall)
        
        elif command == 'push_front':
            teque.push_front(tall)

        elif command == 'push_middle':
            teque.push_middle(tall)
        
        elif command == "get":
            teque.get(tall)
        

if __name__ == '__main__':
    main()
