'''
    This module contains the definition of the class used to represent the
    user interface.
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
        print("0. Exit the application.\n")
        print("1. For each elevator, display its current state.\n")
        print("2. For each floor, display which elevator is going up/down.\n")
        print("3. Call an elevator.\n")
        print("4. Select destination.\n")
        print("5. Reach destination.\n")
        
        
    def displayCurrentStateOfElevators (self):
        
        '''
            For each elevator, it displays its current state.
            Input:
                - none
            Output:
                - none
        '''
        
        stateElevatorA = self.__controller.getStateOfElevator("A")
        stateElevatorB = self.__controller.getStateOfElevator("B")
        
        print("\nThe current state of elevator A is: ", stateElevatorA, "\n")
        print("The current state of elevator B is: ", stateElevatorB, "\n")
        
        
    def displayWhichElevatorisGoingUpDown (self):
        
        '''
            For each floor, it displays which elevator is going up/down.
            Input:
                - none
            Output:
                - none
        '''
        
        for index in range (0, 7):
            stateElevatorA = self.__controller.getStateOfElevator("A")
            stateElevatorB = self.__controller.getStateOfElevator("B")
            print("For the floor ", index, ", elevator A is ", stateElevatorA, "\n")
            print("For the floor ", index, ", elevator B is ", stateElevatorB, "\n")
            
    
    def callElevator (self):
        
        '''
            It calls an elevator from a floor.
            Input:
                - none
            Output:
                - none
        '''
        
        print("On which floor are you right now?")
        print("Type a number between 0 and 6: ")
        
        currentFloor = int(input())
        
        print("\nWhere do you want to go?")
        print("Type 0 for up or 1 for down: ")
        
        direction = input()
        
        self.__controller.callElevator(currentFloor, direction)
        

    def runApplication (self):
        
        '''
            It starts the user interface.
            Input:
                - none
            Output:
                - none
        '''
        
        while (True):
            
            self.printMenu()
            print("Type the number associated with the desired option: ")
            option = int(input())
            
            if option == 0:
                exit()
                
            elif option == 1:
                self.displayCurrentStateOfElevators()
            
            elif option == 2:
                self.displayWhichElevatorisGoingUpDown()
            
            elif option == 3:
                self.callElevator()
            
            elif option == 4:
                pass
            
            elif option == 5:
                pass
            
            else:
                print("\nThis is not a valid option. Please try again.\n")