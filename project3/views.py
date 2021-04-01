from django.http import HttpResponse
import os
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1> you are watching homepage</h1>")

# file_path=os.path.abspath(__file__)
# pro_dir_path=os.path.dirname(file_path)
# dir_path=os.path.dirname(pro_dir_path)
# def html_respo(request):
#     file_addr=os.path.join(dir_path,"sample.html")
#     fp=open(file_addr,"r")
#     data=fp.read()
#     return HttpResponse(data)
def rend_demo(request):
    return render(request,"sample.html")
def sam_demo(request):
    return render(request,"html_demo/sample.html")

