from datacenter import models
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in visitors:
        non_closed_visits.append(
            {
                "who_entered": visitor.passcard,
                "entered_at": visitor.entered_at,
                "duration": models.format_duration(models.get_duration(visitor.entered_at)),
                "is_strange": models.is_visit_long(models.get_duration(visitor.entered_at)),
            }
         )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
