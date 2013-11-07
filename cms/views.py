from django.contrib.auth.models import User, Group, Permission
from models import *
from rest_framework import viewsets, generics, authentication, permissions
from serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status, parsers, renderers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.renderers import (
    BaseRenderer,
    JSONRenderer,
    BrowsableAPIRenderer
)
from django.forms.models import model_to_dict
import datetime
# Create your views here.

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            user = model_to_dict(token.user)
            del user['password']
            return Response({'token': token.key, 'user':user})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
		"""
		API endpoint that allows users to be viewed or edited.
		"""
		# queryset = User.objects.all()
		model = User
		serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
		"""
		API endpoint that allows groups to be viewed or edited.
		"""
		model = Group
		# queryset = Group.objects.all()
		serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
		"""
		API endpoint that allows permissions to be viewed or edited.
		"""
		model = Permission
		# queryset = Permission.objects.all()
		serializer_class = PermissionSerializer

class CourseViewSet(viewsets.ModelViewSet):
		model = Course
		serializer_class = CourseSerializer

class CourseSectionViewSet(viewsets.ModelViewSet):
		model = CourseSection
		serializer_class = CourseSectionSerializer

class CourseRosterViewSet(viewsets.ModelViewSet):
		model = CourseRoster
		serializer_class = CourseRosterSerializer

class SyllabusViewSet(viewsets.ModelViewSet):
		model = Syllabus
		serializer_class = SyllabusSerializer

class LessonViewSet(viewsets.ModelViewSet):
		model = Lesson
		serializer_class = LessonSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
		model = Assignment
		serializer_class = AssignmentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
		model = Document
		serializer_class = DocumentSerializer

class StudentsList(viewsets.ModelViewSet):
		# model = CmsUser
		serializer_class = UserSerializer
		student_group, created = Group.objects.get_or_create(name='student')
		queryset = User.objects.filter(courses__group_id=student_group.id)

class UpcomingAssignmentsList(ListAPIView):
		serializer_class = AssignmentSerializer
		model = Assignment
		# render_classes = (BrowsableAPIRenderer, JSONRenderer)

		def get_queryset(self):
				user = self.request.user
				# lessons = [course.lessons for course in courses]
				assignments = Assignment.objects.filter(lesson__course__sections__members__user__id=user.id,
						due_date__gte=datetime.date.today())
				return assignments

custom_obtain_auth_token = CustomObtainAuthToken.as_view()
upcoming_assignments = UpcomingAssignmentsList.as_view()
