'''
    This is the starting point of the application.
'''

from Test.Test_All import TestAll
from Repository.Repository import Repository
from Controller.Controller import Controller
from User_Interface.User_Interface import UserInterface



# Initialize the necessary objects.
testAll = TestAll()
repository = Repository()
controller = Controller(repository)
userInterface = UserInterface(controller)



# Run the tests and start the application.
testAll.runTests()
userInterface.runApplication()