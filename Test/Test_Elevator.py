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
        
        self.__elevator_1 = Elevator()
        self.__elevator_2 = Elevator(3, "going up")
        self.__elevator_3 = Elevator(6, "going down")
        
        
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
        
        
    def test_getCurrentStatus (self):
        
        '''
            This method tests the "getCurrentStatus" method inside the class "Elevator".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__elevator_1.getCurrentStatus() == None
        assert self.__elevator_2.getCurrentStatus() == "going up"
        assert self.__elevator_3.getCurrentStatus() == "going down"
        
        
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
        
        
    def test_setCurrentStatus (self):
        
        '''
            This method tests the "setCurrentStatus" method inside the class "Elevator".
            Input:
                - none
            Output:
                - none
        '''
        
        self.__elevator_1.setCurrentStatus("going up")
        self.__elevator_2.setCurrentStatus("going down")
        self.__elevator_3.setCurrentStatus("going up")
        
        assert self.__elevator_1.getCurrentStatus() == "going up"
        assert self.__elevator_2.getCurrentStatus() == "going down"
        assert self.__elevator_3.getCurrentStatus() == "going up"
    
    
    def runElevatorTests (self):
        
        '''
            This method runs all the elevator-related tests.
            Input:
                - none
            Output:
                - none
        '''
        
        self.test_getCurrentFloor()
        self.test_getCurrentStatus
        self.test_setCurrentFloor()
        self.test_setCurrentStatus()