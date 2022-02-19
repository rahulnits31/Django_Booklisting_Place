from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Post(models.Model):
	CONDITION_TYPE = (
		("Science" , "Science") ,
		("Arts" , "Arts"),
		("Commerce" , "Commerce"),
		("Engineering" , "Engineering")

	)

	bookname = models.CharField(max_length=100)
	description = models.TextField()
	Contact_no= PhoneNumberField(default='XXXXXXXXXXX')
	Address=models.TextField(default='contact me via call')
	category = models.CharField(max_length=100 , choices=CONDITION_TYPE,default="Arts")
	image = models.ImageField(upload_to='bookpics/' ,default='default.jpg')
	price = models.DecimalField(max_digits=10,decimal_places=5,default='000')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=200, db_index=True)
	def __str__(self):
		return self.bookname


	
	def get_absolute_url(self):
		return reverse('post-detail',args=[str(self.slug)])
