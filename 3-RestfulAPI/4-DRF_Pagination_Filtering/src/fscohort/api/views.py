from django.shortcuts import render
from fscohort.models import Student, Course
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.pagination import PageNumberPagination
from .pagination import NewPageNumberPagination, SecondPageNumberPagination


@api_view(["GET", "POST"])
def student_list_crate_api(request):

    if request.method == "GET":
        students = Student.objects.all()
        # birden fazla obje döndügü için. yoksa hata verir.
        serializer = StudentSerializer(
            students, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        # print("request_data: ", request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def student_get_update_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "GET":
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def course_list_create_api(request):

    if request.method == "GET":
        courses = Course.objects.all()
        # birden fazla obje döndügü için. yoksa hata verir.
        serializer = CourseSerializer(
            courses, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        # print("request_data: ", request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Course created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#!----------------------------------- Class Based Views

# class StudentListCreateAPIView(APIView):

#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True, context={'request': request}) # birden fazla obje döndügü için. yoksa hata verir.
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = StudentSerializer(data=request.data )
#         # print("request_data: ", request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Student created successfully"
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListCreateAPIView(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = NewPageNumberPagination

    # def get_queryset(self):

    #     queryset = Student.objects.all()
    #     student_name = self.request.query_params.get('student_name')
    #     if student_name is not None:
    #         queryset = queryset.filter(first_name=student_name)
    #     return queryset
    
    # GENERIC FILTERING
    
    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"


class CourseListCreateAPIView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = SecondPageNumberPagination
