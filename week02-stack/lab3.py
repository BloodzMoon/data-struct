
class Stack:

    # variables
    stack = []
    MAX_SIZE = 4
    carID = 1

    # constrcutor
    def __init__(self, myList=None):
        if myList is None:
            self.items = []
        else:
            self.items = myList

    # functions
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) is 0

    def isFull(self):
        return len(self.items) is self.MAX_SIZE

    def pop(self):
        return self.items.pop()

    def push(self):
        if self.isFull():
            print('\nFull!')
        else:
            self.items.append(self.carID)
            self.carID += 1

    def peek(self):
        return self.items[-1]

    def view(self):
        print(self.items)

    def depart(self, id):
        keep = []
        i = len(self.items)-1
        if id in self.items:
            print('')
            while True:
                if self.items[i] is not id:
                    print(' pop' + str(self.peek()), end='')
                    keep.append(self.pop())
                    i -= 1
                elif self.items[i] is id:
                    print('\nCar' + str(self.pop()) + ' depart!')
                    break

            while True:
                if len(keep) is 0:
                    break
                tmp = keep.pop()
                print(' push' + str(tmp), end='')
                self.items.append(tmp)

        else:
            print('\nImpossible!! car not found!')


### Main ###

soi = Stack()

while (True):
    print('======================\nThis is SOI simulation\n======================')
    print('[1] Add car\n[2] Depart car')
    menu = int(input('Enter your command number: '))
    if menu is 1:
        print('')
        soi.push()
        soi.view()
    elif menu is 2:
        soi.depart(int(input('Enter car id: ')))
        print('')
        soi.view()
    else:
        print('\nWrong menu!')

    print('\n\n')
