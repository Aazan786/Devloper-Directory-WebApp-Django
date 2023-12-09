from rest_framework import serializers
from projects.models import Project, Review, Tag
from users.models import Profile


class ReviewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class TagSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProjectSerilizer(serializers.ModelSerializer):
    owner = ProfileSerilizer(many=False)
    tags = TagSerilizer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serilizer = ReviewSerilizer(reviews, many=True)
        return serilizer.data
