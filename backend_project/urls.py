from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  
    path('api/tradedetails/', include('tradedetails.urls')),  
    path('api/tradereasons/', include('tradereasons.urls')),  
    path('api/candleimages/', include('candleimages.urls')),  
    path('api/tradingindicators/', include('tradingindicators.urls')),  
    path('api/task/', include('task.urls')),  
    path('api/puzzles/', include('puzzles.urls')),  
    path('api/toys/', include('toys.urls')),  
    path('api/games/', include('games.urls')),  
    path('api/risktrades/', include('risktrades.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
