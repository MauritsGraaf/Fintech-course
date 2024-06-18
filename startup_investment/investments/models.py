from django.db import models
from django.contrib.auth.models import User
import random


def calculate_date() -> int:
    last_investment = Investment.objects.order_by('-date_invested').first()
    if last_investment:
        return last_investment.date_invested + 1


def random_growth_rate() -> float:
    return random.random()  # [0, 1)


def random_interest() -> float:
    return random.random() * 0.1  # [0, 0.1)


class Startup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    industry = models.TextField()
    growth_rate = models.DecimalField(max_digits=4, decimal_places=2, default=random_growth_rate)
    interest = models.DecimalField(max_digits=4, decimal_places=2, default=random_interest)

    def funding_required(self):
        return max(self.target_amount - self.total_funding_raised(), 0)

    def total_funding_raised(self):
        # Calculate the total funding raised for this startup
        total_funding = self.investment_set.aggregate(total=models.Sum('amount'))['total']
        return total_funding or 0  # Return 0 if there are no investments

    def mean_funding_last_7_funds(self):
        # Calculate the mean funding raised by the last 7 investments
        last_7_investments = self.investment_set.order_by('-date_invested')[:7]
        total_funding = sum([investment.amount for investment in last_7_investments])
        return total_funding / len(last_7_investments) if last_7_investments else 1

    def add_investments(self, date: int):
        try:
            new_amount = self.mean_funding_last_7_funds() * self.growth_rate
            investment = Investment.objects.create(
                user=User.objects.first(),
                startup=self,
                amount=new_amount,
                date_invested=date
            )
            investment.save()
        except BaseException:
            new_amount = random.randint(100, 10000)
            investment = Investment.objects.create(
                user=User.objects.first(),
                startup=self,
                amount=new_amount,
                date_invested=date
            )
            investment.save()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.IntegerField(default=calculate_date)

    def calculate_profits(self):
        date = calculate_date()
        if date < self.date_invested:
            return 0
        days_passed = date - self.date_invested
        return self.amount * self.startup.interest * days_passed / 365
