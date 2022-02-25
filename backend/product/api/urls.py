
from django.urls import path,include
from .views import test,getdata




urlpatterns = [
    path('test/',test),
    path('person/',getdata)

    
]
