from .models import Nsqip2018
from rest_framework.views import APIView
from rest_framework.response import Response

class RecordCount(APIView):
    def get(self, request):
        count = Nsqip2018.objects.all().count()
        return Response(count)

