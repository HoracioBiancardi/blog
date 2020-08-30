from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    path("", views.PostIndex.as_view(), name="index"),
    path("post/<int:pk>", views.PostDetalhes.as_view(), name="post_detalhes"),
    path("busca/", views.PostBusca.as_view(), name="post_busca"),
    path(
        "categoria/<str:categoria>",
        views.PostCategoria.as_view(),
        name="post_categoria",
    ),
    path("sitemap.xml", sitemap, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]
