'''
    This module contains the code used for testing the functionalities
    of the entire application.
'''

from Test.Test_Elevator import TestElevator
from Test.Test_Floor import TestFloor
from Test.Test_Repository import TestRepository



class TestAll:
    
    '''
        This class tests all the functionalities of the application.
    '''
    
    
    def __init__ (self):
        
        '''
            This method initializes the class with some data.
            Input:
                - none
            Output:
                - none
        '''

        self.__testElevator = TestElevator()
        self.__testFloor = TestFloor()
        self.__testRepository = TestRepository()


    def runTests (self):
        
        '''
            Runs all the tests.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__testElevator.runElevatorTests()
        self.__testFloor.runFloorTests()
        '''self.__testRepository.runRepositoryTests()'''