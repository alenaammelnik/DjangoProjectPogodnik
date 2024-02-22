from django.http import HttpResponse
from django.shortcuts import render
from .models import City, Temperature
from django.http import JsonResponse
from django.db.models import Avg
import json

def bootstrap_page_handler(request):
    return render(request, 'index.html')

def select_city_view(request):
    cities = City.objects.all()
    
    return render(request, 'index.html', {'cities': cities})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Temperature

def show_temperature_chart(request):
    selected_city_id = request.GET.get('city')
    
    if selected_city_id is not None:
        try:
            temperatures = Temperature.objects.filter(city_id=selected_city_id)
            
            temperature_data = {
                'labels': [],
                'data': []
            }
            
            for temperature in temperatures:
                temperature_data['labels'].append(temperature.date.strftime('%H:%M'))
                temperature_data['data'].append(float(temperature.value))
            
            return JsonResponse(temperature_data)
        
        except Temperature.DoesNotExist:
            return JsonResponse({'error': 'Данные о температуре не найдены'}, status=404)
    
    else:
        return JsonResponse({'error': 'Не передан идентификатор города'}, status=400)
