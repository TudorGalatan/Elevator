'''
    This module contains all the code used for testing the functionalities
    of the "Floor" module.
'''

from Domain.Floor import Floor



class TestFloor:
    
    '''
        This class defines all the tests for the class "Floor".
    '''
    
    
    def __init__ (self):
        
        '''
            This method initializes the class with some data.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__floor_1 = Floor()
        self.__floor_2 = Floor(True)
        self.__floor_3 = Floor(True, True)
        
        
    def test_getUpButtonPressed (self):
        
        '''
            This method tests the "getUpButtonPressed" method inside the class "Floor".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__floor_1.getUpButtonPressed() == False
        assert self.__floor_2.getUpButtonPressed() == True
        assert self.__floor_3.getUpButtonPressed() == True
        
        
    def test_getDownButtonPressed (self):
        
        '''
            This method tests the "getDownButtonPressed" method inside the class "Floor".
            Input:
                - none
            Output:
                - none
        '''
        
        assert self.__floor_1.getDownButtonPressed() == False
        assert self.__floor_2.getDownButtonPressed() == False
        assert self.__floor_3.getDownButtonPressed() == True
        
        
    def test_setUpButtonPressed (self):
        
        '''
            This method tests the "setUpButtonPressed" method inside the class "Floor".
            Input:
                - none
            Output:
                - none
        '''
        
        self.__floor_1.setUpButtonPressed(True)
        self.__floor_2.setUpButtonPressed(False)
        self.__floor_3.setUpButtonPressed(False)
        
        assert self.__floor_1.getUpButtonPressed() == True
        assert self.__floor_2.getUpButtonPressed() == False
        assert self.__floor_3.getUpButtonPressed() == False
        
        
    def test_setDownButtonPressed (self):
        
        '''
            This method tests the "setDownButtonPressed" method inside the class "Floor".
            Input:
                - none
            Output:
                - none
        '''
        
        self.__floor_1.setDownButtonPressed(True)
        self.__floor_2.setDownButtonPressed(True)
        self.__floor_3.setDownButtonPressed(False)
        
        assert self.__floor_1.getDownButtonPressed() == True
        assert self.__floor_2.getDownButtonPressed() == True
        assert self.__floor_3.getDownButtonPressed() == False
    
    
    def runFloorTests (self):
        
        '''
            This method runs all the floor-related tests.
            Input:
                - none
            Output:
                - none
        '''
        
        self.test_getUpButtonPressed()
        self.test_getDownButtonPressed()
        self.test_setUpButtonPressed()
        self.test_setDownButtonPressed()