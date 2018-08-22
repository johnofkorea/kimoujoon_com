from django.contrib import admin
from .models import TmonthKr, ThoughtKr, PressKr, NewsKr



class TmonthKrAdmin(admin.ModelAdmin):
    search_fields = ('year', 'month', )
admin.site.register(TmonthKr, TmonthKrAdmin)



class ThoughtKrAdmin(admin.ModelAdmin):
    search_fields = ('content', )
admin.site.register(ThoughtKr, ThoughtKrAdmin)



class PressKrAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(PressKr, PressKrAdmin)



class NewsKrAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(NewsKr, NewsKrAdmin)
