'''
    This module contains the class that defines a floor.
'''



class Floor:
    
    '''
        This class defines a floor.
    '''
    
    
    def __init__ (self, upButtonPressed = False, downButtonPressed = False):
        
        '''
            This method initializes a floor with the given or the implicit
            values for its attributes.
            Input:
                - "upButtonPressed": the truth value that shows if a button
                was pressed for an elevator to go upwards
                - "downButtonPressed": the truth value that shows if a button
                was pressed for an elevator to go downwards
            Output:
                - none
        '''
        
        self.__upButtonPressed = upButtonPressed
        self.__downButtonPressed = downButtonPressed
        
        
    def getUpButtonPressed (self):
        
        '''
            This method returns the current value of the "upButtonPressed" attribute,
            so it can be accessed from outside the class.
            Input:
                - none
            Output:
                - "upButtonPressed": the current value of the "upButtonPressed" attribute
        '''
        
        upButtonPressed = self.__upButtonPressed
        
        return upButtonPressed
    
    
    def getDownButtonPressed (self):
        
        '''
            This method returns the current value of the "downButtonPressed" attribute,
            so it can be accessed from outside the class.
            Input:
                - none
            Output:
                - "downButtonPressed": the current value of the "downButtonPressed" attribute
        '''
        
        downButtonPressed = self.__downButtonPressed
        
        return downButtonPressed
    
    
    def setUpButtonPressed (self, upButtonPressed):
        
        '''
            This method sets the current value of the "upButtonPressed" attribute.
            Input:
                - "upButtonPressed": the truth value that shows if a button
                was pressed for an elevator to go upwards
            Output:
                - none
        '''
        
        self.__upButtonPressed = upButtonPressed
        
        
    def setDownButtonPressed (self, downButtonPressed):
        
        '''
            This method sets the current value of the "downButtonPressed" attribute.
            Input:
                - "downButtonPressed": the truth value that shows if a button
                was pressed for an elevator to go downwards
            Output:
                - none
        '''
        
        self.__downButtonPressed = downButtonPressed