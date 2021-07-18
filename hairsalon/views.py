from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import News, MENU_CATEGORY
from accounts.models import SalonStaff


# Create your views here.

class ContentView(TemplateView):
    template_name = 'hairsalon/content.html'


class TopView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ごあいさつ
        owner = SalonStaff.objects.get(is_owner=True)
        # お知らせ
        news = News.objects.order_by('-published')

        context['owner'] = owner
        context['news'] = news
        context['page_title'] = 'トップページ'
        context['current_menu_item'] = 'top'
        return context


class GreetingView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = SalonStaff.objects.get(is_owner=True)
        context['owner'] = owner
        context['page_title'] = 'ごあいさつ'
        context['current_menu_item'] = 'greeting'
        return context


class MenuView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MENU_CATEGORY
        context['page_title'] = '施術メニュー'
        context['current_menu_item'] = 'menu'
        return context


class StylistView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stylists = SalonStaff.objects.all()
        context['stylists'] = stylists
        context['page_title'] = 'スタイリスト'
        context['current_menu_item'] = 'stylist'
        return context


class NewsView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.order_by('-published')
        context['news'] = news
        context['page_title'] = 'お知らせ'
        context['current_menu_item'] = 'news'
        return context


class NewsDetailView(DetailView):
    template = 'hairsalon/news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_menu_item'] = 'news'
        return context


class MapView(ContentView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'アクセス'
        context['current_menu_item'] = 'map'
        return context
