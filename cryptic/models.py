from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.CharField(max_length=200)
    img_url = models.URLField(blank=True, null=True)
    points = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    category = models.CharField(max_length=200, default="General")

    def __str__(self):
        return self.question_text
    
class Additional_Hints(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=200)

    def __str__(self):
        return self.hint_text
