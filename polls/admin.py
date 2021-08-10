from django.contrib import admin

from polls.models.poll import Poll
from polls.models.question import Question

admin.site.register(Poll)
admin.site.register(Question)
