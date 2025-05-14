from typing import Literal

from constants import API_URLS
from utils.sendAPIRequest import sendAPIRequest

def api_buyEvent( 
    eventId : int, 
    type : Literal[ "yes", "no" ], 
    buyPrice : float,
    bookProfit : float | None = None,
    stopLoss : float | None = None, 
    qty : int = 1
) -> int :

    response = sendAPIRequest( 
        API_URLS["buyEvent"], 
        "POST", 
        payload = {
            "event_id": eventId,
            "offer_type": "buy" if type == "yes"  else "sell",
            "order_type": "LO",
            "l1_order_quantity": qty,
            "l1_expected_price": buyPrice,
            "advanced_options": {
                "book_profit": {
                    "price": bookProfit,
                    "quantity": qty,
                    "disable_trigger": true if bookProfit is None else false 
                },
                "stop_loss": {
                    "price": stopLoss,
                    "quantity": qty,
                    "disable_trigger": true if stopLoss is None else false 
                },
                "auto_cancel": {
                    "minutes": 1,
                    "disable_trigger": true
                }
            }
        }
    )

    print( response )
    return response