from django.contrib import admin
from .models import TmonthJp, ThoughtJp, PressJp, NewsJp



class TmonthJpAdmin(admin.ModelAdmin):
    search_fields = ('year', 'month', )
admin.site.register(TmonthJp, TmonthJpAdmin)



class ThoughtJpAdmin(admin.ModelAdmin):
    search_fields = ('content', )
admin.site.register(ThoughtJp, ThoughtJpAdmin)



class PressJpAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(PressJp, PressJpAdmin)



class NewsJpAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(NewsJp, NewsJpAdmin)
