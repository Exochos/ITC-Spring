from django.contrib import admin
from django.db import models
from .models import Meeting
from .models import Meeting_Minutes
from .models import Resources
from .models import Event


admin.site.register(Meeting)
admin.site.register(Meeting_Minutes)
admin.site.register(Resources)
admin.site.register(Event)
