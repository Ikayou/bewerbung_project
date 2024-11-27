from django.db import models

class Bewerbung(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    company = models.CharField(max_length=100, verbose_name="Unternehmen")
    position = models.CharField(max_length=100, verbose_name="Position")
    date_applied = models.DateField(verbose_name="Bewerbungsdatum")
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Ausstehend"),
            ("Interview", "Interview"),
            ("Accepted", "Angenommen"),
            ("Rejected", "Abgelehnt"),
        ],
        default="Pending",
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.name} - {self.company} ({self.position})"
