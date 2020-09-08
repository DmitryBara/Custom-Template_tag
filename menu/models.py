from django.db import models



class Menu(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name


class MenuElement(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # related menu object
	title = models.CharField(max_length=20)	# name of category or item (without child)
	number = models.IntegerField()	# number for identification obj in current category
	path = models.CharField(max_length=100) # path to this obj
	is_parent = models.BooleanField(default=False)
	# If you want to keep url in database
	url = models.CharField(max_length=100)


	# All app part getting url addres through the method get_url.
	# You could use other stirng as url (self.path for example)
	def __str__(self):
		return (self.path + ' --- ' + self.title)

	def level(self):
		level = self.path.count('.')
		return level

	def get_url(self):
		return self.url

