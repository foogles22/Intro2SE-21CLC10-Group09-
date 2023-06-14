from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Index(View):
    def get(self, request):
        return HttpResponse('Đây là trang chính của Librarian')