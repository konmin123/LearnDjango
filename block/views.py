from rest_framework.views import Response, APIView

from .models import Note


class BlogApiView(APIView):
    def get(self, request):
        return Response(data=Note)

    def post(self, request):
        new_blog = request.data
        Note.append(new_blog)

        return Response(data=new_blog)

    def put(self, request):
        ...
