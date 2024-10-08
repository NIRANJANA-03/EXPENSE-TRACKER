from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 


urlpatterns = [
    
    path('', RedirectView.as_view(url='signup/', permanent=False)),
    path('', include('expenses.urls')),
    
    path('admin/', admin.site.urls),
    
]
