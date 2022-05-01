from rest_framework.views import Response, APIView

from .models import BLOGS


class BlogApiView(APIView):
    def get(self, request):
        return Response(data=BLOGS)

    def post(self, request):
        ...
