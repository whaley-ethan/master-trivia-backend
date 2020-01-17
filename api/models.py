from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from users.models import CustomUser

# Create your models here.

class Quiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='quizes')

class Answer(models.Model):
    CATEGORY_CHOICES = [
        ("General Knowledge", "General Knowledge"),
        ("Entertainment: Books", "Entertainment: Books"),
        ("Entertainment: Film", "Entertainment: Film"),
        ("Entertainment: Music", "Entertainment: Music"),
        ("Entertainment: Musicals & Theatres", "Entertainment: Musicals & Theatres"),
        ("Entertainment: Television", "Entertainment: Television"),
        ("Entertainment: Video Games", "Entertainment: Video Games"),
        ("Entertainment: Board Games", "Entertainment: Board Games"),
        ("Science & Nature", "Science & Nature"),
        ("Science: Computers", "Science: Computers"),
        ("Science: Mathematics", "Science: Mathematics"),
        ("Mythology", "Mythology"),
        ("Sports", "Sports"),
        ("Geography", "Geography"),
        ("History", "History"),
        ("Politics", "Politics"),
        ("Art", "Art"),
        ("Celebrities", "Celebrities"),
        ("Animals", "Animals"),
        ("Vehicles", "Vehicles"),
        ("Entertainment: Comics", "Entertainment: Comics"),
        ("Science: Gadgets", "Science: Gadgets"),
        ("Entertainment: Japanese Anime & Manga", "Entertainment: Japanese Anime & Manga"),
        ("Entertainment: Cartoon & Animations", "Entertainment: Cartoon & Animations"),
    ]
    DIFF_CHOICES = [
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='answers')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=255)
    difficulty = models.CharField(choices=DIFF_CHOICES, max_length=6)
    time = models.IntegerField()
    didGetRight = models.BooleanField()

    def __str__(self):
        questionRight = 'wrong'
        if self.didGetRight:
            questionRight = 'right'

        return f'{questionRight} {self.difficulty} {self.category} {self.time}'



@receiver(pre_save, sender=Answer)
def validate_category(sender, instance, **kwargs):
    valid_types = [cat[0] for cat in sender.CATEGORY_CHOICES]
    if instance.category not in valid_types:
        from django.core.exceptions import ValidationError
        raise ValidationError(f'Category "{instance.category}" is not a valid category')

@receiver(pre_save, sender=Answer)
def validate_difficulty(sender, instance, **kwargs):
    valid_types = [diff[0] for diff in sender.DIFF_CHOICES]
    if instance.difficulty not in valid_types:
        from django.core.exceptions import ValidationError
        raise ValidationError(f'Difficulty "{instance.difficulty}" is not a valid difficulty')
