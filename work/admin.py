from django.contrib import admin
from .models import Stage, TempThought, TempThoughtRelationship



class StageAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Stage, StageAdmin)


class TempThoughtRelationshipInline(admin.TabularInline):
    model = TempThoughtRelationship
    fk_name = 'from_tt'


class TempThoughtAdmin(admin.ModelAdmin):
    inlines = (TempThoughtRelationshipInline, )
    search_fields = ('content_kr', )
admin.site.register(TempThought, TempThoughtAdmin)
