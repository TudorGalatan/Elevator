'''
    This is the starting point of the application.
'''

from Test.Test_All import TestAll
from Repository.Repository import Repository
from Controller.Controller import Controller
from User_Interface.User_Interface import UserInterface



testAll = TestAll()
repository = Repository()
controller = Controller(repository)
userInterface = UserInterface(controller)



testAll.runTests()
userInterface.runApplication()