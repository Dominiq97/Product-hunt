from django.urls import path,include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
	path('search', views.search, name='search'),
    path('detail', views.detail, name='detail'),
    path('products_by/<str:tag>', views.ListProductsByTag.as_view(),name='list_by_tag'),
    path('products/<int:category_id>',views.category, name='category'),
    
]