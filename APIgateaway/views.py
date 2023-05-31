from rest_framework.views import APIView, status
from .serializers import JobSerializer
from rest_framework.response import Response
from django.db import connection
from .models import Programmer, Data, Network, Cybersecurity
from datetime import datetime
import math
from operator import itemgetter
from itertools import chain


class JobView(APIView):
    def get(self, request, page=1):  # api/job/{page}
        first = 20*(page-1)
        last = 20*(page)
        programmers = Programmer.objects.values()
        datas = Data.objects.values()
        networks = Network.objects.values()
        cybersecuritys = Cybersecurity.objects.values()
        mergeJob = list(chain(programmers, datas, networks, cybersecuritys))
        sortedJob = sorted(mergeJob,  key=itemgetter('date'), reverse=True)
        all_data = len(sortedJob)
        data_dict = {}
        maxPage = math.ceil(all_data/20)
        data_dict['data'] = sortedJob[first:last]
        data_dict['maxPage'] = maxPage
        return Response(data_dict, status=status.HTTP_200_OK)


class JobFilterView(APIView):
    def post(self, request, page=1):
        data = request.data
        first = 10*(page-1)
        last = 10*(page)
        data_dict = {}
        print(data["type"])
        if data["type"] == "programmer":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Programmer.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
                data_length = len(Programmer.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values())
            else:
                programmers = Programmer.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]
                data_length = len(Programmer.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values())

            maxPage = math.ceil(data_length/10)
            data_dict['data'] = programmers
            data_dict['maxPage'] = maxPage
            return Response(data_dict, status=status.HTTP_200_OK)
        elif data["type"] == "data":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Data.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
                data_length = len(Data.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values())
            else:
                programmers = Data.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]
                data_length = len(Data.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values())

            maxPage = math.ceil(data_length/10)
            data_dict['data'] = programmers
            data_dict['maxPage'] = maxPage
            return Response(data_dict, status=status.HTTP_200_OK)
        elif data["type"] == "network":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
                data_length = len(Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values())
            else:
                programmers = Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]
                data_length = len(Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values())

            maxPage = math.ceil(data_length/10)
            data_dict['data'] = programmers
            data_dict['maxPage'] = maxPage
            return Response(data_dict, status=status.HTTP_200_OK)
        elif data["type"] == "cybersecurity":
            if data["date"] != "":
                startdate = datetime.today()
                programmers = Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values()[first:last]
                data_length = len(Network.objects.filter(
                    date__range=[data["date"], startdate]).filter(location__contains=data["location"]).filter(company__contains=data["company"]).values())
            else:
                programmers = Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values()[first:last]
                data_length = len(Network.objects.filter(location__contains=data["location"]).filter(
                    company__contains=data["company"]).values())

            maxPage = math.ceil(data_length/10)
            data_dict['data'] = programmers
            data_dict['maxPage'] = maxPage
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
