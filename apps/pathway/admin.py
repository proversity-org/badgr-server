# Created by wiggins@concentricsky.com on 5/11/16.
import basic_models
from django.contrib.admin import ModelAdmin, TabularInline
from mainsite.admin import badgr_admin
from pathway.models import Pathway, PathwayElement, PathwayElementBadge


class PathwayAdmin(ModelAdmin):
    list_display = ('name', 'issuer', 'jsonld_id')
    pass

badgr_admin.register(Pathway, PathwayAdmin)



class PathwayElementBadgeInline(TabularInline):
    model = PathwayElementBadge
    extra = 0
    fields = ('element','badgeclass','ordering')
    raw_id_fields = ('badgeclass','element')

class PathwayElementAdmin(basic_models.DefaultModelAdmin):
    list_display = ('name','slug', 'pathway_name', 'issuer','is_active','created_at')
    list_filter = ('is_active','created_at')
    search_fields = ('name','slug','description',)
    readonly_fields = ('created_by','created_at','updated_by','updated_by',)
    raw_id_fields = ('completion_badgeclass','pathway','parent_element')
    fieldsets = (
        ('Metadata', {
            'fields': ('is_active','created_by','created_at','updated_by','updated_by',),
            'classes': ('collapse',)
        }),
        (None, {
            'fields': ('name', 'description', 'alignment_url')
        }),
        ('Structure', {
            'fields': ('pathway','parent_element','ordering')
        }),
        ('Completion', {
            'fields': ('completion_badgeclass', 'completion_requirements')
        })
    )
    inlines = [PathwayElementBadgeInline]

    def pathway_name(self, obj):
        return obj.pathway.name
    pathway_name.short_description = 'pathway'

    def issuer(self, obj):
        return obj.pathway.issuer
badgr_admin.register(PathwayElement, PathwayElementAdmin)

