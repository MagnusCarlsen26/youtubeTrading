import argparse

def parse_trading_args():
    parser = argparse.ArgumentParser(description="Run trading script with specified event ID and mode.")
    parser.add_argument("--eventId", type=int, help="The event ID for the trading operation.")
    parser.add_argument("--mode", type=str, choices=['dev', 'prod'], help="The mode for the trading operation (can be 'dev' or 'prod').")
    parser.add_argument("--buyQty", type=int, help="The quantity to buy. Required in 'prod' mode.")

    args = parser.parse_args()

    if args.mode == "prod" and args.buyQty is None:
        parser.error("BUY_QTY is required when mode is 'prod'.")

    event_id = args.eventId
    mode = args.mode

    if mode == "dev" :
        buy_qty = 1
    elif mode == "prod":
        buy_qty = args.buyQty
        
    return event_id, mode, buy_qty 