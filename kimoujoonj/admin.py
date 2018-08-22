from django.contrib import admin
from .models import Media, Tdate
					


class MediaAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Media, MediaAdmin)



class TdateAdmin(admin.ModelAdmin):
    search_fields = ('date', )
admin.site.register(Tdate, TdateAdmin)
