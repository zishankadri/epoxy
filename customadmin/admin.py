from django.contrib import admin


# Custom Admin Registration.
# from core.models import Service, Category, Contact, Testimonial
from core.models import Contact, GalleryItem

class Table:
    def __init__(self, name, model, fields=None, order_by=None) -> None:
        self.name = name
        self.model = model
        self.fields = fields
        self.order_by = order_by

models = [
    Table(
        name="Contact",
        model=Contact,
        fields=["full_name", "email", "phone"],
        # order_by=["level", "subject"]
    ),
    Table(
        name="GalleryItem",
        model=GalleryItem,
        # fields=["test", "question", "is_public"],
        # order_by=["level", "subject"]
    ),
]