from django.db import models

class PDFUpload(models.Model):
    semester = models.IntegerField()
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.pdf_file.name