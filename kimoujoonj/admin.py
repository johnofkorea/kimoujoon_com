from django.contrib import admin
from .models import Media, Tdate, Person, PersonRelationship
					


class MediaAdmin(admin.ModelAdmin):
    search_fields = ('title', )
admin.site.register(Media, MediaAdmin)



class TdateAdmin(admin.ModelAdmin):
    search_fields = ('date', )
admin.site.register(Tdate, TdateAdmin)



class PersonRelationshipInline(admin.TabularInline):
    model = PersonRelationship
    fk_name = 'from_person'



class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonRelationshipInline, )
    search_fields = ('username', 'name', )
admin.site.register(Person, PersonAdmin)
