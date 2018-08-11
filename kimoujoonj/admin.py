from django.contrib import admin
from .models import Media, OldThought, Tdate
					



class MediaAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Media, MediaAdmin)



class OldThoughtAdmin(admin.ModelAdmin):
    search_fields = ('content_kr', )
admin.site.register(OldThought, OldThoughtAdmin)



class TdateAdmin(admin.ModelAdmin):
    search_fields = ('date', )
admin.site.register(Tdate, TdateAdmin)
