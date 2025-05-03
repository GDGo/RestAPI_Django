from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View
    class based view разбивает свою функциональность на методы, которые
    соответствуют http методам
    Каждый метод при вызове должен возвращать объект типа Response"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """request - все заголовки, все типы и прочее,
        что приходит в запросе от пользователя
        format - указание на формат ответ json и прочее,
        если не указано, то используется тип формат, который
        пришел в запросе"""
        an_apiview = [
            '1',
            '2',
            '3'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello, {name}'
            return Response(dict(message=message))
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            '4',
            '5',
            '6'
        ]
        return Response(
            dict(
                message='Hello',
                a_viewset=a_viewset
            )
        )

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handler getting an object by its ID"""

        return Response(
            dict(
                view_method='retrieve()',
                http_method=request.method
            )
        )

    def update(self, request, pk=None):
        """Handle updating an object by its ID"""

        return Response(
            dict(
                view_method='update()',
                http_method=request.method
            )
        )

    def partial_update(self, request, pk=None):
        """Handle partional_update an object by its ID"""

        return Response(
            dict(
                view_method='partional_update()',
                http_method=request.method
            )
        )

    def destroy(self, request, pk=None):
        """Handle destroy an object by its ID"""

        return Response(
            dict(
                view_method='destroy()',
                http_method=request.method
            )
        )