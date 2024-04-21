from datetime import date
import calendar

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

DESCRIPTION_LIST = {
    "first": 1,
    "second": 8,
    "third": 15,
    "fourth": 22,
    "fifth": 29,
    "teenth": 13,
    "last": None
}

LIST_OF_WEEKDAYS = list(calendar.day_name)

def meetup(year, month, week, day_of_week):
    if DESCRIPTION_LIST.get(week):
        start_meetup_day = DESCRIPTION_LIST.get(week)
    else:
        start_meetup_day = calendar.monthrange(year, month)[1] - 6

    try:
        target_day = LIST_OF_WEEKDAYS.index(day_of_week)
        start_week_day = calendar.weekday(year, month, start_meetup_day)
        diff = (target_day - start_week_day) % 7
        return date(year, month, start_meetup_day + diff)

    except:
        raise MeetupDayException("That day does not exist.")
        