from django.contrib import admin
from .models import Listing
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25


admin.site.register(Listing, ListingAdmin)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

