from django.contrib import admin
from .models import Question, Rates
from .models import Tag
from .models import Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Rates)
class QuestionAdmin(admin.ModelAdmin):
    pass
