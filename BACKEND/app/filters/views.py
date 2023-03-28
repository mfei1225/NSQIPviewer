from .models import NSQIP2018,NSQIP_META,NSQIP2017,NSQIP2016,NSQIP2015,NSQIP2014,NSQIP2013,NSQIP2012,NSQIP2011,NSQIP2010,NSQIP2009,NSQIP2008
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from itertools import chain
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet

DATA_TABLES = [NSQIP2018,NSQIP2017,NSQIP2016,NSQIP2015,NSQIP2014,NSQIP2013,NSQIP2012,NSQIP2011,NSQIP2010,NSQIP2009,NSQIP2008]
#DATA_TABLES = [NSQIP2008]
class RecordCount(APIView):
    def get(self, request):
        result = {}
        for model in DATA_TABLES:
            result[model.objects.model._meta.db_table]=model.objects.all().count()
        result = [{'db':k,'count':v} for k,v in result.items()]
        return Response(result)
    
class ColumnsNames(APIView):
    def get(self, request):
        col = set([field.name for field in NSQIP2018._meta.get_fields()]) 
        return Response(col)
    
class ColumnsDetails(ReadOnlyModelViewSet):
    def list(self, request):
        result = NSQIP_META.objects.all().values()  
        return Response(result)

    def retrieve(self, request,pk):
        pk1 = " ".join(pk.split("_"))
        pk2 = " ".join(pk.split("_"))
        result = NSQIP_META.objects.get(Q(Name__iexact=pk1) | Q(Name__iexact=pk2)).Label
        result = {'label':result,'type': NSQIP2018._meta.get_field(pk.lower()).__class__.__name__}
        return Response(result)

class FilterView(APIView):
    def post(self, request):
        filter_query_and = Q()
        result = {}
        for group in request.data['filters']:
            filter_query_or = Q()
           
            for searchTerm in group['searchTerms']:
                filter_query_or.add(Q(**{ group['filter'].lower() : int(searchTerm)}), Q.OR)
            filter_query_and.add(filter_query_or, Q.AND)
        for model in DATA_TABLES:
            result[model.objects.model._meta.db_table]=model.objects.filter(filter_query_and).count()
        result = [{'db':k,'count':v} for k,v in result.items()]

        return Response(result)

class FilterExportView(APIView):
    def post(self, request):
        filter_query_and = Q()
        result_perdb = {}
        select = [item.lower() for item in request.data['selectColumns']]
        for group in request.data['filters']:
            filter_query_or = Q()
            for searchTerm in group['searchTerms']:
                filter_query_or.add(Q(**{ group['filter'].lower()  : int(searchTerm)}), Q.OR)
            filter_query_and.add(filter_query_or, Q.AND)
        for model in DATA_TABLES:
            result_perdb[model.objects.model._meta.db_table]=model.objects.filter(filter_query_and).values(*select)
        querysets = []
        for value in result_perdb.values():
            querysets.append(value)
        result = list(chain(*querysets))
        

        return Response(result)




      
    


