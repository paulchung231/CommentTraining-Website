from trainingApp.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    comment_text = serializers.CharField(max_length=5000)
    number_of_ratings = serializers.IntegerField(default=0)
    rating_1 = serializers.IntegerField(default=0)
    rating_2 = serializers.IntegerField(default=0)
    rating_3 = serializers.IntegerField(default=0)
    mean_rating = serializers.DecimalField(default=0,decimal_places=3,max_digits=10)

    class Meta:
        model = Comment
        fields = ('id', 'comment_text', 'number_of_ratings', 'rating_1', 'rating_2', 'rating_3', 'mean_rating')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment_text = validated_data.get('comment_text', instance.comment_text)
        instance.number_of_ratings = validated_data.get('number_of_ratings', instance.number_of_ratings)
        instance.rating_1 = validated_data.get('rating_1', instance.rating_1)
        instance.rating_2 = validated_data.get('rating_2', instance.rating_2)
        instance.rating_3 = validated_data.get('rating_3', instance.rating_3)
        instance.mean_rating = validated_data.get('mean_rating', instance.mean_rating)
        instance.save()
        return instance
