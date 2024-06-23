from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Person
from .serializers import PoetSerializers
class ListPoet(APIView):
    def get(self, request):
        lst = Person.objects.all().values()
        return Response({'Poet': PoetSerializers(lst, many=True).data})

    def post(self,requests):
        serializers = PoetSerializers(data=requests.data)
        serializers.is_valid(raise_exception=True)
        posts = Person.objects.create(
            name=requests.data["name"],
            content=requests.data["content"],
            cat_id=requests.data["cat_id"],
        )
        return Response({"posts": PoetSerializers(posts).data})


# class ListPoet(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
