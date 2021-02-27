from django.contrib import admin
from .models import *

class ReligionAdmin(admin.ModelAdmin):
    fields = ['religion_name']

class CasteAdmin(admin.ModelAdmin):
    fields = ['religion,caste_name']

class StateAdmin(admin.ModelAdmin):
    fields = ['state_name']

class MothertongueAdmin(admin.ModelAdmin):
    fields = ['mothertongue_name']

class RelationAdmin(admin.ModelAdmin):
    fields = ['relation_name']


admin.site.register(Religion, ReligionAdmin)
admin.site.register(Caste, CasteAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Mothertongue, MothertongueAdmin)
admin.site.register(Relation, RelationAdmin)