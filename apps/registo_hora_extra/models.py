from django.db import models


class RegistoHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motivo')

    def __str__(self):
        return self.motivo
