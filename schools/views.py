from django.shortcuts import render, get_object_or_404
from .models import School, District
from django.db.models import Sum
from django.shortcuts import render
from .models import School
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, 'schools/home.html')

def school_list(request):
    state = request.GET.get('state')
    schools = School.objects.all()

    if state and state != "All":
        schools = schools.filter(state=state)

    states = School.objects.values_list('state', flat=True).distinct().order_by('state')

    return render(request, 'schools/school_list.html', {
        'schools': schools,
        'states': states,
        'selected_state': state,
    })


def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'schools/school_detail.html', {'school': school})

def district_detail(request, pk):
    district = get_object_or_404(District, pk=pk)
    schools = School.objects.filter(district=district)
    return render(request, 'schools/district_detail.html', {'district': district, 'schools': schools})

def enrollment_by_state(request):
    data = (
        School.objects
        .values('state')
        .annotate(total=Sum('enrollment'))
        .order_by('-total')[:10]  # Top 10 states
    )

    labels = [entry['state'] for entry in data]
    values = [entry['total'] for entry in data]

    return render(request, 'schools/enrollment_chart.html', {
        'labels': labels,
        'values': values,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'schools/register.html', {'form': form})
