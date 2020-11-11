from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .models import timeUsage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    
    context = {
        'date': 'today'
    }
    return render(request, 'home/welcome.html', context)
