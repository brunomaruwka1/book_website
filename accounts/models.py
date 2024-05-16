from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=255)
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    first_relase_date = models.DateField()
    literary_genre = models.CharField(max_length=50)
    # cover = models.ImageField(upload_to='sciezka/do/katalogu')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Opinion(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    opinion = models.TextField()
    rating = models.IntegerField()  # możesz dodać pole oceny

    class Meta:
        unique_together = ('customer', 'book')