from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('all',views.all,name='all'),

    path('product/<slug:product_slug>',views.product_info,name='product-info'),

    path('category/<slug:category_slug>',views.list_category,name='list-category'),

    path ('reccomendations',views.reccommend, name = 'reccomendations')
        

]

