'''
    This module contains the definition of the class used to represent the user interface.
'''



class UserInterface:
    
    '''
        This class contains the definition of the user interface.
    '''
    
    
    def __init__ (self, controller):
        
        '''
            It initializes the user interface with a controller.
            Input:
                - "controller": the controller to be used
            Output:
                - none
        '''
        
        self.__controller = controller
        
        
    def printMenu (self):
        
        '''
            It prints the menu with the available options on the screen.
            Input:
                - none
            Output:
                - none
        '''
        
        print("\n\t\tMENU\n\n")
        print("The available options are:\n")
        print("0: Exit the application.\n")
        print("1: For each elevator, display its current state.\n")
        print("2: For each floor, display which elevator is going up/down.\n")
        print("3: Call an elevator.\n")
        print("4: Select a destination.\n")
        print("5: Reach the destination.\n")
        
        
    def displayCurrentStateOfElevators (self):
        
        '''
            For each elevator, it displays its current state.
            Input:
                - none
            Output:
                - none
        '''
        
        stateOfElevatorA = self.__controller.getStateOfElevator("A")
        stateOfElevatorB = self.__controller.getStateOfElevator("B")
        
        print("\nThe current state of elevator A is: ", stateOfElevatorA, "\n")
        print("The current state of elevator B is: ", stateOfElevatorB, "\n")
        
        
    def displayWhichElevatorisGoingUpDown (self):
        
        '''
            For each floor, it displays which elevator is going up/down.
            Input:
                - none
            Output:
                - none
        '''
        
        for floor in range (7):
            stateOfElevatorA = self.__controller.getStateOfElevator("A")
            stateOfElevatorB = self.__controller.getStateOfElevator("B")
            print("For the floor ", floor, ", elevator A is ", stateOfElevatorA, "\n")
            print("For the floor ", floor, ", elevator B is ", stateOfElevatorB, "\n")
            
    
    def callElevator (self):
        
        '''
            It calls an elevator from a given floor.
            Input:
                - none
            Output:
                - none
        '''
        
        # Find the index of the current floor for the person calling the elevator.
        print("\nOn which floor are you right now?")
        currentFloorIndex = int(input("Type a number between 0 and 6: "))
        
        # Find the direction in which the person calling the elevator wants to go.
        print("\nWhere do you want to go?")
        direction = int(input("Type 0 for up or 1 for down: "))
        
        self.__controller.callElevator(currentFloorIndex, direction)
        
        
    def selectDestination (self):
        
        '''
            Once the elevator came to the current floor for the person calling the elevator,
            the person must select a destination floor. This functionality is managed by
            this method.
            Input:
                - none
            Output:
                - none
        '''
        
        # Find the index of the floor to which the person calling the elevator wants to go.
        print("\nWhere do you want to go?")
        destination = int(input("Type a number between 0 and 6: "))
        
        self.__controller.selectDestination(destination)
        
        
    def reachDestination (self):
        
        '''
            Once the person calling the elevator has selected the desired destination floor,
            the elevator takes its time to reach it and when it does, the states change again.
            This functionality is managed by this method.
            Input:
                - none
            Output:
                - none
        '''
        
        self.__controller.reachDestination()
        

    def runApplication (self):
        
        '''
            It starts running the user interface.
            Input:
                - none
            Output:
                - none
        '''
        
        while (True):
            
            self.printMenu()
            option = int(input("\nType the number associated with the desired option: "))
            
            # Exits the application.
            if option == 0:
                exit()
                
            # For each elevator, its current state is displayed.
            elif option == 1:
                self.displayCurrentStateOfElevators()
            
            # For each floor, the state of the elevators is displayed.
            elif option == 2:
                self.displayWhichElevatorisGoingUpDown()
            
            # Allows the user to call an elevator.
            elif option == 3:
                self.callElevator()
            
            # Allows the user to select a destination floor.
            elif option == 4:
                self.selectDestination()
            
            # Reaches the destination.
            elif option == 5:
                self.reachDestination()
            
            # If the user gave an invalid option, an error message is displayed.
            else:
                print("\nThis is not a valid option. Please try again.\n\n")