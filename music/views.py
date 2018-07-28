from django.shortcuts import render, HttpResponse

from .forms import ProfileForm
from django.shortcuts import redirect
from .models import UserInfo, Profile, Notification
import time;

# welcome page
def index(request):
    return render(request, 'login/index.html')


def afterLogin(request):
    if 'username' not in request.session:
        try:
            uname = request.POST["uname"]
            psw = request.POST["psw"]
            all_users = UserInfo.objects.all()
            all_users1 = Profile.objects.filter()
            get_previous_notifiction = Notification.objects.get()
            noti = get_previous_notifiction.reception

            auth = 1;
            if auth == 1:
                for us in all_users:
                    if (us.uname == uname) and (us.psw == psw):
                        # enter username into session
                        request.session['username'] = uname
                        if uname == 'Doctor':
                            noti = get_previous_notifiction.doctor
                        elif uname == 'Reception':
                            noti = get_previous_notifiction.reception
                        elif uname == 'Nurse':
                            noti = get_previous_notifiction.nurse
                        # call html page and session value username
                        return render(request, 'login/login.html',
                                      {'username': uname, 'user': all_users1, 'notification': noti})
                        break
                    else:
                        auth = 2
                if auth == 2:
                    return redirect('/music/')

        except:
            return redirect('/music/')
    else:
        all_users1 = Profile.objects.filter()
        get_previous_notifiction = Notification.objects.get()
        noti = get_previous_notifiction.reception
        uname = request.session['username']
        if uname == 'Doctor':
            noti = get_previous_notifiction.doctor
        elif uname == 'Reception':
            noti = get_previous_notifiction.reception
        elif uname == 'Nurse':
            noti = get_previous_notifiction.nurse
        # call html page and session value username
        return render(request, 'login/login.html',
                      {'username': uname, 'user': all_users1, 'notification': noti})




def view(request):
    all_users = UserInfo.objects.all()
    return render(request, 'login/save.html', {'users': all_users})

# save uploaded data
def SaveProfile(request):
    get_previous_notifiction = Notification.objects.get()
    count_reception = get_previous_notifiction.reception
    count_reception = int(count_reception)
    count_nurse = get_previous_notifiction.nurse
    count_nurse = int(count_nurse)
    count_doctor = get_previous_notifiction.doctor
    count_doctor = int(count_doctor)
    all_users1 = Profile.objects.filter()
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.description = MyProfileForm.cleaned_data["description"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            if profile.name == 'Doctor':
                if request.POST.get('share1') == 'on':
                    count_reception += 1
                    profile.share1 = 'Reception'
                else:
                    profile.share1 = 'None'

                if request.POST.get('share2') == 'on':
                    count_nurse += 1
                    profile.share2 = 'Nurse'
                else:
                    profile.share2 = 'None'

            if profile.name == 'Nurse':
                if request.POST.get('share1') == 'on':
                    count_reception += 1
                    profile.share1 = 'Reception'
                else:
                    profile.share1 = 'None'

                if request.POST.get('share2') == 'on':
                    count_doctor += 1
                    profile.share2 = 'Doctor'
                else:
                    profile.share2 = 'None'

            if profile.name == 'Reception':
                if request.POST.get('share1') == 'on':
                    count_doctor += 1
                    profile.share1 = 'Doctor'
                else:
                    profile.share1 = 'None'

                if request.POST.get('share2') == 'on':
                    count_nurse += 1
                    profile.share2 = 'Nurse'
                else:
                    profile.share2 = 'None'
            get_previous_notifiction.nurse = count_nurse
            get_previous_notifiction.reception = count_reception
            get_previous_notifiction.save()
            localtime = time.asctime(time.localtime(time.time()))
            profile.time = localtime
            profile.save()
        else:
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.description = MyProfileForm.cleaned_data["description"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            if profile.name == 'Doctor':
                if request.POST.get('share1') == 'on':
                    count_reception += 1
                    profile.share1 = 'Reception'
                else:
                    profile.share1 = 'None'

            if request.POST.get('share2') == 'on':
                count_nurse += 1
                profile.share2 = 'Nurse'
            else:
                profile.share2 = 'None'

            if profile.name == 'Nurse':
                if request.POST.get('share1') == 'on':
                    count_reception += 1
                    profile.share1 = 'Reception'
                else:
                    profile.share1 = 'None'

                if request.POST.get('share2') == 'on':
                    count_doctor += 1
                    profile.share2 = 'Doctor'
                else:
                    profile.share2 = 'None'

            if profile.name == 'Reception':
                if request.POST.get('share1') == 'on':
                    count_doctor += 1
                    profile.share1 = 'Doctor'
                else:
                    profile.share1 = 'None'

                if request.POST.get('share2') == 'on':
                    count_nurse += 1
                    profile.share2 = 'Nurse'
                else:
                    profile.share2 = 'None'
            get_previous_notifiction.nurse = count_nurse
            get_previous_notifiction.reception = count_reception
            get_previous_notifiction.save()
            localtime = time.asctime(time.localtime(time.time()))
            profile.time = localtime
            profile.save()
            return redirect('/music/upload_report/')
    else:
        # MyProfileForm = ProfileForm()
        return redirect('/music/upload_report/')
    return redirect('/music/upload_report/')


# user_info = UserInfo(uname=uname, psw=psw)
# user_info.save()


def logout(request):
    get_previous_notifiction = Notification.objects.get()
    x = request.session['username']
    if (x == 'Doctor'):
        get_previous_notifiction.doctor = 0
    elif (x == 'Nurse'):
        get_previous_notifiction.nurse = 0
    elif (x == 'Reception'):
        get_previous_notifiction.reception = 0

    get_previous_notifiction.save()
    del request.session['username']
    return redirect('/music/')
