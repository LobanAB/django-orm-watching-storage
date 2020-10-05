from datacenter import models
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in passcard_visits:
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": models.format_duration(models.get_duration(visit.entered_at, visit.leaved_at)),
                "is_strange": models.is_visit_long(models.get_duration(visit.entered_at, visit.leaved_at)),
            }
        )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
