from rest_framework import serializers

from .models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
		read_only_fields = ['user']

class TransactionSerializer(serializers.ModelSerializer):
	category = serializers.SlugRelatedField(read_only=True, slug_field='name')
	class Meta:
		model = Transaction
		fields = '__all__'
		read_only_fields = ['user', 'updated_timestamp']

