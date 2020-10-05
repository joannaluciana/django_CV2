from django.contrib import admin

from work.models import Project, Category





class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'web_site', 'date_of_create',
    'categories', 'portfolio')
    list_filter = ('name', )
    date_hierarchy = 'date_of_create'
    search_fields = ('name', 'web_site')


    def description_short(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
