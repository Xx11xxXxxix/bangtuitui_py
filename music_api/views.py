import requests
from django.http import JsonResponse


def get_top_songs(request):
    artist_id = request.GET.get('id')
    if not artist_id:
        return JsonResponse({'error': 'Missing artist ID'}, status=400)

    try:
        response = requests.get(f'http://localhost:3020/artist/top/song?id={artist_id}')
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)