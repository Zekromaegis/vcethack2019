from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.views.generic.edit import UpdateView
from .models import Student
from .forms import UserForm
import pickle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import json
# Create your views here.

dbfile = open('IndustryFinder/Classifier.pickle', 'rb')
Classifier = pickle.load(dbfile)
dbfile.close()
dbfile2 = open('IndustryFinder/Scaler.pickle', 'rb')
Scaler = pickle.load(dbfile2)
dbfile2.close()

df = pd.read_csv('IndustryFinder/abc.csv', names = [
    'Marks_10',
    'Marks_12',
    'Marks_CGPA',
    'Hackathons',
    'Research',
    'Internship',
    'Projects',
    'Social_hours',
    'Sports',
    'Company'
])

def equivalent(sports):
    National = 3
    State = 2
    Regional = 1
    gold = 3
    silver = 2
    bronze = 1
    sports['Equivalent'] = int(
        National * ( gold * sports['N_Gold'] + silver * sports['N_Silver'] + bronze * sports['N_Bronze'] )
        + State * ( gold * sports['S_Gold'] + silver * sports['S_Silver'] + bronze * sports['S_Bronze'] )
        + Regional * ( gold * sports['R_Gold'] + silver * sports['R_Silver'] + bronze * sports['R_Bronze'] )
    )
def percentilefinder(data, datalist):
    j = 0
    for i in datalist:
        if( data >= datalist[i]):
            j = j + 1
    return j/len(datalist)

class Home(generic.base.TemplateView):
    template_name='home.html'
    def get(self,request):
        try:
            s = request.user.student
            company = Classifier.predict(Scaler.transform(
            [[
            s.academics['Marks_10'],
            s.academics['Marks_12'],
            s.academics['Marks_CGPA'],
            s.technical['Hackathons'],
            s.technical['Research'],
            s.technical['Internships'],
            s.technical['Projects'],
            s.social,
            s.sports['Equivalent'],
            ]]
            ))

            df2 = df[df['Company'] == company[0]]
            meandf2 = df2[['Marks_CGPA','Sports','Social_hours','Research']].mean().tolist()
            maxdf2 = df2[['Marks_CGPA','Sports','Social_hours','Research']].max().tolist()
            scatter = df2[['Marks_10','Marks_12','Hackathons','Internship','Projects']].T.values.tolist()
            a = {
                'company':company[0],
                'meandf2':meandf2,
                'maxdf2':maxdf2,
                'scatter':scatter,
            }
            s = request.user.student
            b = [
                s.academics['Marks_10'],
                s.academics['Marks_12'],
                s.academics['Marks_CGPA'],
                s.technical['Hackathons'],
                s.technical['Research'],
                s.technical['Internships'],
                s.technical['Projects'],
                s.social,
                s.sports['Equivalent'],
            ]

    #        percentile = [
    #           (percentilefinder(s.academics['Marks_10'],df2['Marks_10']) + 
    #          percentilefinder(s.academics.['Marks_12'],df2['Marks_12']))/2,
    #         percentilefinder(s.sports['Equivalent'], df2['Sports']),
        #        percentilefinder(s.technical.Hackathons,df2['Hackathons']) +
        #       percentilefinder(s.technical.Research,df2['Research']) +
        #      percentilefinder(s.technical.Internships,df2['Internship']),
        #     percentilefinder(s.social, df2['Social_hours']),
            #]

            return render(request,self.template_name,{'b':a,'a':b,'student':request.user.student})
        except:
            return redirect('IndustryFinder:student-update')

def StudentUpdate(request):
    try:
        return render(request, r'IndustryFinder/student_form.html', {'student':request.user.student})
    except:
        return redirect('login')

def saveStudentData(request):
    if request.method == "POST":
        s = request.user.student
        academics = {
            "Marks_10": int(int(request.POST["Marks_10"]) / int(request.POST["Marks_10_max"]) * 500),
            "Marks_12": int(int(request.POST["Marks_12"]) / int(request.POST["Marks_12_max"]) * 650),
            "Marks_CGPA": float(request.POST["Marks_CGPA"]),
        }
        technical = {
            "Hackathons": int(request.POST["Hackathons"]),
            "Research": int(request.POST["Research"]),
            "Projects": int(request.POST["Projects"]),
            "Internships": int(request.POST["Internships"]),
        }
        sports = {
            "N_Gold": int(request.POST["N_Gold"]),
            "S_Gold": int(request.POST["S_Gold"]),
            "R_Gold": int(request.POST["R_Gold"]),
            "N_Silver": int(request.POST["N_Silver"]),
            "S_Silver": int(request.POST["S_Silver"]),
            "R_Silver": int(request.POST["R_Silver"]),
            "N_Bronze": int(request.POST["N_Bronze"]),
            "S_Bronze": int(request.POST["S_Bronze"]),
            "R_Bronze": int(request.POST["R_Bronze"]),
        }
        equivalent(sports)
        s.academics = academics
        s.sports = sports
        s.technical = technical
        s.social = int(request.POST["Social_Hours"])
        s.save()
    return redirect('IndustryFinder:home')

class DetailView(generic.DetailView):
    model = Student
    template_name = r'IndustryFinder/student_detail.html'

class UserFormView(generic.View):
    form_class = UserForm
    template_name = r'IndustryFinder/signup_form.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            #cleaned-normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            student = Student()
            student.user = user
            student.social = 0
            student.save()
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('IndustryFinder:student-update')
                    
        return render(request, self.template_name, {'form' : form})