from django.forms import ModelForm
from  django.db import models
# Create your models here.

class Subject(models.Model):
    subject_id = models.CharField(max_length=7,primary_key=True)
    subject_name = models.TextField()
    subject_description = models.TextField()
    def __str__(self):
        return self.subject_id+" "+self.subject_name

class Material(models.Model):
    subject = models.ForeignKey('Subject',on_delete=models.SET_NULL, null=True)
    material_name = models.TextField()
    upload_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return self.subject.subject_id +" "+self.material_name

PROVINCE_LIST = [ 
    ('Songkhla', 'สงขลา'), 
    ('Yala', 'ยะลา'),
    ('Pattani', 'ปัตตานี'),
    ('Satul', 'สตูล')]

class Survey(models.Model):
    age = models.PositiveSmallIntegerField(verbose_name="อายุผู้กรอกแบบสอบถาม")
    province = models.CharField(max_length=100, choices=PROVINCE_LIST, verbose_name="คุณอยู่จังหวัด")
    opinion = models.TextField(verbose_name="ความเห็นต่อเว็บไซต์")
    def __str__(self):
        return self.opinion


from django.forms import ModelForm
class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['age', 'province', 'opinion'
        ]
 