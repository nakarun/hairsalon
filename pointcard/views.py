from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import PointCard

# Create your views here.


class PointCardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pointcard = PointCard.objects.get()
        context = {
            'vertical_cells': range(pointcard.vertical_cells_count),
            'horizontal_cells': range(pointcard.horizontal_cells_count),
        }
        return render(request, 'pointcard/pointcard.html', context)