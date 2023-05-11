from .models import NSQIP2018,NSQIP_META,NSQIP2017,NSQIP2016,NSQIP2015,NSQIP2014,NSQIP2013,NSQIP2012,NSQIP2011,NSQIP2010,NSQIP2009,NSQIP2008
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from rest_framework import serializers
from itertools import chain
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import Max,Min

DATA_TABLES = [NSQIP2018,NSQIP2017,NSQIP2016,NSQIP2015,NSQIP2014,NSQIP2013,NSQIP2012,NSQIP2011,NSQIP2010,NSQIP2009,NSQIP2008]

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
    
##Grace New Endpoint Insert Here
    
class ColumnsDetails(ReadOnlyModelViewSet):
    def list(self, request):
        result = NSQIP_META.objects.all().values()
        print(len(result))
        return Response(result)

    def retrieve(self, request,pk):
        pk1 = " ".join(pk.split("_"))
        pk2 = " ".join(pk.split("_"))
        result = NSQIP_META.objects.get(Q(Name__iexact=pk1) | Q(Name__iexact=pk2))
        if result.values:
            result = {'label':result.Label,'type': result.type,'values':result.values.split(',')}
        else:
            result = {'label':result.Label,'type': result.type,'values':[]}

        return Response(result)

class FilterView(APIView):
    def post(self, request):
        filter_query_and = Q()
        result_perdb = {}
        removed=set()
        select_db= {}
        select = [item.lower() for item in request.data['selectColumns']]

        if not select:
            select=set([field.name for field in NSQIP2018._meta.get_fields()])
            
            for model in DATA_TABLES:
                select =select.intersection(set([field.name for field in model._meta.get_fields()]))
        for model in DATA_TABLES:
            select_db[model.objects.model._meta.db_table] = [*select]
            for s in select:
                if s not in [field.name for field in model._meta.get_fields()]:
                    select_db[model.objects.model._meta.db_table].remove(s)
        for group in request.data['filters']:
            filter_query_or = Q()
            for model in DATA_TABLES:
                if group['filter'].lower() not in [field.name for field in model._meta.get_fields()]:
                    removed.add(model)
            for searchTerm in group['searchTerms']:
                if searchTerm.isnumeric():
                    searchTerm=int(searchTerm)
                filter_query_or.add(Q(**{ group['filter'].lower()  : searchTerm}), Q.OR)
            filter_query_and.add(filter_query_or, Q.AND)
        for model in DATA_TABLES:
            if model in removed or not select_db[model.objects.model._meta.db_table]:
                result_perdb[model.objects.model._meta.db_table]=[]
            else:
                result_perdb[model.objects.model._meta.db_table]=model.objects.filter(filter_query_and).values(*select_db[model.objects.model._meta.db_table])
            
  
        return Response(result_perdb)

class FilterExportView(APIView):
    def post(self, request):
        filter_query_and = Q()
        result_perdb = {}
        removed=set()
        select_db= {}
        select = [item.lower() for item in request.data['selectColumns']]

        if not select:
            select=set([field.name for field in NSQIP2018._meta.get_fields()])
            
            for model in DATA_TABLES:
                select =select.intersection(set([field.name for field in model._meta.get_fields()]))
        for model in DATA_TABLES:
            select_db[model.objects.model._meta.db_table] = [*select]
            for s in select:
                if s not in [field.name for field in model._meta.get_fields()]:
                    select_db[model.objects.model._meta.db_table].remove(s)
        for group in request.data['filters']:
            filter_query_or = Q()
            for model in DATA_TABLES:
                if group['filter'].lower() not in [field.name for field in model._meta.get_fields()]:
                    removed.add(model)
            for searchTerm in group['searchTerms']:
                if searchTerm.isnumeric():
                    searchTerm=int(searchTerm)
                filter_query_or.add(Q(**{ group['filter'].lower()  : searchTerm}), Q.OR)
            filter_query_and.add(filter_query_or, Q.AND)
        for model in DATA_TABLES:
            if model in removed or not select_db[model.objects.model._meta.db_table]:
                result_perdb[model.objects.model._meta.db_table]=[]
            else:
                result_perdb[model.objects.model._meta.db_table]=model.objects.filter(filter_query_and).values(*select_db[model.objects.model._meta.db_table])
            
        
        querysets = []
       
        exclude_null=True
        for db,value in result_perdb.items():
            out = list(chain(value))
            querysets += out
        return Response(querysets)
    
class Populate(APIView):
    
    def post(self, request):
        cols = NSQIP_META.objects.all().values() 
        for col in cols:
            if col['type']=='float':
                for model in DATA_TABLES:
                    col_name = "_".join(col['Name'].lower().split(" "))
                    if col_name in [field.name for field in model._meta.get_fields()]:
                        col_max = float("-inf")
                        col_min =float("inf")
                        temp_max = model.objects.aggregate(Max(col_name))[col_name+'__max']
                        temp_min = model.objects.aggregate(Min(col_name))[col_name+'__min']
                        col_max = max(col_max,temp_max)
                        col_min = min(col_min,temp_min)
                
                t = NSQIP_META.objects.get(Name=col['Name'])
                t.values = str(col_min)+","+str(col_max)
                t.save()
        
        return Response('hi')
    '''
    def post(self, request):
        cols = NSQIP_META.objects.all().values() 
        for col in cols:
            set_model =set()
    
            for model in DATA_TABLES:
                col_name = "_".join(col['Name'].lower().split(" "))
                
                if col_name in [field.name for field in model._meta.get_fields()]:
                    values = model.objects.values_list(col_name, flat = True).distinct()
           
                    set_model.add(values)
                    if len(list(set(chain(*set_model))))>100:
                        break
            set_values = list(set(chain(*set_model)))
            if len(set_values)<100:
                casted = [str(i) for i in set_values]
                insert = ','.join(casted)   
            else:
                insert = None
            if isinstance(set_values[0], str):
                type = 'string'
            elif isinstance(set_values[0], int):
                type = 'int'
            elif isinstance(set_values[0], float):
                type = 'float'
            else:
                type=None
   
            t = NSQIP_META.objects.get(Name=col['Name'])
            t.values = insert
            t.type=type
            t.save()
        return Response('hi')
    '''   
class TestNull(APIView):
    def get(self, request):
  
        count = NSQIP2018.objects.filter(cpt=27130).values()
        print(count)
  
        return Response(count)

class AddNull(APIView):
    def post(self, request):
        select=set([field.name for field in NSQIP2018._meta.get_fields()])
        for model in DATA_TABLES:
            select =select.union(set([field.name for field in model._meta.get_fields()]))
        print(len(select))
        return Response('test')
    


           


        

        





      
    


