from datetime import timedelta


def get_time_spent_in_storage(entered_at_time, end_time):
    delta = end_time - entered_at_time
    total_seconds = int(delta.total_seconds())
    delta = timedelta(seconds=total_seconds)
    return delta