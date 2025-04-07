from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

# Key for encryption/decryption (use a secure method to store this)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()

    def set_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode())

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password).decode()

    def __str__(self):
        return self.app_name
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

# Key for encryption/decryption (use a secure method to store this)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()

    def set_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode())

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password).decode()

    def __str__(self):
        return self.app_name
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

# Key for encryption/decryption (use a secure method to store this)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()

    def set_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode())

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password).decode()

    def __str__(self):
        return self.app_name
