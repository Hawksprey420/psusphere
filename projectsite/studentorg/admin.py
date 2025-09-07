from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

#admin.site.register(College)
#admin.site.register(Program)
#admin.site.register(Organization)
#admin.site.register(Student)
#admin.site.register(OrgMember)
# Register your models here.

@admin.register(Student)
class StudentAdmin (admin.ModelAdmin):
    list_display = ('student_id', 'last_name', 'first_name', 'middle_name'
                    ,'program')
    search_fields = ('last_name', 'first_name')

@admin.register(OrgMember)
class OrgMemberAdmin (admin.ModelAdmin):
    list_display = ('student',"get_member_program",'organization', 
                    'date_joined')
    
    search_fields = ("student_last_name", "student_first_name",)
    
    def get_member_program (self, obj):
        try:
            member = Student.objects.get(id=obj.student.id)
            return member.program
        
        except Student.DoesNotExist:
            return None

@admin.register(College)
class CollegeAdmin (admin.ModelAdmin):
    list_display = ('college_name', 'created_at', 'updated_at')
    search_fields = ('college_name',)
    list_filter = ('created_at', 'updated_at',)

@admin.register(Program)
class ProgramAdmin (admin.ModelAdmin):
    list_display = ('program_name', 'college', 'created_at', 'updated_at')
    search_fields = ('program_name',)
    list_filter = ('college', 'created_at', 'updated_at',)

@admin.register(Organization)
class OrganizationAdmin (admin.ModelAdmin): 
    list_display = ('name', 'college', 'created_at', 'updated_at')
    search_fields = ('name', 'description',)
    list_filter = ('college', 'created_at', 'updated_at',)



# to do later: add filters  
# list_filter = ('program', 'organization',) for references.

#admin.site.register(College)
#admin.site.register(Program)
#admin.site.register(Organization)