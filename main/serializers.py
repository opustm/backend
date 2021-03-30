from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import *
from collections import OrderedDict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "bio",
            "picture",
            "theme",
            "phone",
        )


class UserField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(UserField, self).to_representation(value)
        try:
            item = User.objects.get(pk=pk)
            serializer = UserSerializer(item)
            return serializer.data
        except User.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])


class TeamSerializer(serializers.ModelSerializer):
    members = UserField(queryset=User.objects.all(), many=True)
    managers = UserField(queryset=User.objects.all(), many=True)
    owners = UserField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Team
        fields = "__all__"


class TeamField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(TeamField, self).to_representation(value)
        try:
            item = Team.objects.get(pk=pk)
            serializer = TeamSerializer(item)
            return serializer.data
        except Team.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}
        return OrderedDict([(item.id, str(item)) for item in queryset])


class InvitationSerializer(serializers.ModelSerializer):
    invitee = serializers.SerializerMethodField()
    inviter = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Invitation
        fields = "__all__"

    def get_invitee(self, obj):
        data = UserSerializer(obj.invitee).data
        return data

    def get_inviter(self, obj):
        data = UserSerializer(obj.inviter).data
        return data

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data
        return data


class AnnouncementSerializer(serializers.ModelSerializer):
    team = TeamField(queryset=Team.objects.all())
    creator = UserField(queryset=User.objects.all())

    class Meta:
        model = Announcement
        fields = "__all__"

    def get_acknowledged(self, obj):
        data = UserSerializer(obj.acknowledged, many=True).data
        lst = []
        for u in data:
            lst.append(u)
        return lst


class EventSerializer(serializers.ModelSerializer):
    user = UserField(queryset=User.objects.all(), allow_null=True)
    team = TeamField(queryset=Team.objects.all(), allow_null=True)

    class Meta:
        model = Event
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    timeframes = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = "__all__"

    def get_timeframes(self, obj):
        data = TimeFrameSerializer(obj.scheduleTimeFrame.all(), many=True).data
        return data

    def get_user(self, obj):
        data = UserSerializer(obj.user).data
        return data


class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    user = UserField(queryset=User.objects.all(), allow_null=True)
    team = TeamField(queryset=Team.objects.all(), allow_null=True)

    class Meta:
        model = Request
        fields = "__all__"

    def get_user(self, obj):
        data = UserSerializer(obj.user).data
        return data

    def get_team(self, obj):
        data = TeamSerializer(obj.team).data
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
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            "token",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "picture",
            "theme",
        )
