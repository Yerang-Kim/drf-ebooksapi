from rest_framework import generics
from rest_framework import mixins

from ebooks.models import Ebook
from ebooks.api.serializers import EbookSerializer

class EbookListCreateAPIView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)