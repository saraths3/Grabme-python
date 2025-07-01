from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # URL for the serpstack API scraping view
    path('get_page_description/', views.get_page_description, name='get_page_description'),

    # URL for displaying search results
    path('get_serpstack_search_results/', views.get_serpstack_search_results, name='get_serpstack_search_results'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('chatbot_form/', views.chatbot_form, name='chatbot_form'),
   
]
