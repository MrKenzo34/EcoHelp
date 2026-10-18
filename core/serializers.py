from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Announcement, Claim

User = get_user_model()

# 1. Ro'yxatdan o'tish Serializeri
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', ''),
            role=validated_data.get('role', 'donor')
        )
        return user


# 2. Kategoriya Serializeri
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# 3. E'lon Serializeri
class AnnouncementSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ('author', 'created_at')


# 4. Band qilish (Claim) Serializeri
class ClaimSerializer(serializers.ModelSerializer):
    applicant_username = serializers.ReadOnlyField(source='applicant.username')

    class Meta:
        model = Claim
        fields = '__all__'
        read_only_fields = ('applicant', 'created_at', 'status')