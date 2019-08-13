import math, csv, time

class PhoneBookNodeForList:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber


class PhoneBookNodeForBST:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.right = None
        self.left = None

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber


class ListPhoneBook:
    def __init__(self):
        self.array = list()

    def size(self):
        return len(self.array)

    def insert(self, name, phoneNumber):
        newContactInfo = PhoneBookNodeForList(name, phoneNumber)
        self.array.append(newContactInfo)

    def find(self, name):
        if len(self.array) == 0:
            return -1

        for i in self.array:
            if i.getName() == name:
                return i.getPhoneNumber()
        return -1


class BinarySearchTreePhoneBook:
    def __init__(self, root=None):
        self.root = root
        self.length = 0
        if root is not None:
            self.length = 1

    def size(self):
        return self.length

    def insert(self, name, phoneNumber):
        self.length += 1
        if self.root is None:
            self.root = PhoneBookNodeForBST(name, phoneNumber)

        else:
            self.insertHelper(name, phoneNumber, self.root)

    # Helper method for insert function
    @staticmethod
    def insertHelper(name, phoneNumber, currentRoot):
        if currentRoot is None:
            currentRoot = PhoneBookNodeForBST(name, phoneNumber)
            return

        elif name >= currentRoot.getName():
            if currentRoot.right is None:
                currentRoot.right = PhoneBookNodeForBST(name, phoneNumber)
                return
            BinarySearchTreePhoneBook.insertHelper(name, phoneNumber, currentRoot.right)

        else:
            if currentRoot.left is None:
                currentRoot.left = PhoneBookNodeForBST(name, phoneNumber)
                return
            BinarySearchTreePhoneBook.insertHelper(name, phoneNumber, currentRoot.left)

    def find(self, name):
        return self.findHelper(name, self.root)

    @staticmethod
    def findHelper(name, currentPhoneNode):
        if currentPhoneNode is None:
            return -1

        elif currentPhoneNode.getName() == name:
            return currentPhoneNode.getPhoneNumber()

        elif name >= currentPhoneNode.getName():
            return BinarySearchTreePhoneBook.findHelper(name, currentPhoneNode.right)

        else:
            return BinarySearchTreePhoneBook.findHelper(name, currentPhoneNode.left)


def readAndInsertCSVFile(fileName, object):
    with open(fileName) as dataFile:
        phoneBookData = csv.reader(dataFile, delimiter=",")
        for name, phoneNumber in phoneBookData:
            object.insert(name, phoneNumber)

    if object.size() != 1000000:
        raise Exception("ERROR: size of Data in CSV file is not same as data store in the class")


def testForFinding(filename, object):
    found = 0
    with open(filename) as dataFile:
        for name in dataFile:
            if object.find(name.strip()) == -1:
               raise Exception("ERROR!!!!:  the given is not found!!!")
            else:
                found += 1
    return found

# TESTING
def finalResult():
    myListPhoneBook = ListPhoneBook()
    startListInsert = time.time()
    readAndInsertCSVFile("data.csv", myListPhoneBook)
    endListInsert = time.time()
    findCalledList = testForFinding("search.txt", myListPhoneBook)
    endListFind = time.time()
    elapsed_time_insert = endListInsert - startListInsert
    elapsed_time_searching = endListFind - endListInsert
    print("----------------------- LISTPHONEBOOK -------------------------")
    print("Insert took {0:.0f} millisecond.".format(elapsed_time_insert * 1000))
    print("The size of the PhoneBook is {}.".format(myListPhoneBook.size()))
    print("find() was called {} times.".format(findCalledList))
    print("Search took {0:.0f} millisecond.".format(elapsed_time_searching * 1000))

    myBSTPhoneBook = BinarySearchTreePhoneBook()
    startBSTInsert = time.time()
    readAndInsertCSVFile("data.csv", myBSTPhoneBook)
    endBSTInsert = time.time()
    findCalledBST = testForFinding("search.txt", myBSTPhoneBook)
    endBSTFind = time.time()
    elapsed_time_insertBST = endBSTInsert - startBSTInsert
    elapsed_time_searchingBST = endBSTFind - endBSTInsert
    print("----------------------- BSTPHONEBOOK -------------------------")
    print("Insert took {0:.0f} millisecond.".format(elapsed_time_insertBST * 1000))
    print("The size of the PhoneBook is {}.".format(myBSTPhoneBook.size()))
    print("find() was called {} times.".format(findCalledList))
    print("Search took {0:.0f} millisecond.".format(elapsed_time_searchingBST * 1000))

if __name__ == "__main__":
    finalResult()


"""
----------------------- LISTPHONEBOOK -------------------------
Insert took 2575 millisecond.
The size of the PhoneBook is 1000000.
find() was called 1000 times.
Search took 89641 millisecond.
----------------------- BSTPHONEBOOK -------------------------
Insert took 21611 millisecond.
The size of the PhoneBook is 1000000.
find() was called 1000 times.
Search took 19 millisecond.

3. In ListPhoneBook the insert is O(1) and search is O(n) too, since it is unsorted List and appending in list is O(1)
   In BSTPhoneBook the insert is O(H) and search is O(H) where H being a height of BST
   So, for inserting, List is much faster, and for searching BST is way faster than list.
"""



