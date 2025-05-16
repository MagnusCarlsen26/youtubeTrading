PROBO_API_URL="https://prod.api.probo.in/api"

API_URLS = {
    "buyBook" : f"{PROBO_API_URL}/v3/tms/trade/bestAvailablePrice?eventId={{eventId}}",
    "eventInfo" : f"{PROBO_API_URL}/v1/product/public/events/{{eventId}}",
    "buyEvent" : f"{PROBO_API_URL}/v1/oms/order/initiate",
    "getAllEvents" : f"{PROBO_API_URL}/v1/product/arena/events/v2"
}

TOPIC_IDS = {
    "youtube" : 452
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