from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, SignUpForm


# Create your views here.

class CustomerSignUp(CreateView):
    object: object
    form_class = SignUpForm
    template_name = "pointcard/signup.html"
    success_url = reverse_lazy('customer_pointcard')

    def form_valid(self, form):
        """ログインも一緒にしてしまうためにオーバーライド"""
        user = form.save()  # formの情報を保存
        login(self.request, user)  # 認証
        self.object = user
        return HttpResponseRedirect(self.get_success_url())  # リダイレクト


class CustomerLogout(LogoutView):
    template_name = 'pointcard/logout.html'


class CustomerLogin(LoginView):
    form_class = LoginForm
    template_name = 'pointcard/login.html'


class CustomerPointCard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'stamp_frames': [0, 1, 2, 3, 4, 5],
        }
        return render(request, 'pointcard/pointcard.html', context)