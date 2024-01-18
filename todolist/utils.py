from .models import Todo
from .weather_utils import is_valid_city

def handle_post_request(request):
    if 'title' in request.POST:
        title = request.POST['title'].strip()
        if title and not Todo.objects.filter(title=title).exists():
            Todo.create_todo(title)

    if 'city_name' in request.POST and request.POST['city_name']:
        return is_valid_city(request)
