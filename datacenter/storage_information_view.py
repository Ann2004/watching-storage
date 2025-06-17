from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .visit_duration import get_duration, format_duration


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for unclosed_visit in unclosed_visits:
        duration = format_duration(get_duration(unclosed_visit))
        
        non_closed_visit = {
            'who_entered': unclosed_visit.passcard.owner_name,
            'entered_at': unclosed_visit.entered_at,
            'duration': duration,
        }
        non_closed_visits.append(non_closed_visit)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
