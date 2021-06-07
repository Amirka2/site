from django.urls import path
from django.views.generic import TemplateView
from lotteryapp.views import SignUpView, LoginUser

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="lotteryapp/index.html"), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(redirect_authenticated_user=True), name='login'),
    path('lk/', TemplateView.as_view(template_name="lotteryapp/LK.html"), name='lk'),
]
