from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name="Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['pub_date']
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    


class Tag(models.Model):
	syntax = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return(self.syntax)