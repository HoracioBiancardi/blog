from django.contrib import admin
from .models import Post
# from django_summernote.admin import SummernoteModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    conteudo_post = forms.CharField(widget=CKEditorUploadingWidget(),label="Conteudo")

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo_post",
        "autor_post",
        "data_post",
        "excerto_post",
        "categoria_post",
        "publicado_post",
    )
    list_display_links = (
        "id",
        "titulo_post",
        "autor_post",
    )
    list_editable = ("publicado_post",)
    #summernote_fields = ("conteudo_post",)
    form = PostAdminForm
