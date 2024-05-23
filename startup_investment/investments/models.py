from django.db import models
from django.contrib.auth.models import User

class Startup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    industry = models.TextField()

    def total_funding_raised(self):
        # Calculate the total funding raised for this startup
        total_funding = self.investment_set.aggregate(total=models.Sum('amount'))['total']
        return total_funding or 0  # Return 0 if there are no investments

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateTimeField(auto_now_add=True)
    profits = models.DecimalField(max_digits=12, decimal_places=2, default=0)
