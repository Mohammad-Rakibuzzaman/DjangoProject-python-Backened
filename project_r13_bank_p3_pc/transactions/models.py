from django.db import models
from accounts.models import UserBankAccount
# Create your models here.
from .constants import TRANSACTION_TYPE

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE) # ekjon user er multiple transactions hote pare
    
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    # is_bankrupt = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['timestamp'] 



class TransferTransaction(models.Model):
    sender = models.ForeignKey(UserBankAccount, related_name = 'transfers_sent', on_delete = models.CASCADE)
    receiver = models.ForeignKey(UserBankAccount, related_name = 'transfers_received', on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits= 12)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.amount}"
    






