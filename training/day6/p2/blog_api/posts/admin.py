from django.contrib import admin
from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'bio')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')

    #list_display_links = ('title','author')
    #list_editable = ('status',)
    #date_hierarchy = 'created_at'
    #fields = ('title', 'content', 'author', 'status')
    #exclude = ('slug',)
    readonly_fields = ('created_at', 'updated_at')
    # fieldsets = (
    #     (None, {'fields': ('title', 'content')}),
    #     ('Author and Status', {'fields': ('author', 'status')}),
    # )
    
    actions = ['mark_as_draft']
    def mark_as_draft(self, request, queryset):
        queryset.update(status='draft')
        self.message_user(request, "Selected posts were marked as draft.")

