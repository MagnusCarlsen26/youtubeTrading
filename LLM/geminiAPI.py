import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

assert os.getenv("GEMINI_API_KEY"), "Please Enter Gemini Key."
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def geminiAPI( prompt : str ) -> str :
    
    genai.configure( api_key = GEMINI_API_KEY )

    model = genai.GenerativeModel( 'gemini-2.0-flash' )

    try :

        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        
        print( "Error Occured while calling Gemini." )
        print( e )

        raise Exception( "Error Occured while calling Gemini." )