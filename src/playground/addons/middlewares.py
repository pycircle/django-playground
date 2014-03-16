# -*- coding: utf-8 -*-

from django.http import HttpResponsePermanentRedirect
import re

class OpenshiftRedirectMiddleware(object):
    """
    This middleware redirects openshift domain to your.
    """
    def process_request(self, request):
        if re.match(r"\w+-\w+\.rhcloud\.com", request.get_host()):
            return HttpResponsePermanentRedirect("http://www.mypage.com" + request.path_info)