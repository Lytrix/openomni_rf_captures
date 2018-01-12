from django.views.generic import TemplateView
#from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.export import TableExport

from rest_framework import viewsets, generics

from openomni.api.models import RawCapture, Action
from openomni.api.tables import CapturesTable
from openomni.api.serializers import (RawCaptureSerializer,
                                         ActionSerializer,
                                         UserSerializer,
                                         )
from openomni.api.filters import RawCaptureFilter



class FilteredCaptureListView(SingleTableMixin, FilterView):
    table_class = CapturesTable
    model = RawCapture
    template_name = 'capture_list.html'

    filterset_class = RawCaptureFilter


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class RawCaptureViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Raw Capture objects """
    queryset = RawCapture.objects.all()
    serializer_class = RawCaptureSerializer


class ActionViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Action objects """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


def capture_list(request):
    table = CapturesTable(RawCapture.objects.all())
    export_format = request.GET.get('_export', None)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'capture_list.html', {'table': table})