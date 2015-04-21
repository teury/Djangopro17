from django.shortcuts import render
from .models import Event, Category

def index(request):
	events = Event.objects.all().order_by('-created')[:6]
	categories = Category.objects.all()

	return render(request,  'events/index.html', {'events':events, 'categories':categories})
def main_panel(request):
	events = Event.objects.filter(organizer_username = "victorvillazon").order_by('is_free', '-create')
	
	cantidad_eventos = events.count()
	return render(request, 'events/panel/panel.html', {'events': events, 'cantidad':cantidad_eventos})