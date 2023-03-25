from .models import NSQIP_2018,NSQIP_META
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers

from django.http import JsonResponse
from django.db.models import Q

class RecordCount(APIView):
    def get(self, request):

        count = NSQIP_2018.objects.all().count()
        return Response(count)
    
class ColumnsNames(APIView):
    def get(self, request):
        col = [field.name for field in NSQIP_2018._meta.get_fields()] 
        return Response(col)
    
class ColumnsDetails(APIView):
    def get(self, request):
        result = NSQIP_META.objects.all().values()  
        return Response(result)

class ColumnsDetailsSingle(APIView):
    def get(self, request,filter):
        filter1 = " ".join(filter.split("_"))
        filter2 = "".join(filter.split("_"))
        print(filter2,filter1)
    
        result = NSQIP_META.objects.get(Q(Name__iexact=filter1) | Q(Name__iexact=filter2)).Label

        return Response(result)
      
    


