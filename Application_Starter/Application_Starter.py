'''
    This is the starting point of the application.
'''

from Test.Test_All import TestAll
from User_Interface.User_Interface import UserInterface



testAll = TestAll()
userInterface = UserInterface()



testAll.runTests()
userInterface.runApplication()