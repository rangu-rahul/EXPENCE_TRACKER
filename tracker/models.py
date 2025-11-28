from django.db import models

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

    def __str__(self):
        return str(self.current_balance)


class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()

    EXPENSE_CHOICES = (
        ('CREDIT', 'CREDIT'),
        ('DEBIT', 'DEBIT'),
    )

    expense_type = models.CharField(
        max_length=10,
        choices=EXPENSE_CHOICES
    )

    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expense_type} - {self.amount}"
