import requests
from datetime import datetime

#this converts a timestamp in epoch seconds to a regular HH:MM in military time
def convertToTimestamp(currentTimestamp):
    format = "%H:%M"
    t = datetime.fromtimestamp(currentTimestamp)
    stopTimestamp = t.strftime(format)
    return stopTimestamp