from django.shortcuts import render

# Create your views here.
def profile(response):
    marks = [
        {"subject": "Bangla", "credit": 3, "mark": 73},
        {"subject": "English", "credit": 3, "mark": 67},
        {"subject": "Advanced Programming", "credit": 3, "mark": 82},
        {"subject": "AI", "credit": 3, "mark": 77},
        {"subject": "SDP 3", "credit": .75, "mark": 86},
    ]
    stdInfo = [
        {"name": "Masum", "age": 25, "id": "028"},
        {"name": "Imran", "age": 25, "id": "006"},
        {"name": "Ikram", "age": 26, "id": "009"},
        {"name": "Jobayer", "age": 24, "id": "011"},
        {"name": "Toufiq", "age": 25, "id": "016"},
    ]
    return render(response, 'student/profile.html',context= {'marks': marks, 'stdInfo': stdInfo})
