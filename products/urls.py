from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('turntables/', views.all_turntables, name='turntables'),
    path('<int:turntable_id>/', views.turntable_detail,
         name='turntable_detail'),
    path('add_turntable/', views.add_turntable, name='add_turntable'),
    path('edit_turntable/<int:turntable_id>/', views.edit_turntable,
         name='edit_turntable'),
    path('delete_turntable/<int:turntable_id>/', views.delete_turntable,
         name='delete_turntable'),
    path('headphones/', views.all_headphones, name='headphones'),
    path('<int:headphones_id>/', views.headphones_detail,
         name='headphones_detail'),
    path('add_headphones/', views.add_headphones, name='add_headphones'),
    path('edit_headphones/<int:headphones_id>/', views.edit_headphones,
         name='edit_headphones'),
    path('delete_headphones/<int:headphones_id>/', views.delete_headphones,
         name='delete_headphones'),
]
