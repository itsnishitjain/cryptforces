from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.CharField(max_length=200)
    img_url = models.URLField(blank=True, null=True)
    points = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=200, default="Easy", choices=(("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")))
    category = models.CharField(max_length=200, default="General")
    tags = models.ManyToManyField(Tag, blank=True)
    from_event = models.BooleanField(default=False)
    event_name = models.CharField(max_length=200, blank=True, null=True)
    event_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.question_text
    
class Additional_Hints(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=200)

    def __str__(self):
        return self.hint_text


class logs(models.Model):
    user = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    attempt = models.CharField(max_length=200)
    

    def __str__(self):
        return self.user