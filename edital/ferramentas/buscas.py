from ..models import Edital

def get_edital(request):
    try:
        return Edital.objects.get(id=request.GET.get('id'))
    except Exception as e:
        return None