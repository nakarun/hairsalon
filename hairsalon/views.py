from django.shortcuts import render, get_object_or_404

from .models import News

# Create your views here.

def top(request):
    news = News.objects.order_by('-published')
    return render(request, 'hairsalon/top.html', {'news': news, 'current_menu_item': 'top'})

def news_detail(request, news_id):
    news_detail = get_object_or_404(News, pk=news_id)
    return render(request, 'hairsalon/news_detail.html', {'news_detail': news_detail, 'current_menu_item': 'news'})