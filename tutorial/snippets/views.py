from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    #this auto provides 'list' 'create' 'update' 'retrieve' and 'destroy'
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    #URL endpoints are derived from the name of the method 
    
    @action(detail=True, renderers_classes=[renderers.StaticHTMLRenderer])
    #@action responds to GET automatically. the url path is also auto added
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    #runs before saving to database
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #this viewset auto provides 'list' and 'retrieve' functions
    queryset = User.objects.all()
    serializer_class = UserSerializer


    