from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Tag, Category,Comment
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

 #   def post(self, request, *args, **kwargs):
 #       term = kwargs['term']
 #       Qd |= Q(syntax__icontains=term)
 #       context['products'] = Product.objects.filter(Qd)
    
    
def search(request):

    template = 'products/search.html'
    query = request.GET.get('q')
    results = Product.objects.filter(Q(tag__syntax=query))    
    return render(request,template,{'products':results})


def category(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'products/categories.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.
    

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

@login_required(login_url="/accounts/login")
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comment = Comment.objects.filter(product_id=product_id)
    tags = Tag.objects.filter(Q(products=product))
    if request.method == 'POST':
        if request.POST['comment']:
            comment = Comment()
            comment.product_id=product
            comment.user_id=request.user
            comment.message=request.POST['comment']
            comment.save()
            return redirect('products/detail.html')
        else:
            return render(request,'products/detail.html',{'error':'No comment written'})
    else:
        return render(request,'products/detail.html',{'product':product,'tags':tags,'comments':comment})
    


#def category(request):
#    products = Product.objects.filter(Q(category=1))
#    return render(request,'products/categories.html',{'products':products})

#def category(request):
#    template = 'products/categories.html'
#    query = request.GET.get('cat')
#    results = Product.objects.filter(Q(category__name=query))    
#    return render(request,template,{'products':results})


@login_required(login_url="/accounts/login")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/'+str(product.id))

    class Meta:
        unique_together = (('user','suggestedName'),)
