from django.shortcuts import render

from .models import News

# Create your views here.

def top(request):
    news = News.objects.order_by('-published')
    return render(request, 'hairsalon/top.html', {'news': news, 'current_menu_item': 'top'})