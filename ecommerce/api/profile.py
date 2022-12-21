from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, serializers
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'last_name')

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    @staticmethod
    def get_first_name(obj):
        return obj.user.first_name

    @staticmethod
    def get_last_name(obj):
        return obj.user.last_name


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def profile_view(request):
    if request.method == 'GET':
        profile = ProfileSerializer(request.user.profile)
    else:
        profile = ProfileSerializer(request.user.profile, data={'avatar': request.FILES.get('avatar')})
        if profile.is_valid():
            profile.save()

    return Response(profile.data)
