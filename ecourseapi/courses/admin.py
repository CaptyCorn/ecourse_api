from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from courses.models import Category, Course, Lesson

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'description', 'created_date']
    list_filter = ['id', 'subject']
    search_fields = ['subject']
    readonly_fields = ['image_view']

    def image_view(self, courses):
        if courses.image:
            return mark_safe(f'<img src=/static/{courses.image.name} width=200>')

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm

class MyAdmin(admin.AdminSite):
    site_header = 'Quản lý khóa học'

    def get_urls(self):
        return [path('stats-view/', self.stat_view)] + super().get_urls()

    def stat_view(self, request):
        stats = Category.objects.annotate(count = Count('course')).values('id', 'name', 'count')

        return TemplateResponse(request, 'admin/stats.html', {'stats':stats})

admin_site = MyAdmin()

admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
