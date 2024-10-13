from rest_framework import mixins, generics, permissions
from rest_framework.authentication import TokenAuthentication
from core.models import Webtoons
from .serializers import WebtoonsSerializer


class WebtoonListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Webtoons.objects.all()
    serializer_class = WebtoonsSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class WebtoonCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Webtoons.objects.all()
    serializer_class = WebtoonsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Associate the webtoon with the authenticated user"""
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WebtoonDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Webtoons.objects.all()
    serializer_class = WebtoonsSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class WebtoonDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Webtoons.objects.all()
    serializer_class = WebtoonsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
