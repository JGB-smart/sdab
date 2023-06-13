from django.shortcuts import render

def intro(request):

    return render(request,'intro.html')

def tema1(request):

    return render(request,'tema1.html')


def tema2(request):

    return render(request,'tema2.html')

def tema3(request):

    return render(request,'tema3.html')