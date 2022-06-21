from django.urls import reverse
from django.db import models

# Create your models here.
class FileModel(models.Model):
	title = models.CharField(max_length=50,default='',verbose_name='Заголовок')#verbose_name for admin
	sender = models.CharField(max_length=50,default='user',verbose_name='Отправитель')
	time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
	time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
	file = models.FileField(upload_to='files',verbose_name='Путь к файлу')#upload_to='specs'
	def __str__(self):
		return self.title
	def get_absolute_url(self):#for admin panel
		return reverse('show',kwargs={'file_id':self.pk})

	class Meta:
		verbose_name = "Файл"
		verbose_name_plural = "Файлы"
		ordering = ['-time_update','-time_create']

# class UserModel(models.Model):
# 	name = models.CharField(max_length=50,default='',verbose_name='Имя')#verbose_name for admin
# 	time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
# 	time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
# 	passwrord
# 	def __str__(self):
# 		return self.name
# 	# def get_absolute_url(self):#for admin panel
# 	# 	return reverse('show',kwargs={'file_id':self.pk})

# 	class Meta:
# 		verbose_name = "Пользователь"
# 		verbose_name_plural = "Пользователи"
# 		ordering = ['-time_update','-time_create']


# class MyLongTestModel(models.Model):
# 	title = models.CharField(max_length=50,default='',verbose_name='Заголовок')#verbose_name for admin
# 	user = models.CharField(max_length=50,default='user',verbose_name='Пользователь')
# 	time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
# 	file = models.FileField(upload_to='files',verbose_name='Путь к файлу')#upload_to='specs'
# 	is_processing = models.BooleanField(default=False)
# 	user_id = models.ForeignKey(default=False)
# 	def __str__(self):
# 		return self.title
# 	def get_absolute_url(self):#for admin panel
# 		return reverse('show',kwargs={'file_id':self.pk})

# 	class Meta:
# 		verbose_name = "Файл"
# 		verbose_name_plural = "Файлы"
# 		ordering = ['-time_update','-time_create']

# class MyCountingTestModel():
# 	current_threads_number=0

# 	def __init__(self,max_threads_number=5):
# 		self.max_threads_number = max_threads_number;
# 	def check()
# 		return state;
