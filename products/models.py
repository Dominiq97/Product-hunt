from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

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
    image = FilerFileField(null=True, blank=True, related_name="file+", on_delete=models.CASCADE)
    icon = FilerImageField(null=True, blank=True, related_name="image+", on_delete=models.CASCADE)
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

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

class Comment(models.Model):
    message = models.TextField('Message')
    date_comment = models.DateField(auto_now_add=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    


class Tag(models.Model):
	syntax = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return(self.syntax)