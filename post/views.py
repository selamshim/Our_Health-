from django.shortcuts import render
from django.views import generic
from .models import Issue

# Create your views here.
class IssueList(generic.ListView):
       model = Issue