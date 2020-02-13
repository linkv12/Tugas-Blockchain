import blockchain_model as bmodel
import blockchain_structure as bstruct

def addBlock_Cli() :
    data = str(input('Input data : '))
    bmodel.addBlock(data)

def printAllBlock() :
    allBlock = bmodel.getAllBlock()
    for block in allBlock :
        print(block)
    x = input('Press Enter...')

def checkChainValidity() :
    pass

def main_UI() :
    isValid = False
    response = 0
    while not isValid :
        print('Main Menu : ')
        print('1. Add Block')
        print('2. Print all block')
        print('3. Check validity')
        print('4. Close')
        try:
            response = int(input('Input : '))
            if response == 4 :
                return response
            elif response == 1 :
                addBlock_Cli()
            elif response == 2 :
                printAllBlock()
            elif response == 3 :
                checkChainValidity()
        except:
            print('Invalid')


def main() :
    stop = False
    while not stop:
        response = main_UI()
        if response == 4 :
            stop = not False