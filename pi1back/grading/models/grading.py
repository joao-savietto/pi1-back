from django.db import models

class Grading(models.Model):
    subject = models.ForeignKey('grading.Subject', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    first_exam = models.FloatField(default=0.0)
    second_exam = models.FloatField(default=0.0)
    third_exam = models.FloatField(default=0.0)
    practice_exam = models.FloatField(default=0.0)
    final_grade = models.FloatField(default=0.0, blank=True, null=True)