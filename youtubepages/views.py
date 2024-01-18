from django.shortcuts import render, redirect ,HttpResponseRedirect
from youtubepages.models import createuserForm
from .models import VideoForm
from .forms import VideoUploadForm
import pandas as pd
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# ============================= HOMEPAGE ===================================


from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def homepage(request):
    Channel_Name_cookie = request.COOKIES.get('Channel_Name')
    
    EmailId_Cookie = request.COOKIES.get('EmailId_Cookie')
    try:

        createuservideo=createuserForm.objects.all()
        homepage_createuservideo = createuserForm.objects.filter(EmailId=EmailId_Cookie)
        firstvideo = VideoForm.objects.all()

        features = [
            {"category": "Space and Technology", "labels": "science"},
            {"category": "Space and Technology", "labels": "earth"},
            {"category": "Space and Technology", "labels": "space"},
            {"category": "Space and Technology", "labels": "technology"},
            # ----------------------------------------------------------------------------
            {"category": "Movie", "labels": "Movie"},
            {"category": "Movie", "labels": "film"},
            {"category": "Movie", "labels": "trailer"},
            # ----------------------------------------------------------------------------
            {"category": "Music", "labels": "music"},
            {"category": "Music", "labels": "song"},
            {"category": "Music", "labels": "bgm"},
            # ---------------------------------------------------------------------------
            {"category": "Animation", "labels": 'animation'},
            {"category": "Animation", "labels": 'cartoon'},
            {"category": "Animation", "labels": 'kunfu'},
            {"category": "Animation", "labels": 'barbie'},
             {"category": "Animation", "labels": 'elie'},
            # -------------------------------------------------------------------------
            {"category": "Games", "labels":  'games'},
            {"category": "Games", "labels": 'games'},
            {"category": "Games", "labels":  'gaming'},
            {"category": "Games", "labels":  'gun', },
            {"category": "Games", "labels":  'free fire'},
            {"category": "Games", "labels":  'pubg'},
            {"category": "Games", "labels":  'clash of clans'},
            # ---------------------------------------------------------------------------------------------------------------
            {"category": "Sports", "labels": 'sports'},
            {"category": "Sports", "labels":  'cricket'},
            {"category": "Sports", "labels":  'tennis'},
            {"category": "Sports", "labels":  'ball'},
            # ----------------------------------------------------------------------------------------------
            {"category": "Vehicles", "labels": 'vehicle'},
            {"category": "Vehicles", "labels":  'car'},
            {"category": "Vehicles", "labels":  'bike'},
            {"category": "Vehicles", "labels":  'cycle'},
            {"category": "Vehicles", "labels":  'Best_Rare_Everyday_Cars_from_my_Collection___Diecast_Model_Cars'},
            {"category": "Vehicles", "labels":  'Best Rare Everyday'},
            # --------------------------------------------------------------------------------------------
            {"category": "Nature", "labels": 'nature'},
            {"category": "Nature", "labels":  'leaf'},
            {"category": "Nature", "labels": 'bird'},
            {"category": "Nature", "labels": 'animal'},
            {"category": "Nature", "labels":  'plant'},
            {"category": "Nature", "labels":  'falls'},
        ]

        x = [i['labels'] for i in features]
        vectorizer = CountVectorizer()
        x_vectorized = vectorizer.fit_transform(x)
        y = [i['category'] for i in features]

        Dtc = DecisionTreeClassifier()
        dtf = Dtc.fit(x_vectorized, y)
        
        search = request.GET.get('Search')
        # file_path = 'youtubepages\\searches.csv'
        # with open(file_path, "a") as file:
        #     file.write(search + "\n")
        createuser_search_db = get_object_or_404(createuserForm, EmailId=EmailId_Cookie)
        if createuser_search_db.Search:
            createuser_search_db.Search = createuser_search_db.Search + "," + search
        else:
            createuser_search_db.Search = search
        createuser_search_db.save()

        
        createuser_search_db_list=createuserForm.objects.get(EmailId=EmailId_Cookie)
        createuser_search_db_list_split=createuser_search_db_list.Search.split(',')

        unique_search_list = []
        #list(set(createuser_search_db_list_split))
        for i in createuser_search_db_list_split:
            if i not in unique_search_list:
                unique_search_list.append(i)

        pred = []
        
        for i in unique_search_list:
            input_label_vectorized = vectorizer.transform([i])
            prediction = dtf.predict(input_label_vectorized)
            pred.append(prediction[0])

        final_prediction_list = []

        for j in pred:
            if j not in final_prediction_list:
                final_prediction_list.append(j)
            
        # hiddeninput=request.GET['hiddeninput']
        # if hiddeninput == "1":
        #     return redirect("/youtubepages/searchdisplay")

        return render(request, "homepage.html", {'search':search,'final_prediction_list':final_prediction_list,'unique_search_list':unique_search_list,'createuser_search_db_list_split':createuser_search_db_list_split,'EmailId_Cookie':EmailId_Cookie,'firstvideo': firstvideo,'homepage_createuservideo':homepage_createuservideo,'Channel_Name_cookie':Channel_Name_cookie})

    except Exception as e:
        print(e)
        search = ''
        
        return render(request, "homepage.html",{'EmailId_Cookie':EmailId_Cookie,'firstvideo': firstvideo,'homepage_createuservideo':homepage_createuservideo,'Channel_Name_cookie':Channel_Name_cookie})

 
def createvideo(request):
    try:
        form = VideoUploadForm(request.POST or None, request.FILES or None)
        
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('success') 
        else:
            return render(request, 'createvideo.html', {'form': form})
    
    except ValidationError as e:
        print(e)
        form = VideoUploadForm()
        return render(request, 'createvideo.html', {'form': form})
    except Exception as e:
        print(e)
        form = VideoUploadForm()
        return render(request, 'createvideo.html', {'form': form})

from django.core.exceptions import ObjectDoesNotExist

def signin(request):
    message = ''

    try:
        email_id = request.GET['useremail']
        password = request.GET['userpassword']
        
        user_object = createuserForm.objects.get(EmailId=email_id, Password=password)

        if user_object:
            response = redirect('homepage/')
            response.set_cookie('Channel_Name', user_object.ChannelName)
            response.set_cookie('EmailId_Cookie', user_object.EmailId)
            return response

    except :
        email_id=''
        password=''
        message = 'Please Enter Valid Email and Password'

    return render(request, "userlogin.html",{'message':message})


def createaccount(request):

    try:
         if request.method == "POST":
            imgdb=createuserForm()
            imgdb.Name = request.POST.get('name')
            imgdb.EmailId = request.POST.get('email')
            imgdb.Password = request.POST.get('password')
            imgdb.Gender = request.POST.get('gender')
            imgdb.ChannelName = request.POST.get('ChannelName')
            
            if len(request.FILES) != 0:
                imgdb.ProfileImage = request.FILES['image']
            imgdb.save()
            return HttpResponseRedirect('/youtubepages/')
    except:
        imgdb()
    return render(request,"createaccount.html")

def searchdisplay(request):
    Channel_Name_cookie = request.COOKIES.get('Channel_Name')
    EmailId_Cookie = request.COOKIES.get('EmailId_Cookie')
    try:
        homepage_createuservideo = createuserForm.objects.filter(EmailId=EmailId_Cookie)
        firstvideo = VideoForm.objects.all()

        features = [
            {"category": "Space and Technology", "labels": "science"},
            {"category": "Space and Technology", "labels": "earth"},
            {"category": "Space and Technology", "labels": "space"},
            {"category": "Space and Technology", "labels": "technology"},
            # ----------------------------------------------------------------------------
            {"category": "Movie", "labels": "Movie"},
            {"category": "Movie", "labels": "film"},
            {"category": "Movie", "labels": "trailer"},
            # ----------------------------------------------------------------------------
            {"category": "Music", "labels": "music"},
            {"category": "Music", "labels": "song"},
            {"category": "Music", "labels": "bgm"},
            # ---------------------------------------------------------------------------
            {"category": "Animation", "labels": 'animation'},
            {"category": "Animation", "labels": 'cartoon'},
            {"category": "Animation", "labels": 'kunfu'},
            {"category": "Animation", "labels": 'barbie'},
             {"category": "Animation", "labels": 'elie'},
            # -------------------------------------------------------------------------
            {"category": "Games", "labels":  'games'},
            {"category": "Games", "labels": 'games'},
            {"category": "Games", "labels":  'gaming'},
            {"category": "Games", "labels":  'gun', },
            {"category": "Games", "labels":  'free fire'},
            {"category": "Games", "labels":  'pubg'},
            {"category": "Games", "labels":  'clash of clans'},
            # ---------------------------------------------------------------------------------------------------------------
            {"category": "Sports", "labels": 'sports'},
            {"category": "Sports", "labels":  'cricket'},
            {"category": "Sports", "labels":  'tennis'},
            {"category": "Sports", "labels":  'ball'},
            # ----------------------------------------------------------------------------------------------
            {"category": "Vehicles", "labels": 'vehicle'},
            {"category": "Vehicles", "labels":  'car'},
            {"category": "Vehicles", "labels":  'bike'},
            {"category": "Vehicles", "labels":  'cycle'},
            {"category": "Vehicles", "labels":  'Best_Rare_Everyday_Cars_from_my_Collection___Diecast_Model_Cars'},
            {"category": "Vehicles", "labels":  'Best Rare Everyday'},
            # --------------------------------------------------------------------------------------------
            {"category": "Nature", "labels": 'nature'},
            {"category": "Nature", "labels":  'leaf'},
            {"category": "Nature", "labels": 'bird'},
            {"category": "Nature", "labels": 'animal'},
            {"category": "Nature", "labels":  'plant'},
            {"category": "Nature", "labels":  'falls'},
        ]

        x = [i['labels'] for i in features]
        vectorizer = CountVectorizer()
        x_vectorized = vectorizer.fit_transform(x)
        y = [i['category'] for i in features]

        Dtc = DecisionTreeClassifier()
        dtf = Dtc.fit(x_vectorized, y)

        
        createuser_search_db_list=createuserForm.objects.get(EmailId=EmailId_Cookie)
        createuser_search_db_list_split=createuser_search_db_list.Search.split(',')

        unique_search_list = []
        for i in createuser_search_db_list_split:
            if i not in unique_search_list:
                unique_search_list.append(i)

        pred = []
        
        for i in unique_search_list:
            input_label_vectorized = vectorizer.transform([i])
            prediction = dtf.predict(input_label_vectorized)
            pred.append(prediction[0])

        last_final_prediction_list=pred[-1]
    
        last_final_prediction_db=VideoForm.objects.all().filter(Category=last_final_prediction_list)




        return render(request, "searchdisplay.html", {'last_final_prediction_db':last_final_prediction_db,'createuser_search_db_list_split':createuser_search_db_list_split,'pred':pred,'last_final_prediction_list':last_final_prediction_list,'unique_search_list':unique_search_list,'EmailId_Cookie':EmailId_Cookie,'Channel_Name_cookie':Channel_Name_cookie})

    except Exception as e:
        print(e)
        search = ''
        
        return render(request, "searchdisplay.html",{'EmailId_Cookie':EmailId_Cookie,'Channel_Name_cookie':Channel_Name_cookie})


