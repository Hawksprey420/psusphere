from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for colleges, programs, organizations, students, and org members'
    
    def handle (self, *args, **kwargs):
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(100)
        
    def create_organization (self, count):
        fake = Faker()
        
        #for_in_range(count):
            #words = [fake.word() for _ in range(2)]  # two words 