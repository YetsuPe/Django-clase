# Create your views here.
from principal.models import Post , Comentario
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response , get_object_or_404

def posts(request):
	todos_posts=Post.objects.all()
	usuarios=User.objects.all()
	comentarios=Comentario.objects.all()
	return render_to_response('posts.html',{'posts':todos_posts,'usuarios':usuarios,'comentarios':comentarios},context_instance=RequestContext(request) )
def yetsu(request):
	return render_to_response('plantillaYetsu.html')
def simple(request):
	return HttpResponse("<html><body>Plantilla simple</body></html>")
def detalle_post(request,id_post):
	post=get_object_or_404(Post,pk=id_post)
	comentarios=Comentario.objects.filter(post=post)
	return render_to_response('post.html',{'post':post,'comentarios':comentarios},context_instance=RequestContext(request))