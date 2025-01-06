from .models import LinkDB

def ctx_dict(request):
    ctx={}
    links = LinkDB.objects.all()
    for link in links:
        ctx[link.key]= link.url
    return ctx