'''
    This module contains the code used for testing the functionalities
    of the entire application.
'''

from Test.Test_Elevator import TestElevator



def runTests ():
    
    '''
        Runs all the tests.
        Input:
            - None
        Output:
            - True, if all the tests pass (all the functionalities work correctly)
            - False, otherwise
    '''
    
    test_elevator = TestElevator()
    
    test_elevator.runElevatorTests()