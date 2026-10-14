from rest_framework import serializers
from Repository.models import Questions


class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(choices=Questions.LANGUAGE_CHOICES, default="python")
    difficulty_level = serializers.ChoiceField(choices=Questions.DIFFICULTY_LEVEL, default="easy")
    notes = serializers.CharField()
    topic = serializers.CharField()
    published_year = serializers.DateTimeField(read_only=True)
    sample_output = serializers.CharField()
    is_active = serializers.BooleanField()
    