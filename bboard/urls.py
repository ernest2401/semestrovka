from django.contrib import admin
from django.urls import path,include,re_path
from .views import index,ad_share,ad_detail,by_rubric,ad_create,wish,create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name='index'),
    path('<int:pk>/share/', ad_share, name='ad_share'),
    path('<int:pk>/', ad_detail, name='ad_detail'),
    path('rubric/<int:rubric_id>/',by_rubric,name='by_rubric'),
    path('add/',ad_create,name='add'),
    re_path(r'wish',wish,name='wish'),
    path('wish/create/',create,name='create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
