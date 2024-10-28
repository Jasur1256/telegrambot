from django.db import models

class Foydalanuvchi(models.Model):
    username = models.CharField(max_length=100, unique=True)  # Telegram username
    chat_id = models.BigIntegerField(unique=True)              # Telegram chat ID
    created_at = models.DateTimeField(auto_now_add=True)       # Yaratilgan sana

    def __str__(self):
        return self.username

class Sorov(models.Model):
    foydalanuvchi = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE)  # Foydalanuvchi bilan bog'lanish
    text = models.TextField()  # Foydalanuvchidan kelgan so'rov matni
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana

    def __str__(self):
        return f"{self.foydalanuvchi.username}: {self.text[:20]}..."  # So'rov matnining birinchi 20 belgisi


