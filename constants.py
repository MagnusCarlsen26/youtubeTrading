PROBO_API_URL="https://prod.api.probo.in/api"

API_URLS = {
    "buyBook" : f"{PROBO_API_URL}/v3/tms/trade/bestAvailablePrice?eventId={{eventId}}",
    "eventInfo" : f"{PROBO_API_URL}/v1/product/public/events/{{eventId}}",
    "buyEvent" : f"{PROBO_API_URL}/v1/oms/order/initiate",
    "getAllEvents" : f"{PROBO_API_URL}/v1/product/arena/events/v2"
}

TOPIC_IDS = {
    "youtube" : 452,
    "bitcoin" : 2449
}

CSV_HEADERS = [
    'timestamp',
    '0.5',
    '1.0',
    '1.5',
    '2.0',
    '2.5',
    '3.0',
    '3.5',
    '4.0',
    '4.5',
    '5.0',
    '5.5',
    '6.0',
    '6.5',
    '7.0',
    '7.5',
    '8.0',
    '8.5',
    '9.0',
    '9.5'
]

PROMPTS = {
    "youtube" : """
        I will give you a sentence please extract the following information :
        1. Target Views.
        2. Target Time.
        3. Video Title.

        Output format -
        Your resopnse should be in JSON format. JSON Format -  
        {{
            targetNumber : int,
            targetTime : HH:MM AM/PM,
            title : str
        }}

        If you can't find one or more fields then please respond with text ( not json ) about why you can't find the info

        Here is the question - {question}
    """,
    "bitcoin" : """
        I will give you a sentence please extract the following information :
        1. Target Views.
        2. Target Time.
        3. Video Title.

        Output format -
        Your resopnse should be in JSON format. JSON Format -  
        {{
            targetNumber : int,
            targetTime : HH:MM AM/PM,
            title : str
        }}

        If you can't find one or more fields then please respond with text ( not json ) about why you can't find the info

        Here is the question - {question}
    """
}