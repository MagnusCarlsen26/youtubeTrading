import csv
from utils.createDirectoryIfNotExist import createDirectoryIfNotExist

def writeCSV( filePath : str, data : list[str] ) :

    createDirectoryIfNotExist( filePath )
    
    with open( filePath, 'a' ) as csvfile :

        writer = csv.writer( csvfile )
        writer.writerow( data )