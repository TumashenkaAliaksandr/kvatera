from django.contrib import admin
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget
from django import forms


class BlogPostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'top', 'price')
    list_filter = ('top', 'author')
    search_fields = ('title', 'author', 'name_object')


admin.site.register(BlogPost, BlogPostAdmin)
