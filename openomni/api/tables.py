import django_tables2 as tables
from openomni.api.models import RawCapture


class CapturesTable(tables.Table):
    class Meta:
        model = RawCapture