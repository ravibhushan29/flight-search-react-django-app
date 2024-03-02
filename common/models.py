from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        help_text="Unique identifier for the record, using UUID4.",
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="The datetime record was created. "
        "Automatically set to the current datetime when the record is first created.",
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text="The datetime the record was last updated. "
        "Automatically updated to the current datetime each time the record is saved.",
    )

    class Meta:
        abstract = True
