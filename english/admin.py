from django.contrib import admin
from .models import ThoughtEn, PressEn, NewsEn



class ThoughtEnAdmin(admin.ModelAdmin):
    search_fields = ('content', )
admin.site.register(ThoughtEn, ThoughtEnAdmin)



class PressEnAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(PressEn, PressEnAdmin)



class NewsEnAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(NewsEn, NewsEnAdmin)
