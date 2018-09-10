from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieDataModelAdmin(admin.ModelAdmin):
    list_display = ["title", "rating", "released_year"]
    list_display_links = ["title"]
    list_filter = ["rating", "released_year"]
    search_fields = ["title"]
    
    class Meta:
        model = Movie

admin.site.register(Movie, MovieDataModelAdmin)