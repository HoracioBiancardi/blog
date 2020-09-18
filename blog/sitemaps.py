from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from posts.models import Post
from posts.models import Categoria


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return ["index"]

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"
    

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return reverse("post_detalhes", args=[item.id])

    def lastmod(self, obj):
        return obj.data_post 
    
class CatSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Categoria.objects.all()

    def location(self, item):
        return reverse("post_categoria", args=[item.nome_cat])
