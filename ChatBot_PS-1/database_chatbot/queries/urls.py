# botinfoapi/urls.py
"""  This module is pure Python code and is a mapping between URL path expressions to Python functions.
For more information visit https://docs.djangoproject.com/en/3.0/topics/http/urls/
    
    """

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'chatbot', views.message_list, 'chatbot')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/messages/', views.message_list, name='message-list')
]
