from django.contrib import admin

from work.models import Project, Category


# class ProjectInline(admin.StackedInline):
#     model = Project
#     extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'web_site', 'date_of_create',
    'categories', 'portfolio')
    list_filter = ('name', 'description', 'web_site')
    date_hierarchy = 'date_of_create'
    search_fields = ('first_name', 'last_name', 'web_site')
    # inlines = [ProjectInline]



    def short_description(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )

    # krotki_opis.short_description = 'Description'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
