from django.test import TestCase
from django.urls import reverse
from .models import City, Temperature

class CityModelTests(TestCase):

    def test_city_creation(self):
        # Проверка создания объекта City
        city_name = "Test City"
        city = City.objects.create(name=city_name)
        self.assertEqual(city.name, city_name)

class TemperatureModelTests(TestCase):

    def setUp(self):
        # Создание тестового города
        self.city = City.objects.create(name="Test City")

    def test_temperature_creation(self):
        # Проверка создания объекта Temperature
        temperature_value = 25
        temperature = Temperature.objects.create(city=self.city, value=temperature_value)
        self.assertEqual(temperature.city, self.city)
        self.assertEqual(temperature.value, temperature_value)

class WeatherAppViewsTests(TestCase):

    def setUp(self):
        # Создание тестового города и температуры
        self.city = City.objects.create(name="Test City")
        Temperature.objects.create(city=self.city, value=25)

    def test_temperature_chart_view(self):
        # Проверка доступности страницы с графиком температур
        response = self.client.get(reverse('temperature-chart'), {'city': self.city.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Температура в выбранном городе")

    def test_temperature_chart_data(self):
        # Проверка данных JSON, возвращаемых представлением
        response = self.client.get(reverse('temperature-chart'), {'city': self.city.id})
        data = response.json()
        self.assertIn('labels', data)
        self.assertIn('data', data)
        self.assertEqual(len(data['labels']), 1)
        self.assertEqual(len(data['data']), 1)
