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
        Description:
            - it initializes the controller with the repository
        Input:
            - "repository", the repository to be used
        Output:
            - the controller is initialized with the repository
        '''
        
        self.__repository = repository
        
    
    def addItem (self, item):
        
        '''
        Description:
            - it adds a new item to the repository
        Input:
            - "item", the item to be added to the repository
        Output:
            - the new item is added to the repository, if it is not
              already in it
            - the quantity of the item is increased by 1, if it is
              already in the repository
        '''
        
        self.__repository.addItem(item)