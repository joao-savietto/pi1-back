from django.db import models
import datetime
from pi1back.shared.utils import get_current_quarter

class Grading(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    first_exam = models.FloatField(default=0.0)
    second_exam = models.FloatField(default=0.0)
    third_exam = models.FloatField(default=0.0)
    practice_exam = models.FloatField(default=0.0)
    final_grade = models.FloatField(blank=True, null=True)
    year = models.IntegerField(null=True, default=None)
    quarter = models.IntegerField(null=True, default=None)

    def save(self, *args, **kwargs):
        if self.year is None:
            self.year = datetime.date.today().year
        if self.quarter is None:
            current_quarter = get_current_quarter()
        super(Grading, self).save(*args, **kwargs)