from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'picture', 'theme', 'phone')

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    managers = serializers.SerializerMethodField()
    owners = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = '__all__'

    def get_members(self, obj):
        data = UserSerializer(obj.members, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

    def get_managers(self, obj):
        data = UserSerializer(obj.managers, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

    def get_owners(self, obj):
        data = UserSerializer(obj.owners, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

class InvitationSerializer(serializers.ModelSerializer):
    invitee = serializers.SerializerMethodField()
    inviter = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    class Meta:
        model = Invitation
        fields = '__all__'

    def get_invitee(self, obj):
        data = UserSerializer(obj.invitee).data['username']
        return data

    def get_inviter(self, obj):
        data = UserSerializer(obj.inviter).data['username']
        return data

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data['name']
        return data

class AnnouncementSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    acknowledged = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    
    class Meta:
        model = Announcement
        fields = '__all__'

    def get_creator(self, obj):
        data = UserSerializer(obj.creator).data['username']
        return data

    def get_acknowledged(self, obj):
        data = UserSerializer(obj.acknowledged, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data['name']
        return data

class EventSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    invited = serializers.SerializerMethodField()
    notGoing = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_user(self, obj):
        data = UserSerializer(obj.user).data['username']
        return data

    def get_invited(self, obj):
        data = UserSerializer(obj.invited, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

    def get_notGoing(self, obj):
        data = UserSerializer(obj.notGoing, many=True).data
        lst=[]
        for u in data:
            lst.append(u['username'])
        return lst

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data['name']
        return data


class ScheduleSerializer(serializers.ModelSerializer):
    timeframes = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = '__all__'

    def get_timeframes(self, obj):
        data = TimeFrameSerializer(obj.scheduleTimeFrame.all(), many=True).data
        return data

    def get_user(self, obj):
        data = UserSerializer(obj.user).data['username']
        return data

class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = '__all__'

    def get_user(self, obj):
        data = UserSerializer(obj.user).data['username']
        return data

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data['name']
        return data

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
