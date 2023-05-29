from rest_framework.views import APIView, status
from .serializers import JobSerializer
from rest_framework.response import Response
from django.db import connection
from .models import Programmer, Data, Network, Cybersecurity
from datetime import datetime


class JobView(APIView):
    def get(self, request, page=1):  # api/job/{page}
        first = 5*(page-1)
        last = 5*(page)
        programmers = Programmer.objects.values()[first:last]
        datas = Data.objects.values()[first:last]
        networks = Network.objects.values()[first:last]
        cybersecuritys = Cybersecurity.objects.values()[first:last]
        merge = []  # mix data
        for i in range(5):
            merge.append(programmers[i])
            merge.append(datas[i])
            merge.append(networks[i])
            merge.append(cybersecuritys[i])
        return Response(merge, status=status.HTTP_200_OK)


class JobFilterView(APIView):
    def post(self, request, page=1):
        data = request.data
        first = 5*(page-1)
        last = 5*(page)
        print(data["type"])
        if data["type"] == "programmer":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Programmer.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
            else:
                programmers = Programmer.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "data":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Data.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
            else:
                programmers = Data.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "network":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
            else:
                programmers = Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "cybersecurity":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Cybersecurity.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
            else:
                programmers = Cybersecurity.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]

            return Response(programmers, status=status.HTTP_200_OK)
        return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
