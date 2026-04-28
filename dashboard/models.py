from django.db import models

# 🔥 USER MODEL (matches Streamlit)
class DBUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    budget_limit = models.FloatField(default=0)

    def __str__(self):
        return self.username


# 🔥 EXPENSE MODEL (matches Streamlit)
class DBExpense(models.Model):
    user = models.ForeignKey(DBUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
