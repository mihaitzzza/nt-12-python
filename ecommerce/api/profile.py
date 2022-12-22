from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    # request.user.profile
    profile_serializer = ProfileSerializer(request.user.profile)

    # return JsonResponse({'message': f'Profile access on {request.method} method. (User: {request.user} | is_authenticated={request.user.is_authenticated})'}, safe=False)
    return Response(data=profile_serializer.data, status=200)
