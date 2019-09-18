# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime


def home(request):
    today = datetime.date.today()
    # import ipdb; ipdb.set_trace()
    return render(request, "tests/testing_template.html", {'today': today})
