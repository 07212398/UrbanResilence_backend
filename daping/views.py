from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from collections import defaultdict


import sys
print(sys.path)

from .models import RankingList
from .models import Monthcountall
from .models import Monthcountly
from .models import RegionCount
from .models import EventsReason
from .models import MonthCountavgm
from .models import MonthCountavgy
from .models import MonthCount

def index(request):
    
    return render(request, 'index.html')

from django.core import serializers
import json
from django.http import JsonResponse

def merge_dict(d1, d2):
    d = defaultdict(list)

    for dd in (d1, d2):
        for key, value in d.items():
            if isinstance(value, list):
                dd[key].extend(value)
            else:
                dd[key].append(value)
    return dict(dd)



def rank_list(request):
    ranking_list = RankingList.objects.all()
    rl_str = serializers.serialize("json", ranking_list)
    rl = json.loads(rl_str)
    print(rl)   
    #[{'model': 'daping.rankinglist', 'pk': '西湖区', 'fields': {'count': 2}}, {'model': 'daping.rankinglist', 'pk': '道里区', 'fields': {'count': 1}}]
    
    return HttpResponse(json.dumps(rl), content_type='application/json')

def month_countall(request):
    monthcountall = Monthcountall.objects.all()
    rl_str = serializers.serialize("json", monthcountall)
    rl = json.loads(rl_str)
    print(rl)   
    #[{'model': 'daping.rankinglist', 'pk': '西湖区', 'fields': {'count': 2}}, {'model': 'daping.rankinglist', 'pk': '道里区', 'fields': {'count': 1}}]
    
    return HttpResponse(json.dumps(rl), content_type='application/json')

def month_countly(request):
    monthcountly = Monthcountly.objects.all()
    rl_str = serializers.serialize("json", monthcountly)
    rl = json.loads(rl_str)
    print(rl)   
    #[{'model': 'daping.rankinglist', 'pk': '西湖区', 'fields': {'count': 2}}, {'model': 'daping.rankinglist', 'pk': '道里区', 'fields': {'count': 1}}]
    
    return HttpResponse(json.dumps(rl), content_type='application/json')

def region_count(request):
    region_counting = RegionCount.objects.all()
    rl_str = serializers.serialize("json", region_counting)
    rl = json.loads(rl_str)
    print(rl)

    return HttpResponse(json.dumps(rl), content_type='application/json')

def events_reason(request):
    events_reasoning = EventsReason.objects.all()
    rl_str = serializers.serialize("json", events_reasoning)
    rl = json.loads(rl_str)
    print(rl)

    return HttpResponse(json.dumps(rl), content_type='application/json')

def month_countavgm(request):
    month_countavgm = MonthCountavgm.objects.all()
    rl_str = serializers.serialize("json", month_countavgm)
    rl = json.loads(rl_str)
    print(rl)   

    return HttpResponse(json.dumps(rl), content_type='application/json')

def month_countavgy(request):
    month_countavgy = MonthCountavgy.objects.all()
    rl_str = serializers.serialize("json", month_countavgy)
    rl = json.loads(rl_str)
    print(rl)   

    return HttpResponse(json.dumps(rl), content_type='application/json')

def month_count(request):
    month_count = MonthCount.objects.all()
    rl_str = serializers.serialize("json", month_count)
    rl = json.loads(rl_str)
    print(rl)   

    return HttpResponse(json.dumps(rl), content_type='application/json')

def getmonth(request):
    month_countavgy = MonthCountavgy.objects.all()
    print(month_countavgm)
    month_countavgm = MonthCountavgm.objects.all()
    monthcountly = Monthcountly.objects.all()
    monthcountall = Monthcountall.objects.all()
    rl_str = serializers.serialize("json", month_countavgy)
    rl = json.loads(rl_str)
    r2_str = serializers.serialize("json", month_countavgm)
    r2 = json.loads(r2_str)
    r3_str = serializers.serialize("json", monthcountly)
    r3 = json.loads(r3_str)
    r4_str = serializers.serialize("json", monthcountall)
    r4 = json.loads(r4_str)

    return HttpResponse(json.dumps(rl), content_type='application/json')


def myview(_request):
    response = HttpResponse(json.dumps({"key": "value","key2":"value"}))
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Alow-Methods"] ="POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] ="1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response