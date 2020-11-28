from django.shortcuts import render
from django.views import View


class MyView(View):
    def get(self, request):
        return render(request, "viceversa.html")


class ReverseCommand(View):

    def get(self, request):
        user_text = request.GET['usertext']
        number_of_words = self.numberofwords(user_text)
        reverse = user_text[::-1]
        return render(request, "reverse.html",
                      {'usertext': user_text, 'reversed': reverse, 'numberofwords': number_of_words})

    def numberofwords(self, user_text):
        count = 0
        flag = 0
        for i in range(len(user_text)):
            if user_text[i] != ' ' and flag == 0:
                count += 1
                flag = 1
            else:
                if user_text[i] == ' ':
                    flag = 0
        return count
