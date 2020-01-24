'''
    This module contains the class that defines an elevator.
'''



class Elevator:
    
    '''
        This class defines an elevator.
    '''
    
    
    def __init__ (self, currentFloor = 0, currentState = "going nowhere"):
        
        '''
            This method initializes an elevator with the given or the implicit
            values for its attributes.
            Input:
                - "currentFloor": the current floor
                - "currentState": the current state
            Output:
                - none
        '''
        
        self.__currentFloor = currentFloor
        self.__currentState = currentState
        
        
    def getCurrentFloor (self):
        
        '''
            This method returns the current floor, so it can be accessed from
            outside the class.
            Input:
                - none
            Output:
                - "currentFloor": the current floor
        '''
        
        currentFloor = self.__currentFloor
        
        return currentFloor
    
    
    def getCurrentState (self):
        
        '''
            This method returns the current state, so it can be accessed from
            outside the class.
            Input:
                - none
            Output:
                - "currentState": the current state
        '''
        
        currentState = self.__currentState
        
        return currentState
    
    
    def setCurrentFloor (self, currentFloor):
        
        '''
            This method sets the current floor to its new value.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__currentFloor = currentFloor
        
        
    def setCurrentState (self, currentState):
        
        '''
            This method sets the current state to its new value.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__currentState = currentState