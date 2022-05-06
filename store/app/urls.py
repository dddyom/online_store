from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('category/<slug:cat_slug>', Categories.as_view(), name='category'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),

]
