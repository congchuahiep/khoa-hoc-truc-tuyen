from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    '''Custom lession view'''
    # Field display
    list_display = ['id', 'subject', 'activate', 'created_date']
    # Add search box
    search_fields = ['subject']
    # Add field filter
    list_filter = ['activate']
    # Alow editable field
    list_editable = ['subject']
    # Set image_view field to readonly for display image
    # (field image_view is define below)
    readonly_fields = ['image_view']

    def image_view(self, lesson):
        if lesson:
            return mark_safe(f"<img src='/{lesson.image.name}' width='400'/>")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }



# Register models for admin page
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)