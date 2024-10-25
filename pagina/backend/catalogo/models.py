from django.db import models

class Boletines(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title