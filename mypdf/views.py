from django.shortcuts import render
from .models import Profile
# Create your views here.

def take(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        graduation = request.POST.get("graduation", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")
        
        profile = Profile(name=name, email=email, phone=phone, summary=summary, graduation=graduation, university=university, school=school, previous_work=previous_work, skills=skills)
        profile.save()
        
    return render(request, 'pdf/take.html')

