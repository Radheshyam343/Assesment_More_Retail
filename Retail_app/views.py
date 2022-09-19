from http.client import HTTPResponse
from .models import Product_record,Transaction_record
from .serializers import Product_recordSerializer,Transaction_recordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def Product_record_list(request):
    if request.method == 'GET':
        products = Product_record.objects.all()
        serializer = Product_recordSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = Product_recordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Product_record_list(request,pk):
    try:
        products = Product_record.objects.get(pk = pk)
    except Product_record.DoesNotExist:
        return HTTPResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = Product_recordSerializer(products)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = Product_recordSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST'])
def Transaction_record_list(request,pk):
    if request.method == 'GET':
        transactions = Transaction_record.objects.get(Transactions_id=pk)
        serializer = Transaction_recordSerializer(transactions,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = Transaction_recordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Transaction_record_list(request,):
    try:
        transactions = Transaction_record.objects.all()
    except Transaction_record.DoesNotExist:
        return HTTPResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = Transaction_recordSerializer(transactions)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = Transaction_recordSerializer(transactions,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        transactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





