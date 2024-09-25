from django.shortcuts import render
from .serializer import Create_elections_serializer
import base64
import json
from rest_framework.response import Response
from login_apis.models import users 
from rest_framework.decorators import api_view
from .models import create_election
from rest_framework import generics
from django.views.decorators.cache import cache_page
from voting_system_b.settings import CACHE_TTL
# from .models import create_elections,candiates
from .serializer import Create_elections_serializer
from .models import create_election as ce
# class create_candidates(generics.ListCreateAPIView):
#         queryset=candidate.objects.all()
#         serializer_class=Create_elections_serializer
def create_unique_id(request):
        name=request.data.get("name")
        
        number_of_candidates=request.data.get("number_of_candidates")
        unique_id=generate_unique_id(name,number_of_candidates)
        id=type(unique_id)
        return unique_id
# class create_elections(generics.CreateAPIView):
#         unique_id=create_unique_id(request)
#         request.unique_id=unique_id
#         queryset=create_election.objects.all()
#         serializer_class=Create_elections_serializer
@api_view(["POST","PUT","GET"])
@cache_page(CACHE_TTL)
def create_election(request):
    if request.method=="GET":
        elections=ce.objects.all()
        print("get_called")
       
        serializer=Create_elections_serializer(elections,many=True)

       
        return Response(serializer.data)
        
    if request.method=="POST":
         unique_id=create_unique_id(request)
         request.data["unique_id"]=unique_id
         print(request.data)
         serializer=Create_elections_serializer(data=request.data)
         if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data)
         else:
                print(serializer.errors)
                return Response("serilizer is not valid")
    if request.method=="PUT":
        check_name=request.data["names"]
        user=users.objects.all().filter(username=check_name).first()
        if not user:
                return Response({"status":"not the user"})
        filter_user=ce.objects.all().filter(organizer=user.id)
        if filter_user:
            print(request.data)
            print(filter_user.values())
            filter_user.title=request.data["title"]
            return Response({"status":"updated"})
        if not filter_user:
                return Response({"status":"user do not have any election "}) 
        print(filter_user.values())

        

        
@api_view(["POST"])
def do_vote(request):
                
                candidates=request.data["names"]
                candidates=candiates.object.filter(name=candidates).first()
                candidates.number_of_votes=candidates.number_of_votes+1
                
                candidates.save()
                
                return Response("done")
# @api_view(["POST"])
def create_unique_id(request):
        name=request.data.get("name")
        
        number_of_candidates=request.data.get("number_of_candidates")
        unique_id=generate_unique_id(name,number_of_candidates)
        id=type(unique_id)
        return unique_id
@api_view(["POST"])
def select_election(request):
    
    unique_id=request.data.get("unique_id")
    if unique_id:
           
           election=ce.objects.all().filter(unique_id=unique_id).values()
           return Response(election)
    
@api_view(["GET"])
def details_of_election(request):
       election_name=request.dta.get("election_name")
       number_of_candidates=request.data.get("number_of_candidates")
       
def generate_unique_id(name: str, number: int) -> str:
    combined = f"{name}:{number}"
    
    # Encode the combined string to Base64
    encoded_bytes = base64.urlsafe_b64encode(combined.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    
    return encoded_str

def decode_unique_id(encoded_str: str) :
    # Decode the Base64 string back to the original combined string
    decoded_bytes = base64.urlsafe_b64decode(encoded_str.encode('utf-8'))
    decoded_str = decoded_bytes.decode('utf-8')
    
    # Split the combined string to retrieve name and number
    name, number = decoded_str.split(':')
    
    return name, int(number)
# Example usage


                                

        
