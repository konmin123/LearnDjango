from datetime import datetime
from django.views import View
from django.http import HttpResponse, HttpRequest


class SimpleView(View):
    def get(self, request: HttpRequest):
        html = f"{datetime.now()}"

        return HttpResponse(html)