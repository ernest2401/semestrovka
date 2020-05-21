from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
#from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

#schema_view = get_swagger_view(title='EMS API Documentaion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/',include('bboard.urls')),
    path('accounts/',include('accounts.urls')),
    path('registration/',include('registration.urls')),
    #path('api_documentation/',schema_view)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
