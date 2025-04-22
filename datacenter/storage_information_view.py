from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.get_time_spent_in_storage import get_time_spent_in_storage


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for unclosed_visit in unclosed_visits:
        entered_at_time = unclosed_visit.entered_at
        
        now_time = timezone.localtime(timezone.now())
        duration = get_time_spent_in_storage(entered_at_time, now_time)
        
        # delta = now_time - entered_at_time
        # total_seconds = int(delta.total_seconds())
        # delta = timedelta(seconds=total_seconds)
        
        non_closed_visit = {
            'who_entered': unclosed_visit.passcard.owner_name,
            'entered_at': entered_at_time,
            'duration': duration,
        }
        non_closed_visits.append(non_closed_visit)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
