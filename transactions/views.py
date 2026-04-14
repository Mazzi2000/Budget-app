from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer

# GET all transactions
@api_view(['GET', 'POST'])
def transactionFunView(request):
	if request.method=="GET":
		transactions = Transaction.objects.filter(user=request.user)
		serializer = TransactionSerializer(transactions, many=True)
		return Response(serializer.data)
	else:
		serializer = TransactionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			return Response(serializer.data)
		return Response(serializer.errors)