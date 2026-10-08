from django.db import models

# apps/analytics/models.py
from django.db import models
from apps.common.models import TimeStampedModel


class OlympiadResult(TimeStampedModel):
    test_result = models.OneToOneField(
        'assessments.TestResult', 
        on_delete=models.CASCADE, 
        related_name='final_olympiad_result'
    )
    rank = models.PositiveIntegerField(null=True, blank=True, help_text="Olimpiadadagi egallagan o'rni")
    is_disqualified = models.BooleanField(default=False, help_text="Proctoring xulosasiga ko'ra diskvalifikatsiya qilinganmi?")
    disqualification_reason = models.TextField(null=True, blank=True)
    
    certificate_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"Natija: {self.test_result.user.get_full_name()} - O'rin: {self.rank or 'N/A'}"


class SubjectAnalytics(TimeStampedModel):
    
    subject = models.ForeignKey('olympiads.Subject', on_delete=models.CASCADE)
    total_participants = models.PositiveIntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    highest_score = models.FloatField(default=0.0)
    flagged_attempts_count = models.PositiveIntegerField(default=0, help_text="Shubhali urinishlar soni")

    def __str__(self):
        return f"Statistika: {self.subject.name} ({self.created_at.strftime('%Y-%m')})"
