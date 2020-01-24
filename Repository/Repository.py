'''
    This module contains the definition of the class used to represent
    the repository of the application.
'''

from Domain.Elevator import Elevator
from Domain.Floor import Floor



class Repository:
    
    '''
        This class defines the repository of the application.
    '''
    
    
    def __init__ (self):
        
        '''
            This method initializes the repository of the application
            with two elevators and seven floors.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__elevator_A = Elevator()
        self.__elevator_B = Elevator(6)
        
        self.__listOfFloors = []
        floor = Floor()
        
        for index in range (0, 7):
            self.__listOfFloors.append(floor)
            
            
    def getElevator (self, elevatorName):
        
        '''
            This method returns the elevator (either "A" or "B").
            Input:
                - "elevatorName": the name of the elevator
            Output:
                - "elevator": the elevator
        '''
        
        if elevatorName == "A":
            elevator = self.__elevator_A
        else:
            elevator = self.__elevator_B
        
        return elevator
        
        
    def getListOfFloors (self):
        
        '''
            This method returns the list of floors.
            Input:
                - none
            Output:
                - "listOfFloors": the list of floors
        '''
        
        listOfFloors = self.__listOfFloors
        
        return listOfFloors
    
    
    def getFloor (self, index):
        
        '''
            This method returns the floor with the specified index.
            Input:
                - "index": the given index
            Output:
                - "floor": the element on the given position
        '''
        
        floor = self.__listOfFloors[index]
        
        return floor
    
    
    def getStateOfElevator (self, elevatorName):
        
        '''
            This method returns the state of the elevator.
            Input:
                - "elevatorName": the name of the elevator
            Output:
                - "state": the state of the elevator
        '''
        
        if elevatorName == "A":
            elevator = self.__elevator_A
        else:
            elevator = self.__elevator_B
            
        state = elevator.getCurrentState()
        
        return state
    
    
    def callElevator (self, currentFloor, direction):
        
        '''
            It calls an elevator from a floor.
            Input:
                - "currentFloor": the current floor
            Output:
                - "direction": the direction
        '''
        
        elevator_A_currentFloor = self.__elevator_A.getCurrentFloor()
        elevator_B_currentFloor = self.__elevator_B.getCurrentFloor()
        
        
        if elevator_A_currentFloor >= currentFloor:
            distanceToElevatorA = elevator_A_currentFloor - currentFloor
        else:
            distanceToElevatorA = currentFloor - elevator_A_currentFloor
            
        if elevator_B_currentFloor >= currentFloor:
            distanceToElevatorB = elevator_B_currentFloor - currentFloor
        else:
            distanceToElevatorB = currentFloor - elevator_B_currentFloor
            
        if distanceToElevatorA > distanceToElevatorB:
            nearestElevator = self.__elevator_B
        elif distanceToElevatorB > distanceToElevatorA:
            nearestElevator = self.__elevator_A
        else:
            if elevator_A_currentFloor <= elevator_B_currentFloor:
                nearestElevator = self.__elevator_A
            else:
                nearestElevator = self.__elevator_B
                
        