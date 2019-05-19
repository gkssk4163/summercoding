from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class List(models.Model):
    PRIORITY_CHOICES = ((1, '낮음'), (2,'보통'), (3,'높음'))
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()
    priority = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], choices=PRIORITY_CHOICES)
    created_date = models.DateField(default=timezone.now)
    completed_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    def complete(self):
        self.completed_date = timezone.now()
        self.save()

    def undo_complete(self):
        self.completed_date = None
        self.save()

    def __str__(self):
        return self.title
