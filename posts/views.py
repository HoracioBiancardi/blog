from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from .models import Post
from django.db.models import Count, When, Case, Q
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages
from categorias.models import Categoria


class PostIndex(ListView):
    model = Post
    template_name = "posts/index.html"
    paginate_by = 6
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("categoria_post")
        qs = qs.order_by("-id").filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(When(comentario__publicado_comentario=True, then=1))
            )
        )

        return qs


class PostBusca(PostIndex):
    template_name = "posts/post_busca.html"

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET["termo"]

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo)
            | Q(excerto_post__icontains=termo)
            | Q(autor_post__username__iexact=termo)
            | Q(conteudo_post__icontains=termo)
            | Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs


class PostCategoria(PostIndex):
    template_name = "posts/post_categoria.html"


    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get("categoria", None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)
        return qs


class PostDetalhes(UpdateView):
    template_name = "posts/post_detalhes.html"
    model = Post
    form_class = FormComentario
    context_object_name = "post"

  
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(
            publicado_comentario=True, post_comentario=post.id
        )

        contexto["comentarios"] = comentarios
        contexto["categorias"] = Categoria.objects.all()
        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, "Comentário enviado com sucesso.")
        return redirect("post_detalhes", pk=post.id)

