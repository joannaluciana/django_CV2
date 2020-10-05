from django.contrib import admin


from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['title', 'description', 'project__title',]
    list_display = ['title', 'project', 'user', 'state', 'pub_date']
    list_filter = ['state', 'project']


admin.site.register(Reviews, ReviewsAdmin)