from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('place_order/', views.place_order, name='place_order'),
]


urlpatterns = [
    # your other url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
