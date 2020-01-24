'''
    This module contains all the code used for testing the functionalities
    of the "Elevator" module.
'''

from Domain.Elevator import Elevator



class TestElevator:
    
    '''
        This class defines all the tests for the class "Elevator".
    '''
    
    
    def __init__ (self):
        
        '''
            This method initializes the class with some data.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__elevator_1 = Elevator(0)
        self.__elevator_2 = Elevator(3)
        self.__elevator_3 = Elevator(6)
        
        
    def test_getCurrentFloor (self):
        
        '''
            This method tests the "getCurrentFloor" method inside the class "Elevator".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__elevator_1.getCurrentFloor() == 0
        assert self.__elevator_2.getCurrentFloor() == 3
        assert self.__elevator_3.getCurrentFloor() == 6
        
        
    def test_setCurrentFloor (self):
        
        '''
            This method tests the "setCurrentFloor" method inside the class "Elevator".
            Input:
                - none
            Output:
                - none
        '''
        
        self.__elevator_1.setCurrentFloor(6)
        self.__elevator_2.setCurrentFloor(4)
        self.__elevator_3.setCurrentFloor(0)
        
        assert self.__elevator_1.getCurrentFloor() == 6
        assert self.__elevator_2.getCurrentFloor() == 4
        assert self.__elevator_3.getCurrentFloor() == 0
        
    
    def runElevatorTests (self):
        
        '''
            This method runs all the elevator-related tests.
            Input:
                - none
            Output:
                - none
        '''
        
        self.test_getCurrentFloor()
        self.test_setCurrentFloor()