from django.db import models
from django.conf import settings

from datetime import date

# def get_or_create_default_category():
# 	category, _ = Category.objects.get_or_create(name="Other")
# 	return category.id

def get_todays_date():
	today = date.today()
	return today

class Category(models.Model):
	"""
	Model for the expense/income category
	Each category is associated with a user.
	"""
	name = models.CharField(max_length=100)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="category")

	def __str__(self):
		return (f"{self.name}")

	class Meta:
		verbose_name_plural = 'Categories' 

class Transaction(models.Model):
	"""
	Model for transcations. Records both Income and Expenses.
	"""
	class TypeChoices(models.TextChoices):
		EXPENSE = "Ex", "Expense"
		INCOME = "In", "Income"
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="transaction")
	description = models.TextField(blank=True, null=True)	
	date = models.DateField(blank=True, default=get_todays_date)
	transaction_type = models.CharField(max_length=2, choices=TypeChoices.choices)
	updated_timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transaction")

	def __str__(self):
		return (f"{self.transaction_type} on {self.date} of {self.amount}")