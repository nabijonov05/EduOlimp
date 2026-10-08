from django.db import models
from django.contrib.auth.models import User



class TestMaterial(models.Model):
    subject = models.ForeignKey('olympiads.Subject', on_delete=models.CASCADE)
    grade = models.IntegerField()
    file = models.FileField(upload_to='tests/')

    def __str__(self):
        return f"{self.subject} - {self.grade}-sinf"


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
    test_material = models.ForeignKey(TestMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    
    correct_count = models.IntegerField()
    total_questions = models.IntegerField()
    score_percent = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)

    user_answers = models.JSONField(null=True, blank=True)
    questions_order = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.score_percent}%"