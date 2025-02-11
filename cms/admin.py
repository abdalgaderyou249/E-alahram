from django.contrib import admin
from .models import teacher,course,chapter,chapter_content,ChatMessage



# Register your models here.



@admin.register(teacher)
class teacherADMIN(admin.ModelAdmin):
    list_display = ['id','name','email','password']
    search_fields = ('name', 'email') 


@admin.register(course)
class courseADMIN(admin.ModelAdmin):
    list_display = ['id','cname','user','cimg','slug','disp','dateof']




@admin.register(chapter)
class chapterADMIN(admin.ModelAdmin):
    list_display = ['id','title','user','chimg','slug','disp','dateof','course','chfiles','chnumber']


@admin.register(chapter_content)
class chapter_contentADMIN(admin.ModelAdmin):
    list_display = ['id','title','chimg','dispcription','chapter','chfiles']

from django.contrib import admin
from .models import ChatMessage, FAQ

# تسجيل موديل الأسئلة الشائعة
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # عرض السؤال والإجابة في القائمة
    search_fields = ('question',)  # إضافة شريط بحث عن الأسئلة

# تسجيل موديل المحادثات
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'assistant_response', 'timestamp')  # عرض تفاصيل الرسائل
    search_fields = ('user_message', 'assistant_response')  # دعم البحث
    list_filter = ('timestamp',)  # إمكانية التصفية حسب التاريخ






