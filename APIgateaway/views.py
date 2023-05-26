from rest_framework.views import APIView, status
from .serializers import JobSerializer
from rest_framework.response import Response
from django.db import connection
from .models import Programmer, Data, Network, Cybersecurity
from django.core import serializers
from datetime import datetime, timedelta


class JobView(APIView):
    def get(self, request):
        # programmer = Programmer.objects.filter(
        #     title__contains="Programmer").values()
        # print(programmer)
        programmers = Programmer.objects.values()[:5]
        datas = Data.objects.values()[:5]
        networks = Network.objects.values()[:5]
        cybersecuritys = Cybersecurity.objects.values()[:5]
        merge = []  # mix data
        for i in range(5):
            merge.append(programmers[i])
            merge.append(datas[i])
            merge.append(networks[i])
            merge.append(cybersecuritys[i])
        # merge = programmers | datas
        # prog_json = serializers.serialize('json',  Programmer.objects.values())
        # cursor = connection.cursor()
        # cursor.execute("SELECT * FROM programmer")
        # row = cursor.fetchall()
        return Response(merge, status=status.HTTP_200_OK)

    def post(self, request):
        # serializers = JobSerializer(data=request.data)
        # if serializers.is_valid():
        data = request.data
        print(data["type"])
        if data["type"] == "programmer":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Programmer.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[:10]
            else:
                programmers = Programmer.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[:10]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "data":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Data.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[:10]
            else:
                programmers = Data.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[:10]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "network":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[:10]
            else:
                programmers = Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[:10]

            return Response(programmers, status=status.HTTP_200_OK)
        elif data["type"] == "cybersecurity":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Cybersecurity.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[:10]
            else:
                programmers = Cybersecurity.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[:10]

            return Response(programmers, status=status.HTTP_200_OK)
        return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializers = JobSerializer(data=request.data)
    #     if serializers.is_valid():
    #         data = serializers.data
    #         # print("SELECT * FROM %s WHERE date > %s",
    #         #       [data["type"], data["date"]])
    #         sql_query = "SELECT * FROM " + data["type"]
    #         if data["date"] != "":
    #             sql_query += "WHERE data > "
    #         cursor = connection.cursor()
    #         cursor.execute(
    #             "SELECT * FROM programmer WHERE date > %s", [data["date"]])
    #         row = cursor.fetchall()
    #         return Response(row, status=status.HTTP_200_OK)
    #     return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
