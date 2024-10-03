from django.db.models.signals import post_save
from django.dispatch import receiver
from pi1back.grading.models import Grading
from pi1back.occurrences.models import Occurrence

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
