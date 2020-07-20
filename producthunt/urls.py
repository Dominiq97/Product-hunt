
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('products_by/<str:tag>', views.ListProductsByTag.as_view(),name='list_by_tag'),
    path('products/category.html', views.category, name='category'),
    url(r'^filer/', include('filer.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

