'''
    This module contains the class that defines an elevator.
'''



class Elevator:
    
    '''
        This class defines an elevator.
    '''
    
    
    def __init__ (self, currentFloor):
        
        '''
            This method initializes an elevator with the given or the implicit
            values for its attributes.
            Input:
                - "currentFloor": the current floor
            Output:
                - None
        '''
        
        self.__currentFloor = currentFloor
        
        
    def getCurrentFloor (self):
        
        '''
            This method returns the current floor, so it can be accessed from
            outside the class.
            Input:
                - None
            Output:
                - "currentFloor": the current floor
        '''
        
        currentFloor = self.__currentFloor
        
        return currentFloor
    
    
    def setCurrentFloor (self, currentFloor):
        
        '''
            This method sets the current floor to its new value.
            Input:
                - None
            Output:
                - "currentFloor": the current floor
        '''
        
        self.__currentFloor = currentFloor