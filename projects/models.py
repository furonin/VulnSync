from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Represents a specific penetration testing engagement.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.client_name}"

class Vulnerability(models.Model):
    """
    Represents a technical finding identified during the scan.
    """
    SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Info', 'Info'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='vulnerabilities')
    title = models.CharField(max_length=255)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='Low')
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, blank=True, null=True)
    cve_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="CVE ID")
    description = models.TextField()
    remediation = models.TextField()
    detected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vulnerabilities"

    def __str__(self):
        return f"[{self.severity}] {self.title}"