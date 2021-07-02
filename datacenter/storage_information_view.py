from datacenter import models
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in visitors:
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': visitor.entered_at,
                'duration': visitor.format_duration(visitor.get_duration()),
                'is_strange': visitor.is_visit_long(visitor.get_duration()),
            }
         )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
