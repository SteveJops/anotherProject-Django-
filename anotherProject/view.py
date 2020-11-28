from django.shortcuts import render
from django.views import View


class MyView(View):
    def get(self, request):
        return render(request, "viceversa.html")


class ReverseCommand(View):
    def get(self, request):
        user_text = request.GET['usertext']
        reverse = user_text[::-1]
        return render(request, "reverse.html", {'usertext': user_text, 'reversed': reverse})
