from django.contrib import admin
from .models import Media, Tmonth, Tdate
					



class MediaAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Media, MediaAdmin)



class TmonthAdmin(admin.ModelAdmin):
    search_fields = ('year', 'month', )
admin.site.register(Tmonth, TmonthAdmin)



class TdateAdmin(admin.ModelAdmin):
    search_fields = ('date', )
admin.site.register(Tdate, TdateAdmin)
