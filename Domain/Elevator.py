'''
    This module contains the class that defines an elevator.
'''



class Elevator:
    
    '''
        This class defines an elevator.
    '''
    
    
    def __init__ (self, currentFloor = 0, currentStatus = None):
        
        '''
            This method initializes an elevator with the given or the implicit
            values for its attributes.
            Input:
                - "currentFloor": the current floor
                - "currentStatus": the current status
            Output:
                - none
        '''
        
        self.__currentFloor = currentFloor
        self.__currentStatus = currentStatus
        
        
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
    
    
    def getCurrentStatus (self):
        
        '''
            This method returns the current status, so it can be accessed from
            outside the class.
            Input:
                - none
            Output:
                - "currentStatus": the current status
        '''
        
        currentStatus = self.__currentStatus
        
        return currentStatus
    
    
    def setCurrentFloor (self, currentFloor):
        
        '''
            This method sets the current floor to its new value.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__currentFloor = currentFloor
        
        
    def setCurrentStatus (self, currentStatus):
        
        '''
            This method sets the current status to its new value.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__currentStatus = currentStatus