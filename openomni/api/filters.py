import django_filters

from openomni.api.models import RawCapture

class RawCaptureFilter(django_filters.FilterSet):
    
    class Meta:
        model = RawCapture
        fields = '__all__' 