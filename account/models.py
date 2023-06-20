from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

Status = ((0, "Draft"),(1,"Published"))







