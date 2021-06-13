from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import News

# Create your views here.

class TopView(View):
    def get(self, request, *args, **kwargs):
        news = News.objects.order_by('-published')
        context = {
            'news': news,
            'current_menu_item': 'top',
        }
        return render(request, 'hairsalon/top.html', context)

top = TopView.as_view()

class NewsDetailView(View):
    def get(self, request, news_id, *args, **kwargs):
        news_detail = get_object_or_404(News, pk=news_id)
        context = {
            'news_detail': news_detail,
            'current_menu_item': 'news',
        }
        return render(request, 'hairsalon/news_detail.html', context)

news_detail = NewsDetailView.as_view()