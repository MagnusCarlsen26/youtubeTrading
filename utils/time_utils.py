import datetime
import pytz

def is_current_time_before_target(targetTime: str) -> bool:
    """
    Compares the current IST time with a target time string (HH : MM AM/PM).

    Args:
        targetTime: The target time string in "HH : MM AM/PM" format.

    Returns:
        True if the current IST time is before the target time, False otherwise.
    """
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

    # Parse targetTime into a datetime object for today
    try:
        target_dt_str = datetime.datetime.now().strftime("%Y-%m-%d") + " " + targetTime
        target_dt = datetime.datetime.strptime(target_dt_str, "%Y-%m-%d %I:%M %p").replace(tzinfo=ist_tz)
    except ValueError as e:
        print(f"Error parsing target time '{targetTime}': {e}")
        # If parsing fails, we cannot proceed with the comparison, so return False (or handle as an error)
        return False # Or raise an exception depending on desired error handling

    # Get current time in IST
    current_ist_time = datetime.datetime.now(ist_tz)

    # Return True if current time is before target time, False otherwise
    return current_ist_time < target_dt 

def get_current_time_ist():
    current_time_utc = datetime.datetime.now(datetime.timezone.utc)
    ist = pytz.timezone('Asia/Kolkata')
    current_time_ist = current_time_utc.astimezone(ist)
    return current_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z%z') 