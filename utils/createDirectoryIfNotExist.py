import os

def createDirectoryIfNotExist( filePath : str ):

    directory = os.path.dirname( filePath )
    
    if not os.path.exists( directory ) :
        
        os.makedirs( directory ) 