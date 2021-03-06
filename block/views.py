from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from block.models import Note
from . import serializers


class NoteListCreateAPIView(APIView):
    def get(self, request: Request):
        objects = Note.objects.all()
        return Response([serializers.note_to_json(obj) for obj in objects])

    def post(self, request: Request):
        data = request.data
        note = Note(**data)
        note.save(force_insert=True)

        return Response(
            serializers.note_add_new(note),
            status=status.HTTP_201_CREATED
        )


class NoteDetailAPIView(APIView):
    def get(self, request: Request, pk):
        note = get_object_or_404(Note, pk=pk)
        return Response(serializers.note_to_json(note))
