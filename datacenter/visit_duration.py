from django.utils import timezone


def get_duration(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        now_time = timezone.localtime(timezone.now())
        delta = now_time - visit.entered_at
    return delta


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    if hours:
        formatted_time = f'{hours} ч {minutes} мин'
    else:
        formatted_time = f'{minutes} мин'
    return formatted_time


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60