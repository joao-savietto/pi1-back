from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from pi1back.shared.utils import get_current_quarter
from pi1back.occurrences.models import Occurrence

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
            self.quarter = get_current_quarter()
        self.final_grade = self.first_exam + self.second_exam + self.third_exam + self.practice_exam
        super(Grading, self).save(*args, **kwargs)

@receiver(post_save, sender=Grading)
def create_occurrence_for_insufficient_grade(sender, instance, **kwargs):
    # Check if all grades are posted
    if instance.first_exam is not None and instance.second_exam is not None and instance.third_exam is not None and instance.practice_exam is not None:
        if instance.final_grade < 5.0:
            description = f"O aluno não obteve nota suficiente para passar o trimestre na disciplina {instance.subject.name}."
            Occurrence.objects.create(
                created_by=instance.user,
                student=instance.user,
                occurrence_type=Occurrence.NOTA_INSUFICIENTE,
                description=description
            )
