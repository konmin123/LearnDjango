from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from block.models import Note
from . import serializers


class NoteListCreateAPIView(APIView):
    def get(self, request: Request):
        objects = Note.objects.all()
        return Response([serializers.note_to_json(obj) for obj in objects])



