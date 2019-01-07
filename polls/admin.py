from django.contrib import admin

# Register your models here.
from .models import Choice, Question
#admin.site.register(Question) #this is regularly register
#need to put ChoiceInline before Question one so that it can call
class ChoiceInline(admin.TabularInline): # stackedInline
    model = Choice
    extra = 3
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
  # fields=['pub_date','question_text'] # this just field
  #format=fieldsets= [(text_show {"field":[col value], "class": []})]
  fieldsets = [(None, {"fields": ['question_text']}),
            ('Date information',{"fields":['pub_date'],"classes": ['collape']}),
              ]
 #pls note this is classes
  inlines = [ChoiceInline]

  #this the display pages
  list_display = ('question_text', 'pub_date', 'was_published_recently')

  #filter
  list_filter = ['pub_date']

  #search
  search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)







