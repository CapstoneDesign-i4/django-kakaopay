from django.contrib import admin
from django.urls import path, include
from matchat import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('matchat/', include('matchat.urls')),
    path('', views.main, name='main'),
    path('api_same_check/', include('api_same_check.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)