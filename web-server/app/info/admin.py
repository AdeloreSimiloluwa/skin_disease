from django.contrib import admin
from .models import Info
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class SummerInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('causes', 'things_to_avoid',)
    list_display = ('id', 'disease', 'created_at', 'updated_at')
    ordering = ('id',)
    search_fields = ('disease',)

admin.site.register(Info, SummerInfoAdmin)