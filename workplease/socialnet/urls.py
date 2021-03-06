from django.urls import path
from .views import *


urlpatterns = [
    path('mypage/', user_page, name='user_page'),
    path('editmypage/', edit_user_page, name='edit_user_page'),
    path('friends/', friends, name='friends'),
    path('settings/', settings, name='settings'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path('test-items/', test_items, name='test_items')
]
