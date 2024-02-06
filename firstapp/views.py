# views.py
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import json
from firstapp.models import employee
from .forms import ModelForm




def emp_api(request):
    emp_data = employee.objects.all()
    serialized_data = serialize("json", emp_data)
    serialized_data = json.loads(serialized_data)
    print(serialized_data)
    return JsonResponse(serialized_data, status=200, safe=False)

def delete(request, id):
    data = employee.object(employee, id=id) 
    data.delete()
    return JsonResponse(data)


def insert(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or do something else
    else:
        form = ModelForm()

    return render(request, 'emp.html', {'form': form})


   


 
