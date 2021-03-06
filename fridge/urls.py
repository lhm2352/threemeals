from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


from fridge.views import *
#
urlpatterns=[
    url(r'^$', FridgeHomeView.as_view(), name='recommendation'),
    url(r'^ingredient/$', IngredientHomeView.as_view(), name='ingredient'),
    url(r'^scrap/$', ScrapHomeView.as_view(), name="scrap"),

    url(r'^menu_detail/$', MenuDetailView.as_view(), name='menu_detail'),

    url(r'^shopping/$', ShoppingHomeView.as_view(), name="shopping"),
    url(r'^(?P<pk>[0-9]+)/delete/$', ItemDeleteView.as_view(), name="delete"),
]