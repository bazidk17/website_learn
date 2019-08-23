from django.shortcuts import render, redirect
from .forms import topic_add,subtopic_add,topic_remove_from_course,subtopic_remove_from_topic,subtopics_info_edit
from .models import course,topic,subtopics,subtopics_info


# Create your views here.

def route_home(request):
	content={
		'my_courses':course.objects.all()
	}
	return render(request,"learn/home.html",content)

def route_about(request):
	return render(request,"learn/about.html",{"title":"About"})

def route_contact(request):
	return render(request,"learn/contact.html",{"title":"Contact Us"})

def route_course(request,coursename):
	temp_coursename=coursename
	if temp_coursename:
		id_of_course=course.objects.filter(course_name=temp_coursename).first()
		topics_in_that_course=topic.objects.filter(course_id=id_of_course)
		context={
			"coname":temp_coursename,
			"topics_collection":topics_in_that_course,
		}
		return render(request,"learn/course.html",context)
	else:
		return render(request,"learn/course.html")

def route_topic(request,coursename,topicname):
	temp_coursename=coursename
	temp_topicname=topicname
	if temp_coursename and temp_topicname:
		# id_of_course=course.objects.filter(course_name=temp_coursename).first()
		id_of_topic=topic.objects.filter(topic_name=temp_topicname).first()
		subtopics_in_that_topic=subtopics.objects.filter(topic_id=id_of_topic)
		context={
			"coname":temp_coursename,
			"toname":temp_topicname,
			"subtopics_collection":subtopics_in_that_topic,
		}
		return render(request,"learn/topic.html",context)
	else:
		return render(request,"learn/topic.html")

def route_subtopic(request,coursename,topicname,subtopicname):
	temp_coursename=coursename
	temp_topicname=topicname
	temp_subtopicname=subtopicname

	record_of_subtopic=subtopics.objects.filter(subtopics_name=temp_subtopicname).first()
	data_accordingly=None
	if record_of_subtopic:
		data_accordingly=subtopics_info.objects.filter(subtopics_id=record_of_subtopic.pk).first()
	if temp_coursename and temp_subtopicname and temp_topicname:
		context={
			"toname":temp_topicname,
			"coname":temp_coursename,
			"soname":temp_subtopicname,
			"data":data_accordingly
		}
		return render(request,"learn/subtopic.html",context)
	else:
		return render(request,"learn/subtopic.html")
	
def route_add_new(request,toadd,keyname):
	if toadd=="New Topic":
		if request.method=="POST":
			form=topic_add(request.POST)
			if form.is_valid():
				z=topic()
				z.topic_name=form.cleaned_data["topic_name"]
				coursename=keyname
				id_of_course=course.objects.filter(course_name=coursename).first()
				z.course_id=id_of_course
				z.save()
				return redirect('/'+coursename)
		else:
			form=topic_add()
		temp_toknowadd=toadd
		context={
			"thingtobe":temp_toknowadd,
			"form":form,
		}
	elif toadd=="New Subtopic":
		if request.method=="POST":
			form=subtopic_add(request.POST)
			if form.is_valid():
				z=subtopics()
				z.subtopics_name=form.cleaned_data["subtopics_name"]
				topicname=keyname
				instance_of_topic=topic.objects.filter(topic_name=topicname).first()

				##GETTING COURSE DATA FROM TOPIC
		
				coursename=instance_of_topic.course_id.course_name

				z.topic_id=instance_of_topic
				z.save()
				return redirect('/'+coursename+"/"+topicname)
		else:
			form=subtopic_add()
		temp_toknowadd=toadd
		context={
			"thingtobe":temp_toknowadd,
			"form":form,
		}
	return render(request,"learn/add.html",context)

def route_remove(request,toremovefrom,fromby):
	temp_toknowremove=toremovefrom
	if fromby=="course":
		if request.method=="POST":
			form=topic_remove_from_course(request.POST)
			if form.is_valid:
				selected=form["select_topic"].value()
				# print(selected)
				if selected:
					topic.objects.filter(topic_id=selected).first().delete()
					return redirect('/'+temp_toknowremove)
		else:
			id_of_course=course.objects.filter(course_name=temp_toknowremove).first()
			form=topic_remove_from_course(cname=id_of_course)
	elif fromby=="topic":
		if request.method=="POST":
			form=subtopic_remove_from_topic(request.POST)
			if form.is_valid:
				selected=form["select_subtopic"].value()
				# print(selected)
				print(toremovefrom)
				if selected:
					subtopics.objects.filter(subtopics_id=selected).first().delete()
					instance_of_topic=topic.objects.filter(topic_name=toremovefrom).first()
					coursename=instance_of_topic.course_id.course_name
					return redirect('/'+coursename+'/'+toremovefrom)
		else:
			id_of_topic=topic.objects.filter(topic_name=temp_toknowremove).first()
			form=subtopic_remove_from_topic(cname=id_of_topic)

	context={
		"thingtobe":temp_toknowremove,
		"form":form,
	}
	return render(request,"learn/remove.html",context)


def route_edit_subtopic(request,subname):
	temp_whichsubtopic=subname
	id_of_subtopic=subtopics.objects.filter(subtopics_name=temp_whichsubtopic).first()
	topicname=id_of_subtopic.topic_id.topic_name
	id_of_topic=topic.objects.filter(topic_name=topicname).first()
	coursename=id_of_topic.course_id.course_name
	obj=subtopics_info.objects.filter(subtopics_id=id_of_subtopic.pk).first()
	emsg=None
	if request.method=="POST":
		form=subtopics_info_edit(request.POST,request.FILES)
		if form.is_valid():
			
			if obj:
				obj.theory=form.cleaned_data["theory"]
				obj.diagram=form.cleaned_data["diagram"]
				obj.code_py=form.cleaned_data["code_py"]
				obj.code_cpp=form.cleaned_data["code_cpp"]

				obj.save()
			else:
				new_obj=subtopics_info()
				new_obj.subtopics_id=id_of_subtopic
				new_obj.theory=form.cleaned_data["theory"]
				new_obj.diagram=form.cleaned_data["diagram"]
				new_obj.code_py=form.cleaned_data["code_py"]
				new_obj.code_cpp=form.cleaned_data["code_cpp"]

				new_obj.save()
			return redirect("/"+coursename+"/"+topicname+"/"+temp_whichsubtopic)
		else:
			emsg=form.errors
	else:
		if obj:
			form=subtopics_info_edit({"theory":obj.theory,"diagram":obj.diagram,"code_py":obj.code_py,"code_cpp":obj.code_cpp})
		else:
			form=subtopics_info_edit()
	context={
		"thingtobe":temp_whichsubtopic,
		"form":form,
		"form_errors":emsg,
	}
	return render(request,"learn/edit.html",context)
