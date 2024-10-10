from django.db.models import Model, CharField, TextField, ImageField, ForeignKey, CASCADE, ManyToManyField


class BookCategory(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = "book_category"
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"

    def __str__(self):
        return self.name


class BookGenre(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = "book_genre"
        verbose_name = "Book Genre"
        verbose_name_plural = "Book Genres"

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=255)
    summary = TextField()
    cover = ImageField(upload_to="books")
    category = ForeignKey("BookCategory", CASCADE)
    genres = ManyToManyField("BookGenre")

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
