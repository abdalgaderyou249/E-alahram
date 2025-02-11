from django.db import models
from autoslug import AutoSlugField

# نموذج المعلم
class teacher(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# نموذج الدورة
class course(models.Model):
    cname = models.CharField(max_length=400)
    user = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name='courses')
    slug = AutoSlugField(populate_from='cname', max_length=250, unique=True, null=True, default=None)
    disp = models.TextField(blank=True, null=True)  
    dateof = models.DateTimeField(auto_now_add=True)
    cimg = models.FileField(upload_to='coursevideos/', null=True, blank=True)

    def __str__(self):
        return self.cname

# نموذج الفصول
class chapter(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='chapters')
    user = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name='chapters_created')
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    disp = models.TextField(blank=True, null=True)
    chimg = models.ImageField(upload_to='chaptersimg/', null=True, blank=True)
    chfiles = models.FileField(upload_to='chfiles/', null=True, blank=True)
    chnumber = models.IntegerField()
    dateof = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.cname} - {self.title}"

    class Meta:
        verbose_name_plural = "Chapters"

# نموذج محتوى الفصل
class chapter_content(models.Model):
    title = models.CharField(max_length=250)
    chapter = models.ForeignKey(chapter, on_delete=models.CASCADE, related_name='contents')
    dispcription = models.TextField(blank=True, null=True)
    chimg = models.ImageField(upload_to='chaptersimg/', blank=True, null=True)
    chfiles = models.FileField(upload_to='chfiles/', blank=True, null=True)

    def __str__(self):
        return self.title

############
from django.db import models

class ChatMessage(models.Model):
    user_message = models.CharField(max_length=255)  # رسالة المستخدم
    assistant_response = models.TextField()  # رد المساعد
    timestamp = models.DateTimeField(auto_now_add=True)  # توقيت الرسالة
    is_predefined = models.BooleanField(default=False)  # هل هذه إجابة محفوظة مسبقًا؟

    def __str__(self):
        return f"User: {self.user_message} | Predefined: {self.is_predefined}"
    
    #######
class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)  # السؤال
    answer = models.TextField()  # الإجابة
    

    def __str__(self):
        return self.question
