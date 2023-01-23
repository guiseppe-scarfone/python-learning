MINUTES_IN_DAY = 24 * 60


def add_time(start: str, duration: str, day_of_week: str = None):
  """Add duration to the time and return the result."""
  start_time_in_minutes = time_to_minutes(start)
  dur_in_minutes = time_to_minutes(duration)
  days = calc_days(start_time_in_minutes, dur_in_minutes)

  new_time = minutes_to_time(start_time_in_minutes + dur_in_minutes, days,
                             day_of_week)

  return new_time


def calc_days(start_time_in_minutes: int, dur_in_minutes: int) -> int:
  """Calculate the number of days from the start time to the end of the duration."""
  return int((start_time_in_minutes + dur_in_minutes) / MINUTES_IN_DAY)


def time_to_minutes(time: str) -> int:
  """Convert from time to the number of minute elapsed for the day."""
  am_or_pm = ''
  if 'M' in time:
    am_or_pm = time[-3:].strip()
    time = time[:-3]
  time_list = time.split(':')
  hours = int(time_list[0]) + (12 if am_or_pm.upper() == 'PM' else 0)
  minutes = int(time_list[1])
  return (hours * 60) + minutes


def minutes_to_time(minutes: int, days: int, day_of_week: str = None) -> str:
  """Convert minutes in the day to the time."""
  am_or_pm = 'AM'
  days_text = ''
  weekday = ''
  current_day_minutes = minutes % MINUTES_IN_DAY
  hours = int(current_day_minutes / 60)
  minutes = current_day_minutes - (hours * 60)

  if hours == 12:
    am_or_pm = 'PM'
  elif hours > 12:
    hours -= 12
    am_or_pm = 'PM'
  elif hours == 0:
    hours = 12

  if days == 1:
    days_text = ' (next day)'
  elif days > 1:
    days_text = f' ({days} days later)'

  if day_of_week:
    weekday = day_of_week_to_desc(day_of_week, days)

  return f'{hours}:{minutes:02d} {am_or_pm}{weekday}{days_text}'


def day_of_week_to_desc(day_provided: str, days: int) -> str:
  """Convert day of the week plus elapsed days to a day of week desc."""
  days_of_week = ('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY',
                  'FRIDAY', 'SATURDAY')
  current_day_of_week = days_of_week.index(day_provided.upper())
  new_day_of_week = (current_day_of_week + days) % 7
  return f', {days_of_week[new_day_of_week].capitalize()}'
