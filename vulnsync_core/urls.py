from django.contrib import admin
from django.urls import path
from projects.views import upload_scan, download_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_scan, name='upload_scan'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_scan, name='upload_scan'),
    path('download/<int:project_id>/', download_report, name='download_report'), 
]