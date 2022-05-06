from django.contrib import admin
from django.urls import path, include
from matchat import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('matchat/', include('matchat.urls')),
    path('api_same_check/', include('api_same_check.urls')),
    path('api_paycheck/', include('api_paycheck.urls')),
    path('', views.main, name='main'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)