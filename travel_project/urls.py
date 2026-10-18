from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('tour/', include('tour.urls')),
    path('blog/', include('blog.urls')),
    path('marketing/', include('marketing.urls')),
]

# Customizing Admin Panel Texts - 2026 SaaS-Grade Command Center
admin.site.site_header = "Bobby Tour & Travels | Command Center"
admin.site.site_title = "Bobby Admin Portal"
admin.site.index_title = "Welcome to Bobby Tour & Travels Management Dashboard"