import argparse

def parse_trading_args():
    parser = argparse.ArgumentParser(description="Run trading script with specified event ID and mode.")
    parser.add_argument("--eventCategory", type=str, help="The category of the event.")

    args = parser.parse_args()

    event_category = args.eventCategory

    return event_category 