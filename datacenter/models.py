from django.db import models
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self, visited, leaved=django.utils.timezone.localtime()):
        if leaved is None:
            leaved = django.utils.timezone.localtime()
        duration = leaved - visited
        return duration

    def format_duration(self, duration):
        duration_in_sec = duration.total_seconds()
        return f'{ int(duration_in_sec // 3600) }ч. { int((duration_in_sec % 3600) // 60) }мин.'

    def is_visit_long(self, visit, minutes=60):
        return visit.total_seconds() > minutes * 60
