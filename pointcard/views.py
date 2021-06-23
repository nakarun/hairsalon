from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import PointCard, Stamp


# Create your views here.


class PointCardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pointcard = PointCard.objects.get()
        stamps = Stamp.unused_objects.filter(customer=request.user)

        stamp_frames = [[0] * pointcard.horizontal_cells_count for i in range(pointcard.vertical_cells_count)]

        for i, stamp in enumerate(stamps):
            v = i // pointcard.horizontal_cells_count
            h = i - v * pointcard.horizontal_cells_count
            stamp_frames[v][h] = stamp

        context = {
            'stamp_frames': stamp_frames,
        }

        return render(request, 'pointcard/pointcard.html', context)