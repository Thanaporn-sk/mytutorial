from django.shortcuts import render

# Create your views here.
def d3Chain(request):

  return render(request,'d3/d3.html')

def d3circlepack(request):

  return render(request,'d3/d3circlepack.html') 

def d3lineChart(request):

  return render(request,'d3/d3lineChart.html') 

def d3multiLineChart(request):

  return render(request,'d3/d3multiLineChart.html')  

def d3barChart(request):

  return render(request,'d3/d3barChart.html') 

def d3sunburst(request):

  return render(request,'d3/d3sunburst.html')     