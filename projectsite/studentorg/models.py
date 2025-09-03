from django.db import models

# Create your models here.

class BaseModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    college_name = models.CharField(max_length=255)

    def __str__(self):
        return self.college_name
    
class Program (BaseModel):
    program_name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return self.program_name
    
class Organization (BaseModel):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE, related_name='organizations')
    description = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Student (BaseModel):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)   
    last_name = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OrgMember (BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='org_memberships')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=255, null=True, blank=True)