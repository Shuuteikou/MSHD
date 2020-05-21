#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("/data_resolver/details_xmxx")