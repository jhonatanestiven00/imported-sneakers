from django.contrib import admin
from .models import CategoryDB, PostDB
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created", "update")

class PostAdmin(admin.ModelAdmin):
    readonly_fields=("created", "update")
    list_display=("title", "author","published","post_categories")
    ordering=('author',)
    search_fields=('title',)
    date_hierarchy='published'
    list_filter=('author__username','categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name  for c in obj.categories.all().order_by("name")])
    post_categories.short_description="Categorias"


admin.site.register(CategoryDB, CategoryAdmin)
admin.site.register(PostDB, PostAdmin)