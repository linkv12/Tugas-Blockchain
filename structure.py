import json
import datetime
from hashlib import sha256


class blockChain :
    chain  = []

    def __init__(self):
        self.chain.append(block('0','gene','0','0'))

    def addBlock(self, data):
        temp = self.chain[-1]


        self.chain.append(block(str(int(temp.index) + 1),
                          data, str(datetime.datetime.now()),
                          temp.getHash()))


    def testValidity(self):
        valid = True
        for i in range(0, len(self.chain)-1) :
            if valid :
               # print("--------------------")
               # print(self.chain[i].hashDataTestValid() == self.chain[i].getHash())
               # print("--------------------")
               # print( (self.chain[i+1].getPrevHash() == self.chain[i].getHash()))

               # print("--------------------")
                valid = valid and (self.chain[i].hashDataTestValid() == self.chain[i].getHash()) and (self.chain[i+1].getPrevHash() == self.chain[i].getHash())
            else :
                print('is Valid : %s' % str(valid))
                return False

        valid = valid and self.chain[-1].hashDataTestValid() == self.chain[-1].getHash()
        print('is Valid : %s'  % str(valid))
        return True

    def printAllBlock(self):
        for bloc in self.chain :
            bloc.printBlock()
            print('')




class block :
    index : str
    data : str
    timeStamp : str
    _prevHash : str
    _hash : str

    def __init__(self, index, data, timeStamp, prevHash):
        self.index = index
        self.data = data
        self.timeStamp = timeStamp
        self._prevHash = prevHash
        #print("blk,. %s" % self._prevHash)
        #xx = json.dumps({'index': self.index,
        #                            'data': self.data,
        #                            'timeStamp': timeStamp,
        #                            'prevHash': prevHash})
        #print(type(xx.encode('utf-8')))
        #print(type(json.loads(xx)))
        #print(xx[index] == index)

        self._hash = str(sha256(json.dumps({'index': self.index,
                                    'data': self.data,
                                    'timeStamp': timeStamp,
                                    'prevHash': prevHash}).encode('utf-8')).hexdigest())

    def getPrevHash(self):
        return self._prevHash

    def getHash(self):
        return self._hash

    def hashDataTestValid(self):
        return str(sha256(json.dumps({'index': self.index,
                                    'data': self.data,
                                    'timeStamp': self.timeStamp,
                                    'prevHash': self._prevHash}).encode('utf-8')).hexdigest())

    def printBlock(self):
        print("index : %s" % self.index)
        print("data : %s" % self.data)
        print("timeStamp : %s" % self.timeStamp)
        print("prevHash : %s" % self._prevHash)
        print("_hash : %s" % self._hash)


if __name__ == "__main__" :
    x = ['a', 'b', 'c', 'd', 'e']


    blkChain = blockChain()
    for i in x :
        blkChain.addBlock(i)
    blkChain.printAllBlock()
    blkChain.testValidity()


    #blk = block('0', 'gene', '4/5/20', '0').printBlock()