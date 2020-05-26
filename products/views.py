from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.views.generic import TemplateView
from django.db.models import Q

# Create your views here.
def home(request):
    products = Product.objects
    return render(request,'products/home.html',{'products':products})

class ListProductsByTag(TemplateView):

	template_name = 'products/search.html'

	def get(self, request, *args, **kwargs):

		tag_url = kwargs['tag']
		print(tag_url)
		context = {}
		context['products'] = Product.objects.filter(tag__syntax=tag_url)


		# term = kwargs['term']
		# Qd = Q()
		# Qd |= Q(name__icontains=term)
		# Qd |= Q(author__icontains=term)

		# context['products'] = Product.objects.filter(Qd)


		return render(request, self.template_name, context)

def search(request):
    products = Product.objects
    return render(request, 'products/search.html',{'products':products})


@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+str(product.id)) 
        else:
            return render(request, 'products/create.html',{'Error':'All fields required!'})
    else:
        return render(request,'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required(login_url="/accounts/login")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/'+str(product.id))
