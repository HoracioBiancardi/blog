"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from blog.sitemaps import StaticSitemap, PostSitemap, CatSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "pages": StaticSitemap,
    "posts": PostSitemap,
    "categoria": CatSitemap,
}


urlpatterns = [
    path("", include("posts.urls")),
    path("admin/", admin.site.urls),
    # path("summernote/", include("django_summernote.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("sitemap.xml", sitemap, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", include('robots.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Blog Swordpower Admin"
admin.site.site_title = "Blog Swordpower Admin"
# admin.site.site_url = "http://coffeehouse.com/"
admin.site.index_title = "Blog Swordpower Administração"
admin.empty_value_display = "**Vazio**"

