from django.contrib import admin
from .models import Bewerbung

@admin.register(Bewerbung)
class BewerbungAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "position", "date_applied", "status")
    list_filter = ("status", "date_applied")
    search_fields = ("name", "company", "position")
