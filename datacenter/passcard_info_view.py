from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datacenter.get_time_spent_in_storage import get_time_spent_in_storage


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []
    for visit in visits_by_passcard: 
        entered_at_time = visit.entered_at
        if visit.leaved_at:
            duration = get_time_spent_in_storage(entered_at_time, visit.leaved_at)
        else: 
            now_time = timezone.localtime(timezone.now())
            duration = duration = get_time_spent_in_storage(entered_at_time, now_time)
        
        is_strange = False   
        if duration.seconds > 3600:
            is_strange = True
        
        passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
        }
        this_passcard_visits.append(passcard_visit)

        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
