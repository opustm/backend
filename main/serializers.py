from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Event, Request, ToDo, Invitation, User, Clique, Schedule, TimeFrame, Announcement, DirectMessage, CliqueMessage, Reaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CliqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clique
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    timeframes = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    cliques = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = '__all__'

    def get_timeframes(self, obj):
        data = TimeFrameSerializer(obj.scheduleTimeFrame.all(), many=True).data
        return data

    def get_user(self, obj):
        data = UserSerializer(obj.user).data
        return data

    def get_cliques(self, obj):
        data = CliqueSerializer(obj.cliques.all(), many=True).data
        return data

class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame
        fields = '__all__'

class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = '__all__'

class CliqueMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CliqueMessage
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email', 'phone', 'picture', 'theme')
