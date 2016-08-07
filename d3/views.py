from django.shortcuts import render

# Create your views here.
def d3Chain(request):

  return render(request,'d3/d3.html')

def d3circlepack(request):

  return render(request,'d3/d3circlepack.html') 

def d3multiLineChart(request):

  return render(request,'d3/d3multiLineChart.html') 