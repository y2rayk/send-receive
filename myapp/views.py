from rest_framework_json_api.views import viewsets
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

class MessageFilter(filters.FilterSet):
    id__gt = filters.NumberFilter(field_name='id', lookup_expr='gt')
    id__lt = filters.NumberFilter(field_name='id', lookup_expr='lt')

    class Meta:
        model = Message
        fields = ['id', 'seen', ]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('id', 'seen',)
    filterset_class = MessageFilter

    @action(detail=False, methods=['post',], permission_classes=[permissions.IsAuthenticated])
    def delete_many(self, request):
        try:
            lo_ids =[ int(x) for x in request.query_params['ids'].split(',')]
        except ValueError:
            return Response("Check input.", status=400)
        results = Message.objects.filter(id__in=lo_ids).delete()
        return Response("OK.")
