from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title_post', 'slug', 'status', 'created')
    search_fileds = ['title', 'content']
    prepopulated_fields = {'slug': ('title_post',)}
    list_filter = ('status', ('created'))
    summernote_fileds = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'body_content', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
