def sendAPICallback( apiFunction : callable ) :

    try : return apiFunction()
    
    except Exception as e :

        print( f"Error Occured in {sendAPICallback.__name__}" )
        print( e )

        raise Exception( e )