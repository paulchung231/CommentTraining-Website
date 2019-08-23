from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Comment
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from trainingApp.serializers import CommentSerializer
from trainingApp.models import Comment
import pandas as pd
import numpy as np
import csv
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # first_comment =  Comment.objects.get(pk=3)
    # context = {'first_comment':first_comment}
    context = {}
    return render(request, 'trainingApp/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse("Inside training website index. Add test")

class CommentView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk) #Hardcode to get comment with pk of 1
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

#Returns a random comment in the database
class RandomCommentView(APIView):
    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        random_comment = random.choice(all_comments)
        serializer = CommentSerializer(random_comment)
        return Response(serializer.data)

#   Used purely for initializing the database with the comments. Make a POST request
#   and see that there is a filepath that should lead to a dataset with the same format
#   as the NYT comments
class CommentListView(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # code below will initialize the NBA player database
        with open("/Users/paulchung/Desktop/Test_Comments.csv") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Comment.objects.get_or_create(
                    comment_text=row[3]
                    )
        return Response(status=status.HTTP_201_CREATED)
