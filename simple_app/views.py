from datetime import datetime
from django.views import View
from django.http import HttpResponse, HttpRequest


class SimpleView(View):
    def get(self, request: HttpRequest):
        html = f"{datetime.now()}"

        return HttpResponse(html)


class SimpleView1(View):
    def get(self, request:HttpRequest):
        html = f"Hi"

        return HttpResponse(html)

    def post(self, request: HttpRequest):
        ...

    def put(self, request: HttpRequest):
        ...
