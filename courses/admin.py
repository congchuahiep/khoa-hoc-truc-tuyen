from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse

from courses.models import Category, Course, Lesson, Tag, Comment, User
from courses.utils import get_cloudinary_image
from django.urls import path

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.utils.safestring import mark_safe


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = "__all__"


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "description"]
    list_editable = ["subject"]
    readonly_fields = ["image_view"]

    def image_view(self, course):
        if course:
            return get_cloudinary_image(
                course.image.public_id, transformations={"width": 200}
            )


class MyLessonAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "active", "created_date"]
    search_fields = ["subject"]
    list_filter = ["id", "created_date"]
    list_editable = ["subject"]
    readonly_fields = ["image_view"]
    form = LessonForm

    def image_view(self, lesson):
        if lesson:
            return get_cloudinary_image(
                lesson.image.public_id, transformations={"width": 200}
            )

    class Media:
        css = {"all": ("/static/css/styles.css",)}


class MyUserAdmin(admin.ModelAdmin):
    list_display = ["status_display", "username", "email"]
    search_fields = ["username", "email"]
    list_filter = ["is_active", "date_joined"]
    sortable_by = ["username"]

    fieldsets = [
        ("Thông tin cá nhân", {"fields": ["status_display", "username", "email", "avatar_view"]}),
        (
            "Quyền truy cập",
            {
                "description": "Thiết lập quyền truy cập của người dùng",
                "classes": ["collapse"],
                "fields": ["user_permissions", "is_staff", "is_superuser"],
            },
        ),
    ]

    # list_editable = ['is_staff']
    readonly_fields = ["avatar_view", "status_display"]
    filter_horizontal = ["user_permissions"]

    def avatar_view(self, user):
        if user:
            return get_cloudinary_image(
                user.avatar.public_id, transformations={"width": 200}
            )

    def status_display(self, user):
        """Hiển thị trạng thái dưới dạng biểu tượng màu."""
        color = "green" if user.is_active else "red"
        return mark_safe(f'<span style="color: {color};">●</span>')

    status_display.short_description = "Trạng thái"


class MyAdminSite(admin.AdminSite):
    site_header = "OU eCourse Online"

    def get_urls(self):
        return [
            path("course-stats/", self.course_stats),
        ] + super().get_urls()

    def course_stats(self, request):
        stats = Category.objects.annotate(course_count=Count("course__id")).values(
            "id", "name", "course_count"
        )

        return TemplateResponse(request, "admin/stats.html", {"stats": stats})


admin_site = MyAdminSite(name="eCourse")

admin_site.register(Category)
admin_site.register(Course, MyCourseAdmin)
admin_site.register(Lesson, MyLessonAdmin)
admin_site.register(Tag)
admin_site.register(Comment)
admin_site.register(User, MyUserAdmin)
