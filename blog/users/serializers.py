from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
    
from django.contrib.auth import get_user_model, login, logout, authenticate


from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')

    password = CharField(style={'input_type': 'password'},label='Password')
    password2 = CharField(style={'input_type': 'password'},label='Conform Password')


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            
        ]
        read_only_fields = [
            'password',
            'password2',
        ]
        extra_kwargs = {"password": {"write_only": True}}


    def validate_email(self, value):
        data = self.get_initial()
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        password2= value
        if password != password2:
            raise ValidationError("Confirm Password must match.")
        return value



    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        password = validated_data['password']
        is_staff = 1
        user_obj = User(
                username = username,
                email = email,
                is_staff =is_staff
            )

        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address',required=False, allow_blank=True)
    password = CharField(style={'input_type': 'password'},label='Password')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":{"write_only": True}}
    def validate(self, data):
        user_object=None
        email=data.get("email",None)
        username=data.get("username",None)
        password=data.get("password")
        data['user_object']=[]
        if not email and not username:
            raise ValidationError("Username or Email is must to login")
        user_check=User.objects.filter(
            Q(email=email)|
            Q(username=username)).distinct()

        if user_check.exists() and user_check.count() == 1:
            user_object=user_check.first()
        else:
            raise ValidationError("Username or Email is not Valid")
        if user_object:
            if not user_object.check_password(password):
                raise ValidationError("Incorrect Password")
        return data



class UserLogoutSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            
        ]
