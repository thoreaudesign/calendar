from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pathlib import Path
from loguru import logger
import os
import pytz
 
# init the calendar
#cal = Calendar()
#cal.add('prodid', '-//Thoreau Design, LLC//Hunt Calendar//')
#cal.add('version', '2.0')

e = open('tmp/de/deer.ics', 'rb')
ecal = Calendar.from_ical(e.read())
for component in ecal.walk():
    logger.info(component)
e.close()
