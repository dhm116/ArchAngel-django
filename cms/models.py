from django.db import models
from django.contrib.auth.models import User, Group
from model_utils.managers import InheritanceManager
from django.contrib.contenttypes import generic

# Create your models here.
class CmsUser(User):
	title = models.CharField(max_length=200, blank=True)
	objects = InheritanceManager()

class UserProfile(models.Model):
	bio = models.TextField(blank=True)
	picture = models.URLField(blank=True)
	user = models.OneToOneField(CmsUser, null=False)

class Course(models.Model):
	name = models.CharField(max_length=400, null=False)
	full_name = models.TextField()
	description = models.TextField()
	schedule_no = models.CharField(max_length=7, null=False, unique=True)
	start_date = models.DateField(null=False)
	end_date = models.DateField(null=False)

class CourseSection(models.Model):
	section_no = models.CharField(max_length=7, default='001', null=False)
	course = models.ForeignKey(Course, related_name='sections')

	class Meta:
		unique_together = (('section_no', 'course'),)

class CourseRoster(models.Model):
	user = models.ForeignKey(CmsUser)
	section = models.ForeignKey(CourseSection, related_name='members')
	group = models.ForeignKey(Group)

	class Meta:
		unique_together = (('user', 'section'),)

	def _get_course(self):
		return self.section.course

	course = property(_get_course)

class Team(models.Model):
	user = models.ForeignKey(CmsUser)
	section = models.ForeignKey(CourseSection, related_name='teams')
	team_no = models.PositiveIntegerField()

	def _get_course(self):
		return self.section.course

	course = property(_get_course)

	class Meta:
		unique_together = (('user', 'section', 'team_no'),)

class Document(models.Model):
	author = models.ForeignKey(CmsUser)
	name = models.CharField(max_length=400)
	description = models.TextField()
	content = models.TextField()
	file_path = models.CharField(max_length=400)
	creation_date = models.DateTimeField(auto_now_add=True)
	objects = InheritanceManager()
	# course = models.ForeignKey(Course, related_name='documents')

class Syllabus(Document):
	course = models.ForeignKey(Course, related_name='syllabus')

	class Meta:
		verbose_name = 'Syllabus'
		verbose_name_plural = 'Syllabuses'

class Lesson(Document):
	course = models.ForeignKey(Course, related_name='lessons')
	week_no = models.PositiveIntegerField()

	class Meta:
		verbose_name = 'Lesson'
		verbose_name_plural = 'Lessons'

class Assignment(Document):
	due_date = models.DateTimeField()
	points = models.DecimalField(max_digits=5, decimal_places=2)
	lesson = models.ForeignKey(Lesson, related_name='assignments')

	class Meta:
		verbose_name = 'Assignment'
		verbose_name_plural = 'Assignments'

class AssignmentSubmission(Document):
	assignment = models.ForeignKey(Assignment, related_name='submissions')
	team = models.ForeignKey(Team, related_name='submissions', null=True)
	submitted_date = models.DateTimeField(auto_now_add=True)
