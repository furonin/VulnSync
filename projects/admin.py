from django.contrib import admin
from .models import Project, Vulnerability

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'created_at', 'owner')
    search_fields = ('name', 'client_name')

@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'project', 'ip_address')
    list_filter = ('severity', 'project')
    search_fields = ('title', 'cve_id', 'ip_address')