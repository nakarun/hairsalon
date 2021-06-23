from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.


class CustomerPointCard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'stamp_frames': [0, 1, 2, 3, 4, 5],
        }
        return render(request, 'pointcard/pointcard.html', context)