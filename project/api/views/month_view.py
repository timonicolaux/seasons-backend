from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404

from api.models import MonthModel
from api.serializers import MonthSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter

class MonthView(APIView):
    @extend_schema(
            summary="Détail d'un mois via son id",
            parameters=[
                OpenApiParameter(name='id', required=True, type=int, location=OpenApiParameter.PATH),
            ],
            responses={
                200: MonthSerializer,
                404: {"description": "Month not found"},
                500: {"description": "Unexpected error"}
            }
    )
    def get(self, request, id=None):
        try:
            month = get_object_or_404(MonthModel, id=id)
            return Response({'month detail': MonthSerializer(month).data}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'error': 'Month not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MonthListView(APIView):
    @extend_schema(
            summary="Liste des mois",
            responses={
                200: MonthSerializer(many=True),
                500: {"description": "Unexpected error"}
            }
    )
    def get(self, request):
        try:
            months = MonthModel.objects.all()
            return Response({'month list': MonthSerializer(months, many=True).data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
