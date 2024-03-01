from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tutions.models import Tution
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import RegistrationForm,ChangeUserForm
from django.views import View

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .tokens import account_activation_token

from django.contrib.auth.decorators import login_required
from tutions.models import Applicant  # Import Tution model from the correct location






# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
    
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form' : author_form})


#activate

# def activate(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse("Than you for your email confirmation. Now you can login your account.")
#     else:
#         return HttpResponse('Activation link is invalid!')


# def activateEmail(request, user, to_email):
#     mail_subject = 'Activate your user account.'
#     message = render_to_string('template_activate_account.html', {
#         'user': user.username,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     if email.send():
#         messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
#             received activation link to confirm and complete the registration. Note: Check your spam folder.')
#     else:
#         messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    activation_message = f'Dear {user}, please go to your email {to_email} inbox and click on the received activation link to confirm and complete the registration. Note: Check your spam folder.'
    
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])


    if email.send():
        messages.success(request, activation_message)
    else:
        messages.error(request, 'Problem sending confirmation email, please check if you typed the email correctly.')

    return redirect('register') 






# def register(request):
#     if request.method == 'POST':
#         register_form = forms.RegistrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('register')
    
#     else:
#         register_form = forms.RegistrationForm()
#     return render(request, 'register.html', {'form' : register_form, 'type': 'Register'})
    
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        #here mail send its a builtin Django doc
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = False
            user.save()
            
            
            # current_site = get_current_site(request)
            # mail_subject = 'Activation link has been sent to your email id'
            # message = render_to_string('acc_active_email.html', {
            #         'user':user, 
            #         'domain': current_site.domain,
            #         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #         'token':account_activation_token.make_token(request, user),
            #     })
            # to_email = register_form.cleaned_data.get('email')
            # email = EmailMessage(
            #                 mail_subject, message, to=[to_email]
            #     )
            # email.send()
            activateEmail(request, user, register_form.cleaned_data.get('email'))

            # messages.success(request, 'Please confirm your email address to complte the registration.')
            return redirect('register')
        else:
            for error in list(register_form.errors.values()):
                messages.error(request, error)
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type': 'Register'})




# def activate(request, uidb64, token):
#     return redirect('register')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('user_login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('register')







# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name, password= user_pass)
#             if user is not None:
#                 messages.success(request, 'Logged in Successfully')
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Login Information Invalid')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'register.html', {'form' : form, 'type': 'Login'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Login Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Login info invalid')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
 











# @login_required
# def profile(request):
#     data = Tution.objects.filter(author= request.user)
#     print(data)
#     print(request)
#     return render(request, 'profile.html', {'data': data})



# @login_required
# def edit_profile(request):

#     if request.method == 'POST':
#         profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile')
    
#     else:
#         profile_form = forms.ChangeUserForm(instance = request.user)
#     return render(request, 'update_profile.html', {'form' : profile_form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)

    return render(request, 'update_profile.html', {'form': profile_form})


def pass_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, data= request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, 'Password Updated successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user= request.user)
    return render(request, 'pass_change.html', {'form' : pass_form})

def user_logout(request):
    logout(request)
    return redirect('user_login')


# @login_required
# def profile(request):
#     # musicians = models.Musician.objects.all()
#     add_userdetails = models.Userdetails.objects.all()
#     return render(request,"profile.html", {'data': add_userdetails})



@login_required
def profile(request):
    # Filter Applicants based on the admin selection
    add_userdetails = models.Userdetails.objects.filter(user=request.user)

    selected_applicants = Applicant.objects.filter(user=request.user, is_selected=True)

    # Extract the associated Tution instances from the selected applicants
    selected_tutions = [applicant.tution for applicant in selected_applicants]

    print(selected_tutions)

    return render(request, "profile.html", {'data': add_userdetails, 'selected_tutions': selected_tutions})









# @login_required
# def add_userdetails(request):
#     if request.method == 'POST':
#         form = forms.UserdetailsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = forms.UserdetailsForm()
#     return render(request, 'add_userdetails.html', {'form' : form})

@login_required
def add_userdetails(request):
    if request.method == 'POST':
        form = forms.UserdetailsForm(request.POST)
        if form.is_valid():
            userdetails = form.save(commit=False)
            print("Logged-in user:", request.user)  # Debug statement
            userdetails.user = request.user  # Associate the user with the userdetails
            userdetails.save()
            return redirect('profile')
    else:
        form = forms.UserdetailsForm()
    return render(request, 'add_userdetails.html', {'form': form})


@login_required
def edit_userdetails(request, id):
    userdetails = models.Userdetails.objects.get(pk=id) 
    userdetails_form = forms.UserdetailsForm(instance=userdetails)

    if request.method == 'POST':
        userdetails_form = forms.UserdetailsForm(request.POST, instance=userdetails)
        if userdetails_form.is_valid():
            userdetails_form.save() 
            return redirect('profile')
    
    return render(request, 'add_userdetails.html', {'form' : userdetails_form})


@login_required
def delete_userdetails(request, id):
    std = models.Userdetails.objects.get(pk = id)
    std.delete()
    return redirect("profile")