from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('scrape-page/', views.scrape_web_page, name='scrape_web_page'),
    path('scraped-text/<str:url>/', views.scrape_web_page, name='scraped_text'),

]
