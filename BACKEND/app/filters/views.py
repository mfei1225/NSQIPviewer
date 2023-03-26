from .models import NSQIP_2018,NSQIP_META
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json

from django.http import JsonResponse
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet

class RecordCount(APIView):
    def get(self, request):

        count = NSQIP_2018.objects.all().count()
        return Response(count)
    
class ColumnsNames(APIView):
    def get(self, request):
        col = [field.name for field in NSQIP_2018._meta.get_fields()] 
        return Response(col)
    
class ColumnsDetails(ReadOnlyModelViewSet):
    def list(self, request):
        result = NSQIP_META.objects.all().values()  
        return Response(result)

    def retrieve(self, request,pk):
        pk1 = " ".join(pk.split("_"))
        pk2 = "".join(pk.split("_"))
        result = NSQIP_META.objects.get(Q(Name__iexact=pk1) | Q(Name__iexact=pk2)).Label
        result = {'label':result,'type': NSQIP_2018._meta.get_field(pk).__class__.__name__}
        return Response(result)

class FilterView(APIView):
    def post(self, request):
        filter_query = Q()

        for f in request.data['filters']:
            print(f)
            filter_name = f['filter'] + '__exact'
            
            filter_query.add(Q(**{ f['filter'] : f['searchTerm']}), Q.AND)
        filtered = NSQIP_2018.objects.filter(filter_query).count()
        print(filtered)
        return Response(filtered)




      
    


