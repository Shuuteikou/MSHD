#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("/data_resolver/index_20200514")

def register(request):
	return HttpResponseRedirect("/data_resolver/register")