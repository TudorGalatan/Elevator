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
    
    
    def callElevator (self, currentFloorIndex, direction):
        
        '''
            It calls an elevator from a floor.
            Input:
                - "currentFloorIndex": the current floor
            Output:
                - "direction": the direction
        '''
        
        self.__repository.callElevator(currentFloorIndex, direction)
        
        
    def selectDestination (self, destination):
        
        '''
            Once the elevator came to your floor and you enter the elevator,
            you have to select a destination. This functionality is managed
            by this method.
            Input:
                - "destination": the destination
            Output:
                - none
        '''
        
        self.__repository.selectDestination(destination)
        
    
    def reachDestination (self):
        
        '''
            Once you selected the desired destination, the elevator takes its time to reach
            it and when it does, the states change again. This functionality is managed
            by this method.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__repository.reachDestination()