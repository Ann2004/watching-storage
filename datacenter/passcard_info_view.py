from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .visit_duration import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []
    for visit in visits_by_passcard: 
        duration = format_duration(get_duration(visit))
            
        flag = is_visit_long(visit)
        
        passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': flag
        }
        this_passcard_visits.append(passcard_visit)

        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
