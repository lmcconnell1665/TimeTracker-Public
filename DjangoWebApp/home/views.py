from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .models import timeUsage

# Create your views here.

def home_view(request):
    
    context = {
        'date': 'today'
    }
    return render(request, 'home/welcome.html', context)
