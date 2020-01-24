'''
    This module contains all the code used for testing the functionalities
    of the "Repository" module.
'''

from Repository.Repository import Repository
from Domain.Elevator import Elevator
from Domain.Floor import Floor



class TestRepository:
    
    '''
        This class defines all the tests for the class "Repository".
    '''
    
    
    def __init__ (self):
        
        '''
            This method initializes the class with some data.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__repository = Repository()
        
        self.__elevator_1 = Elevator()
        self.__elevator_2 = Elevator(6)
        
        self.__floor = Floor()
        
        self.__listOfFloors = []
        for index in range (0, 7):
            self.__listOfFloors.append(self.__floor)
        
        
    def test_getElevator (self):
        
        '''
            This method tests the "getElevator" method inside the class "Repository".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__repository.getElevator("A") == self.__elevator_1
        assert self.__repository.getElevator("B") == self.__elevator_2
        
        
    def test_getListOfFloors (self):
        
        '''
            This method tests the "getListOfFloors" method inside the class "Repository".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__repository.getListOfFloors() == self.__listOfFloors
        
        
    def test_getFloor (self):
        
        '''
            This method tests the "getFloor" method inside the class "Repository".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__repository.getFloor(0) == self.__floor
        assert self.__repository.getFloor(3) == self.__floor
        assert self.__repository.getFloor(6) == self.__floor
    
    
    def runRepositoryTests (self):
        
        '''
            This method runs all the repository-related tests.
            Input:
                - none
            Output:
                - none
        '''
        
        self.test_getElevator()
        self.test_getListOfFloors()
        self.test_getFloor()