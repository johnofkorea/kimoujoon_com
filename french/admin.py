from django.contrib import admin
from .models import ThoughtFr, PressFr, NewsFr



class ThoughtFrAdmin(admin.ModelAdmin):
    search_fields = ('content', )
admin.site.register(ThoughtFr, ThoughtFrAdmin)



class PressFrAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(PressFr, PressFrAdmin)



class NewsFrAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(NewsFr, NewsFrAdmin)
