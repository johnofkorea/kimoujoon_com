from django.contrib import admin
from .models import Media, Thought



class MediaAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Media, MediaAdmin)



class ThoughtAdmin(admin.ModelAdmin):
    search_fields = ('content_kr', )
admin.site.register(Thought, ThoughtAdmin)
