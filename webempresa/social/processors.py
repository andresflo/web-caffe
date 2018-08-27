from .models import Link


def ctx_dict(request):#Estamos ampliando el contexto para que quede global y accesible en todas las vistas
    ctx={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx