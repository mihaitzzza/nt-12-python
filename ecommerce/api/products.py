from rest_framework.decorators import api_view
from django.http import JsonResponse


#@api_view(['GET', 'POST'])
def products_view(request):
    if request.method == 'GET':
        return JsonResponse({
            'message': 'Products resource accessed on GET method.'
        }, safe=False)

    if request.method == 'POST':
        return JsonResponse({
            'message': 'Products resource accessed on POST method.'
        }, safe=False)
