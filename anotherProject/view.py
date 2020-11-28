from django.shortcuts import render
from django.views import View


class MyView(View):
    def get(self, request):
        return render(request, "viceversa.html")
