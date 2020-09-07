from django import template
from random import randint

register = template.Library()


@register.filter(name="plural_comentarios")
def plural_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            return f"Nenhum comentário"
        elif num_comentarios == 1:
            return f"{num_comentarios} Comentário"
        else:
            return f"{num_comentarios} Comentários"

    except:
        return f"{num_comentarios} Comentário(s)"

@register.filter(name="aos")
def aos(t,s=1):
    return randint(s,t)