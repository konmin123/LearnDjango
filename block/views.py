from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class NoteListCreateAPIView(APIView):
    def get(self, request: Request):
        return Response({'Test': 'Test'})



