
from django.urls import path,include
from .views import test,getdata,home_page




urlpatterns = [
    path('test/',test),
    path('person/',getdata),
    path('',home_page)

]
