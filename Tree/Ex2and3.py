class EmployeeNode:
    def __init__(self, name, title, directReport=[]):
        self.name = name
        self.title = title
        self.directReport = directReport

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getDirectReport(self):
        return self.directReport

    def __str__(self):
        return "Name: {}, Title: {}".format(self.name, self.title)


class OrganizationStructure:
    def __init__(self, ceo):
        self.ceo = ceo
        self.level = 0

    def getLevel(self):
        return self.level

    def printLevelByLevel(self):
        root = self.ceo
        print(root)
        print("\n")
        if self.level == 0:
            self.level += 1
        lowerLevel_list = list(root.getDirectReport())
        self.printLevelByLevelHelper(lowerLevel_list)


    def printLevelByLevelHelper(self, lowerLevelList):
        if len(lowerLevelList) == 0:
            return

        nextLowerLevel = list()
        for employee in lowerLevelList:
            print(employee)
            nextLowerLevel += list(employee.getDirectReport())
        print("\n")
        if self.level == 0:
            self.level += 1

        self.printLevelByLevelHelper(nextLowerLevel)

    # we check if printLevelByLevel function is called, if not called then need to find the level else,
    # printLevelByLevel has already found the level.
    def printNumLevels(self):
        if self.level > 0:
            print(self.getLevel())
        else:
            root = self.ceo
            self.level += 1
            lowerLevel_list = list(root.getDirectReport())
            self.printNumLevelsHelper(lowerLevel_list)
            print(self.getLevel())

    # it is same as printLevelByLevelHelper function
    def printNumLevelsHelper(self, lowerLevelList):
                if len(lowerLevelList) == 0:
                    return

                nextLowerLevel = list()
                for employee in lowerLevelList:
                    nextLowerLevel += list(employee.getDirectReport())
                self.level += 1

                self.printNumLevelsHelper(nextLowerLevel)



K = EmployeeNode("K", "Sales Intern", [])
J = EmployeeNode("J", "Sales Representative", [K])
F = EmployeeNode("F", "Engineer", [])
G = EmployeeNode("G", "Engineer", [])
H = EmployeeNode("H", "Engineer", [])
I = EmployeeNode("I", "Director", [J])
D = EmployeeNode("D", "Manager", [F, G, H])
E = EmployeeNode("E", "Manager", [])
B = EmployeeNode("B", "CFO", [I])
C = EmployeeNode("C", "CTO", [D, E])
A = EmployeeNode("A", "CEO", [B, C])


company = OrganizationStructure(A)
print("number of level is ", end = " ")
company.printNumLevels()
print("\n")
company.printLevelByLevel()
print("number of level is ", end = " ")
company.printNumLevels()



"""   --------------- RUN ---------------
number of level is  5


Name: A, Title: CEO


Name: B, Title: CFO
Name: C, Title: CTO


Name: I, Title: Director
Name: D, Title: Manager
Name: E, Title: Manager


Name: J, Title: Sales Representative
Name: F, Title: Engineer
Name: G, Title: Engineer
Name: H, Title: Engineer


Name: K, Title: Sales Intern


number of level is  5

"""

