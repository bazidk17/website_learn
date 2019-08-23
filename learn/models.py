from django.db import models

# Create your models here.
class course(models.Model):
	course_id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=30)
	course_picture=models.ImageField(upload_to="courses/imag/",blank=False,null=False)

	def __str__(self):
		return self.course_name

class topic(models.Model):
	topic_id=models.AutoField(primary_key=True)
	topic_name=models.CharField(max_length=30)
	course_id=models.ForeignKey(course,on_delete=models.CASCADE)

	def __str__(self):
		return self.topic_name

class subtopics(models.Model):
	subtopics_id=models.AutoField(primary_key=True)
	subtopics_name=models.CharField(max_length=30)
	topic_id=models.ForeignKey(topic,on_delete=models.CASCADE)

	def __str__(self):
		return self.subtopics_name

class subtopics_info(models.Model):
	subtopics_id=models.ForeignKey(subtopics,on_delete=models.CASCADE)
	theory=models.TextField(default=None,blank=True)
	diagram=models.ImageField(upload_to="diagram_representation/imag/",blank=True,default=None)
	code_py=models.TextField(default=None,blank=True)
	code_cpp=models.TextField(default=None,blank=True)

