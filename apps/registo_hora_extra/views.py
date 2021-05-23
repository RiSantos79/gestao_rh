from django.shortcuts import render
from django.views.generic import ListView

from .models import RegistoHoraExtra


class HoraExtraList(ListView):
    model = RegistoHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistoHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
