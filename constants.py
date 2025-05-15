PROBO_API_URL="https://prod.api.probo.in/api"

API_URLS = {
    "buyBook" : f"{PROBO_API_URL}/v3/tms/trade/bestAvailablePrice?eventId={{eventId}}",
    "eventInfo" : f"{PROBO_API_URL}/v1/product/public/events/{{eventId}}",
    "buyEvent" : f"{PROBO_API_URL}/v1/oms/order/initiate",
    "getAllEvents" : f"{PROBO_API_URL}/v1/product/arena/events/v2"
}