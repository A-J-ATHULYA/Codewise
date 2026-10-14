from django.db import models

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=100)
    
    LANGUAGE_CHOICES = (
        ("python", "python"),
        ("java", "java"),
        ("javascript", "javascript"),
        ("C", "C"),
    )
    language = models.CharField(max_length=200, choices=LANGUAGE_CHOICES, default="python")
    
    DIFFICULTY_LEVEL = (
            ("hard", "hard"),
            ("medium", "medium"),
            ("easy", "easy")
        )
    difficulty_level = models.CharField(max_length=200, choices=DIFFICULTY_LEVEL, default="easy")
    
    notes = models.TextField(null=True)
    
    topic = models.CharField(max_length=200)
    
    published_year = models.DateTimeField(auto_now_add=True)

    sample_output = models.TextField()
    
    is_active = models.BooleanField(default=True)
