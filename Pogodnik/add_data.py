# import os 
# import django 
# import random
# from datetime import datetime, timedelta 

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pogodnik.settings')
# django.setup()

# from FindOutTheWeather.models import City, Temperature

# def add_data():
#     city_names = ['Мурманск', 'Санкт-Петербург', 'Москва', 'Казань', 'Новороссийск']
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=1)

#     for name in city_names: 
#         city = City.objects.create (name=name)

#         for i in range(24):
#             temperature_value = round(random.uniform(-20, 30), 2)
#             random_time = start_date + timedelta(hours = i)
#             Temperature.objects.create(city=city, date = random_time, value = temperature_value)

# if __name__ == '__main__':
#     add_data()


# import os 
# import django 
# import random
# from datetime import datetime, timedelta 

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pogodnik.settings')
# django.setup()

# from FindOutTheWeather.models import City, Temperature

# def add_data():
#     city_data = {
#         'Мурманск': {'min_temp': -20, 'max_temp': -10},
#         'Санкт-Петербург': {'min_temp': -5, 'max_temp': 2},
#         'Москва': {'min_temp': -1, 'max_temp': 7},
#         'Казань': {'min_temp': 1, 'max_temp': 10},
#         'Новороссийск': {'min_temp': 10, 'max_temp': 17}
#     }

#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=1)

#     for city_name, temp_range in city_data.items(): 
#         city = City.objects.create(name=city_name)

#         for i in range(24):
#             temperature_value = round(random.uniform(temp_range['min_temp'], temp_range['max_temp']), 2)
#             random_time = start_date + timedelta(hours=i)
#             Temperature.objects.create(city=city, date=random_time, value=temperature_value)

# if __name__ == '__main__':
#     add_data()

