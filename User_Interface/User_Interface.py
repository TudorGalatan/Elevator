'''
    This module contains the definition of the class used to represent the
    user interface.
'''



class UserInterface:
    
    '''
        This class contains the definition of the user interface.
    '''
    
    
    def __init__ (self):
        
        '''
            It initializes the user interface with a controller.
            Input:
                - "controller": the controller to be used
            Output:
                - none
        '''
        
        pass
        
        '''self.__controller = controller'''
        
        
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
                pass
            
            elif option == 2:
                pass
            
            elif option == 3:
                pass
            
            else:
                print("\nThis is not a valid option. Please try again.\n")