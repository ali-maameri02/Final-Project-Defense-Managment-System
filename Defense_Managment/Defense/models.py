from django.db import models
from Account.models import *

class DefenseSchedule(models.Model):  # Fixed name from `DefeneSchedule`
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"Defense on {self.date} at {self.location}"


class Jury(models.Model):
    defense_session = models.ForeignKey(DefenseSchedule, on_delete=models.CASCADE)
    juries = models.ManyToManyField(Professor)

    def __str__(self):
        return f"Jury for Defense {self.defense_session.id}"


class Evaluation(models.Model):
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.FloatField()

    def save(self, *args, **kwargs):
        if not (0.0 <= self.grade <= 20.0):  # Ensure grade is within a valid range
            raise ValueError("Grade must be between 0.0 and 20.0")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Evaluation for {self.student.user.username}: {self.grade}"