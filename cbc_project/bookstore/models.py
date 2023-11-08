from django.db import models
from django.utils import timezone
from jsonfield import JSONField

class Book(models.Model):
    # Fields for the Book model
    name = models.CharField(max_length=255)
    authors = JSONField()
    year_published = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Automatically set to current timestamp when created
    date_modified = models.DateTimeField(auto_now=True)      # Automatically updated to current timestamp when modified

    def __str__(self):
        """
        Returns a string representation of the Book model.
        """
        try:
            first_author = self.authors[0]
            first_name = first_author.get('first_name', '')
            last_name = first_author.get('last_name', '')
        except (IndexError, KeyError):
            first_name = ''
            last_name = ''

        return f"{self.name} by {first_name} {last_name} - {self.year_published}"

class Review(models.Model):
    # Fields for the Review model
    my_review = models.TextField()
    stars = models.IntegerField()
    unfinished = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)  # Automatically set to current timestamp when created
    date_modified = models.DateTimeField(auto_now=True)      # Automatically updated to current timestamp when modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # ForeignKey linking to the Book model

    def __str__(self):
        """
        Returns a string representation of the Review model.
        """
        return f"Review for '{self.book.name}' - {self.stars} stars"

    class Meta:
        """
        Meta class for the Review model to define additional options.
        """
        ordering = ['-date_added']  # Order reviews by date_added in descending order


