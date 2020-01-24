'''
    This module contains the code used for testing the functionalities
    of the entire application.
'''

from Test.Test_Elevator import TestElevator



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


    def runTests (self):
        
        '''
            Runs all the tests.
            Input:
                - none
            Output:
                - true, if all the tests pass (all the functionalities work correctly)
                - false, otherwise
        '''
        
        self.__testElevator.runElevatorTests()