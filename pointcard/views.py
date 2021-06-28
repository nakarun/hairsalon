from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from typing import Union, List

from .models import PointCard, Stamp


# Create your views here.

def get_stamp_frames(pointcard: PointCard, stamps: Union[QuerySet, List[Stamp]]) -> List:
    stamp_frames = [[0] * pointcard.horizontal_cells_count for i in range(pointcard.vertical_cells_count)]

    for i, stamp in enumerate(stamps):
        v = i // pointcard.horizontal_cells_count
        h = i - v * pointcard.horizontal_cells_count
        if v + 1 > len(stamp_frames):
            break
        stamp_frames[v][h] = stamp

    return stamp_frames


class PointCardView(LoginRequiredMixin, TemplateView):
    template_name = 'pointcard/pointcard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: salonでフィルターする
        pointcard = PointCard.objects.first()
        stamps = Stamp.unused_objects.filter(customer=self.request.user)

        context['stamp_frames'] = get_stamp_frames(pointcard, stamps)
        return context
