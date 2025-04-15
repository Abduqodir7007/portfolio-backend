from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import (
    Project, 
    Hero, 
    Social,
    Education, 
    Category,
    Skill,
    Work,
    )
from rest_framework.views import APIView
from .serializers import (
    ProjectSerializer,
    CategorySerializer,
    SkillSerializer,
    HeroSerializer,
    SocialSerializer,
    EducationSerializer,
    WorkSerializer,
    )

class CategoryView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all categories",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=CategorySerializer,
        operation_description="Create a new category",
        responses={201: CategorySerializer()}
    )
    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=CategorySerializer,
        operation_description="Update an existing category by ID",
        responses={200: CategorySerializer()}
    )
    def put(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=404)

        serializers = CategorySerializer(category, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a category by ID",
        responses={200: openapi.Response("Category deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=404)
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=200)


class SkillView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all skills",
        responses={200: SkillSerializer(many=True)}
    )
    def get(self, request):
        skills = Skill.objects.all()
        serializers = SkillSerializer(skills, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=SkillSerializer,
        operation_description="Create a new skill",
        responses={201: SkillSerializer()}
    )
    def post(self, request):
        serializers = SkillSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=SkillSerializer,
        operation_description="Update an existing skill by ID",
        responses={200: SkillSerializer()}
    )
    def put(self, request, pk):
        try:
            skill = Skill.objects.get(id=pk)
        except Skill.DoesNotExist:
            return Response({"message": "Skill not found"}, status=404)

        serializers = SkillSerializer(skill, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a skill by ID",
        responses={200: openapi.Response("Skill deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            skill = Skill.objects.get(id=pk)
        except Skill.DoesNotExist:
            return Response({"message": "Skill not found"}, status=404)
        skill.delete()
        return Response({"message": "Skill deleted successfully"}, status=200)

class ProjectView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all projects ordered by rank",
        responses={200: ProjectSerializer(many=True)}
    )
    def get(self, request):
        projects = Project.objects.all().order_by('-rank')
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=ProjectSerializer,
        operation_description="Create a new project",
        responses={201: ProjectSerializer()}
    )
    def post(self, request):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=ProjectSerializer,
        operation_description="Update an existing project by ID",
        responses={200: ProjectSerializer()}
    )
    def put(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"message": "Project not found"}, status=404)

        serializers = ProjectSerializer(project, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a project by ID",
        responses={200: openapi.Response("Project deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"message": "Project not found"}, status=404)
        project.delete()
        return Response({"message": "Project deleted successfully"}, status=200)


class HeroView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all hero sections",
        responses={200: HeroSerializer(many=True)}
    )
    def get(self, request):
        hero = Hero.objects.all()
        serializers = HeroSerializer(hero, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=HeroSerializer,
        operation_description="Create a new hero section",
        responses={201: HeroSerializer()}
    )
    def post(self, request):
        serializers = HeroSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=HeroSerializer,
        operation_description="Update an existing hero section by ID",
        responses={200: HeroSerializer()}
    )
    def put(self, request, pk):
        try:
            hero = Hero.objects.get(id=pk)
        except Hero.DoesNotExist:
            return Response({"message": "Hero not found"}, status=404)

        serializers = HeroSerializer(hero, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a hero section by ID",
        responses={200: openapi.Response("Hero deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            hero = Hero.objects.get(id=pk)
        except Hero.DoesNotExist:
            return Response({"message": "Hero not found"}, status=404)
        hero.delete()
        return Response({"message": "Hero deleted successfully"}, status=200)
    

class SocialView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all social media links",
        responses={200: SocialSerializer(many=True)}
    )
    def get(self, request):
        social = Social.objects.all()
        serializers = SocialSerializer(social, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=SocialSerializer,
        operation_description="Create a new social media link",
        responses={201: SocialSerializer()}
    )
    def post(self, request):
        serializers = SocialSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=SocialSerializer,
        operation_description="Update an existing social media link by ID",
        responses={200: SocialSerializer()}
    )
    def put(self, request, pk):
        try:
            social = Social.objects.get(id=pk)
        except Social.DoesNotExist:
            return Response({"message": "Social not found"}, status=404)

        serializers = SocialSerializer(social, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a social media link by ID",
        responses={200: openapi.Response("Social deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            social = Social.objects.get(id=pk)
        except Social.DoesNotExist:
            return Response({"message": "Social not found"}, status=404)
        social.delete()
        return Response({"message": "Social deleted successfully"}, status=200)


class EducationView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all education entries",
        responses={200: EducationSerializer(many=True)}
    )
    def get(self, request):
        education = Education.objects.all()
        serializers = EducationSerializer(education, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=EducationSerializer,
        operation_description="Create a new education entry",
        responses={201: EducationSerializer()}
    )
    def post(self, request):
        serializers = EducationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=EducationSerializer,
        operation_description="Update an existing education entry by ID",
        responses={200: EducationSerializer()}
    )
    def put(self, request, pk):
        try:
            education = Education.objects.get(id=pk)
        except Education.DoesNotExist:
            return Response({"message": "Education not found"}, status=404)

        serializers = EducationSerializer(education, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete an education entry by ID",
        responses={200: openapi.Response("Education deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            education = Education.objects.get(id=pk)
        except Education.DoesNotExist:
            return Response({"message": "Education not found"}, status=404)
        education.delete()
        return Response({"message": "Education deleted successfully"}, status=200)
    

class WorkView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all work experiences",
        responses={200: WorkSerializer(many=True)}
    )
    def get(self, request):
        work = Work.objects.all()
        serializers = WorkSerializer(work, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        request_body=WorkSerializer,
        operation_description="Create a new work experience",
        responses={201: WorkSerializer()}
    )
    def post(self, request):
        serializers = WorkSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        request_body=WorkSerializer,
        operation_description="Update an existing work experience by ID",
        responses={200: WorkSerializer()}
    )
    def put(self, request, pk):
        try:
            work = Work.objects.get(id=pk)
        except Work.DoesNotExist:
            return Response({"message": "Work not found"}, status=404)

        serializers = WorkSerializer(work, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a work experience by ID",
        responses={200: openapi.Response("Work deleted successfully")}
    )
    def delete(self, request, pk):
        try:
            work = Work.objects.get(id=pk)
        except Work.DoesNotExist:
            return Response({"message": "Work not found"}, status=404)
        work.delete()
        return Response({"message": "Work deleted successfully"}, status=200)