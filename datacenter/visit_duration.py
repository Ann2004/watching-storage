from django.utils import timezone


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
MINUTES_IN_HOUR = 60


def get_duration(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        now_time = timezone.localtime(timezone.now())
        delta = now_time - visit.entered_at
    return delta


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // MINUTES_IN_HOUR
    if hours:
        formatted_time = f'{hours} ч {minutes} мин'
    else:
        formatted_time = f'{minutes} мин'
    return formatted_time


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * SECONDS_IN_MINUTE