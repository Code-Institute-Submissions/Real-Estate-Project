from django.contrib import admin
from .models import Listing, Comment


class ListingAdmin(admin.ModelAdmin):
  
  list_display = ('id', 'title', 'slug', 'status', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor', 'likes')
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25


admin.site.register(Listing, ListingAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'listing', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(Comment)