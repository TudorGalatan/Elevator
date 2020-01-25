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
    
    
    def callElevator (self, currentFloorIndex, direction):
        
        '''
            It calls an elevator from a floor.
            Input:
                - "currentFloorIndex": the current floor
                - "direction": the direction
            Output:
                - none
        '''
        
        # if you want to go up
        if direction == 0:      
            self.__listOfFloors[currentFloorIndex].setUpButtonPressed(True)
        # if you want to go down
        else:
            self.__listOfFloors[currentFloorIndex].setDownButtonPressed(True)
        
        # Find the nearest elevator.
        elevator_A_currentFloor = self.__elevator_A.getCurrentFloor()
        elevator_B_currentFloor = self.__elevator_B.getCurrentFloor()
        
        if elevator_A_currentFloor >= currentFloorIndex:
            distanceToElevatorA = elevator_A_currentFloor - currentFloorIndex
        else:
            distanceToElevatorA = currentFloorIndex - elevator_A_currentFloor
            
        if elevator_B_currentFloor >= currentFloorIndex:
            distanceToElevatorB = elevator_B_currentFloor - currentFloorIndex
        else:
            distanceToElevatorB = currentFloorIndex - elevator_B_currentFloor
            
        if distanceToElevatorA > distanceToElevatorB:
            nearestElevatorName = "B"
            nearestElevator = self.__elevator_B
        elif distanceToElevatorB > distanceToElevatorA:
            nearestElevatorName = "A"
            nearestElevator = self.__elevator_A
        else:
            if elevator_A_currentFloor <= elevator_B_currentFloor:
                nearestElevatorName = "A"
                nearestElevator = self.__elevator_A
            else:
                nearestElevatorName = "B"
                nearestElevator = self.__elevator_B
                
        initialFloor = nearestElevator.getCurrentFloor()
        if initialFloor >= currentFloorIndex:
            if nearestElevatorName == "A":
                self.__elevator_A.setCurrentState("going down")
            else:
                self.__elevator_B.setCurrentState("going down")
        else:
            if nearestElevatorName == "A":
                self.__elevator_A.setCurrentState("going up")
            else:
                self.__elevator_B.setCurrentState("going up")