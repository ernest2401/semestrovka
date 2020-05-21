from django.contrib import admin
from django.contrib.auth.models import User
from .models import Ad,Rubric,Comment,Wish

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',)
    list_filter = ('publish', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'created', 'active',)
    list_filter = ('active', 'created', 'updated',)
    search_fields = ('body',)

admin.site.register(Rubric)
@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('author', 'body','number',)
    list_filter = ('author',)
    search_fields = ('body', 'number',)
