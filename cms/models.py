from django.db import models
from django.contrib.auth.models import User, Group
from model_utils.managers import InheritanceManager
from django.contrib.contenttypes import generic

# Create your models here.
class CmsUser(User):
	title = models.CharField(max_length=200, blank=True)
	objects = InheritanceManager()

	def __unicode__(self):
		return (u'%s %s - %s'%(self.first_name, self.last_name, self.email)).title()

class UserProfile(models.Model):
	bio = models.TextField(blank=True)
	picture = models.URLField(blank=True)
	user = models.OneToOneField(CmsUser, null=False)

class Course(models.Model):
	name = models.CharField(max_length=400, null=False)
	full_name = models.TextField()
	description = models.TextField(blank=True)
	schedule_no = models.CharField(max_length=7, null=False, unique=True)
	start_date = models.DateField(null=False)
	end_date = models.DateField(null=False)
	active = models.BooleanField(null=False, default=False)

	def __unicode__(self):
		return u'#%s %s : %s'%(self.schedule_no, self.name, self.full_name)

class CourseSection(models.Model):
	section_no = models.CharField(max_length=7, null=False, verbose_name='Course Section')
	course = models.ForeignKey(Course, related_name='sections')

	def __unicode__(self):
		return u'%s section %s'%(self.course.name, self.section_no)

	class Meta:
		unique_together = (('section_no', 'course'),)
		# order_with_respect_to = 'course'
		ordering = ['section_no']
		
class Role(models.Model):
	name = models.CharField(max_length=10)

class CourseRoster(models.Model):
	user = models.ForeignKey(CmsUser, related_name='members', primary_key=True)
	section = models.ForeignKey(CourseSection, related_name='courses', primary_key=True)
	role = models.ForeignKey(Role)
	group = models.ForeignKey(Group)

	def _get_course(self):
		return self.section.course

	course = property(_get_course)

	def __unicode__(self):
		return u'%s -> %s -> %s'%(self.user, self.section, self.role, self.group)

class Team(models.Model):
	user = models.ForeignKey(CmsUser, primary_key=True)
	section = models.ForeignKey(CourseSection, related_name='teams', primary_key=True)
	team_no = models.PositiveIntegerField(primary_key=True)

	def _get_course(self):
		return self.section.course

	course = property(_get_course)

	class Meta:
		ordering = ['team_no']

class Document(models.Model):
	author = models.ForeignKey(CmsUser)
	name = models.CharField(max_length=400)
	description = models.TextField(blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	file_path = models.CharField(max_length=400, blank=True, null=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	objects = InheritanceManager()
	# course = models.ForeignKey(Course, related_name='documents')

class Syllabus(Document):
	course = models.OneToOneField(Course, null=False, related_name='syllabus')

	class Meta:
		verbose_name = 'Syllabus'
		verbose_name_plural = 'Syllabuses'

	def __unicode__(self):
		return u'%s -> %s'%(self.course, self.name)

class Lesson(Document):
	course = models.ForeignKey(Course, related_name='lessons')
	week_no = models.PositiveIntegerField()

	class Meta:
		verbose_name = 'Lesson'
		verbose_name_plural = 'Lessons'
		# order_with_respect_to = 'course'
		ordering = ['week_no']

	def __unicode__(self):
		return u'%s -> Week %s'%(self.course, self.week_no)

class Assignment(Document):
	due_date = models.DateTimeField()
	points = models.DecimalField(max_digits=5, decimal_places=0)
	lesson = models.ForeignKey(Lesson, related_name='assignments')

	class Meta:
		verbose_name = 'Assignment'
		verbose_name_plural = 'Assignments'
		ordering = ['due_date']

	def __unicode__(self):
		return u'%s -> %s'%(self.lesson, self.name)

class AssignmentSubmission(Document):
	assignment = models.ForeignKey(Assignment, related_name='submissions')
	user = models.ForeignKey(CmsUser, related_name='submissions', null=True)
	team = models.ForeignKey(Team, related_name='submissions', null=True)
	submitted_date = models.DateTimeField(auto_now_add=True)
	score = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		# order_with_respect_to = 'assignment'
		ordering = ['-submitted_date']
