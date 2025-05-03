from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View
    class based view разбивает свою функциональность на методы, которые
    соответствуют http методам
    Каждый метод при вызове должен возвращать объект типа Response"""

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