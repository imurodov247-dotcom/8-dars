from django.db import models

# Create your models here.
class Expense(models.Model):
    description = models.TextField()
    amount = models.FloatField()
    category = models.CharField(choices=[
        ('food','Food'),
        ('transport','Transport'),
        ('shopping','Shopping'),
        ('entertaining','Entertaining'),
        ('bills','Bills'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[
        ('yangi','Yangi'),
        ('eski','Eski')
        ],default="yangi")
    
    def __str__(self):
        return self.description
    
    
    
    
    