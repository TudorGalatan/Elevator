'''
    This module contains the definition of the class used to control the
    operations performed on the application.
'''



class Controller:
    
    '''
        It defines the controller.
    '''
    
    
    def __init__ (self, repository):
        
        '''
            It initializes the controller with the repository
            Input:
                - "repository", the repository to be used
            Output:
                - none
        '''
        
        self.__repository = repository
        
    
    def getStateOfElevator (self, elevatorName):
        
        '''
            This method returns the state of the elevator.
            Input:
                - "elevatorName": the name of the elevator
            Output:
                - "state": the state of the elevator
        '''
        
        state = self.__repository.getStateOfElevator(elevatorName)
        
        return state
    
    
    def callElevator (self, currentFloor, direction):
        
        '''
            It calls an elevator from a floor.
            Input:
                - "currentFloor": the current floor
            Output:
                - "direction": the direction
        '''
        
        self.__repository.callElevator(currentFloor, direction)