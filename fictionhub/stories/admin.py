from django.contrib import admin

from .models import Hub, Story, Chapter, Comment

class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Hub)
admin.site.register(Story)
admin.site.register(Comment)

