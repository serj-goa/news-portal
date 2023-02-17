from django.contrib import admin

from news.models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title', )
    search_fields = ('title', )


admin.site.register(Category, CategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'updated_at',
        'is_published',
    )
    list_display_links = ('id', 'title', 'category', )
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category', )
    search_fields = ('title', 'content', 'category', )


admin.site.register(News, NewsAdmin)
