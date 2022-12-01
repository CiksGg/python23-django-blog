from rest_framework.serializers import ModelSerializer
from .models import Post
from reviews.serializers import CommentSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["author"] = instance.author.username
        comments = instance.comments.all()
        rep['comments'] = CommentSerializer(comments, many=True).data
        return rep