"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentorg import views
from studentorg.views import (
    # Organization
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    # OrgMember
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    # Student
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    # College
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    # Program
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
    
    HomePageView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),  # allauth routes
    path('', views.HomePageView.as_view(), name='home'), 
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<int:pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    
    path('orgmember_list', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<int:pk>', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<int:pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    
    path('student_list', StudentList.as_view(), name='student-list'),
    path('student/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<int:pk>', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('college/add', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<int:pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<int:pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    
    path('program_list', ProgramList.as_view(), name='program-list'),
    path('program/add', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<int:pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<int:pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),

]
