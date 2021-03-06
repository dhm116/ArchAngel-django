from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
import models

class ProfileInline(admin.StackedInline):
	model = models.UserProfile
	can_delete = False
	verbose_name_plural = 'profile'

class GroupInline(admin.TabularInline):
	model = Group

class DocumentInline(admin.TabularInline):
	model = models.Document
	extra = 1

class CourseInline(admin.TabularInline):
	model = models.Course

class CourseSectionInline(admin.TabularInline):
	model = models.CourseSection
	extra = 1
	# fk_name = 'course'

class CourseRosterInline(admin.TabularInline):
	model = models.CourseRoster
	extra = 1
	# fk_name = 'section'

class TeamInline(admin.TabularInline):
	model = models.Team
	extra = 1
	# fk_name = 'section'

class LessonInline(admin.TabularInline):
	model = models.Lesson
	extra = 1

class AssignmentInline(admin.TabularInline):
	model = models.Assignment
	fk_name = 'lesson'
	extra = 1

class SyllabusInline(admin.TabularInline):
	model = models.Syllabus
	max_num = 1

class TeamMemberInline(admin.TabularInline):
	model = models.TeamMember
	extra = 1

class UserAdmin(UserAdmin):
	inlines = (ProfileInline, )

class CourseAdmin(admin.ModelAdmin):
	model = models.Course
	list_display = ('name', 'full_name', 'schedule_no')

	inlines = [
		LessonInline,
		SyllabusInline,
		CourseSectionInline,
	]

class CourseSectionAdmin(admin.ModelAdmin):
	model = models.CourseSection
	list_display = ('course', 'section_no')
	list_filter = ('course__name',)

class CourseRosterAdmin(admin.ModelAdmin):
	model = models.CourseRoster
	list_display = ('user', 'section', 'group')
	list_editable = ('section', 'group')
	list_filter = ('section', 'section__course__name', 'group', 'user')

	# inlines = [
	# 	CmsUser,
	# 	GroupInline,
	# 	CourseSectionInline,
	# ]

class TeamAdmin(admin.ModelAdmin):
	model = models.Team
	list_display = ('section', 'team_no', 'name', 'start_date', 'end_date')
	list_filter = ('section', 'section__course__name')

	inlines = [
		TeamMemberInline,
	]

class TeamMemberAdmin(admin.ModelAdmin):
	model = models.TeamMember
	list_display = ('user', 'team')

class SyllabusAdmin(admin.ModelAdmin):
	model = models.Syllabus
	list_display = ('course', 'name', 'description','file_path', 'creation_date')
	list_filter = ('course__name', 'author')

class LessonAdmin(admin.ModelAdmin):
	model = models.Lesson
	list_display = ('course', 'name', 'description', 'week_no','file_path', 'creation_date')
	list_filter = ('course__name', 'author')

	inlines = [
		AssignmentInline,
	]

class AssignmentAdmin(admin.ModelAdmin):
	model = models.Assignment
	list_display = ('lesson', 'name', 'points', 'due_date')
	list_editable = ('points', 'due_date')
	list_filter = ('lesson__course__name', 'author')

class SubmissionAdmin(admin.ModelAdmin):
	model = models.AssignmentSubmission
	list_display = ('assignment', 'author', 'team', 'submitted_date')
	list_filter = ('assignment', 'author', 'submitted_date')

class GradedSubmissionAdmin(admin.ModelAdmin):
	model = models.GradedAssignmentSubmission
	list_display = ('author', 'submission', 'score')
	list_editable = ('score',)
	list_filter = ('submission__assignment', 'author', 'creation_date')

class ForumAdmin(admin.ModelAdmin):
	model = models.Forum
	list_display = ('course', 'lesson', 'name')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.CourseSection, CourseSectionAdmin)
admin.site.register(models.CourseRoster, CourseRosterAdmin)
admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TeamMember, TeamMemberAdmin)
admin.site.register(models.Syllabus, SyllabusAdmin)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.Assignment, AssignmentAdmin)
admin.site.register(models.AssignmentSubmission, SubmissionAdmin)
admin.site.register(models.GradedAssignmentSubmission, GradedSubmissionAdmin)
admin.site.register(models.Forum, ForumAdmin)
