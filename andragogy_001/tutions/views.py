from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404

from django.db import IntegrityError
from django.contrib import messages
from .models import Tution, Applicant
from .forms import CommentForm, ApplicantForm
from django.views import View

# Create your views here.

# @login_required
# def add_post(request):
#     if request.method == 'POST': # user post request koreche
#         post_form = forms.PostForm(request.POST)
#         if post_form.is_valid():
#             # post_form.cleaned_data['author'] = request.user
#             post_form.instance.author = request.user
#             post_form.save()
#             return redirect('add_post')
    
#     else: # user normally website e gele blank form pabe
#         post_form = forms.PostForm()
#     return render(request, 'add_post.html', {'form' : post_form})


#add post using class based view

@method_decorator(login_required, name= 'dispatch')
class AddTutionCreateView(CreateView):
    model = models.Tution
    form_class = forms.TutionForm
    template_name = 'add_tution.html'
    success_url = reverse_lazy('add_tution')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id) 
#     post_form = forms.PostForm(instance=post)
#     # print(post.title)
#     if request.method == 'POST': # user post request koreche
#         post_form = forms.PostForm(request.POST, instance=post) # user er post request data ekhane capture korlam
#         if post_form.is_valid(): # post kora data gula amra valid kina check kortechi
#             post_form.instance.author = request.user
#             post_form.save() # jodi data valid hoy taile database e save korbo
#             return redirect('homepage') # sob thik thakle take add author ei url e pathiye dibo
    
#     return render(request, 'add_post.html', {'form' : post_form})

@method_decorator(login_required, name= 'dispatch')
class EditTutionView(UpdateView):
    model = models.Tution
    form_class = forms.TutionForm
    template_name = 'add_tution.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


# @login_required
# def delete_post(request, id):
#     post = models.Post.objects.get(pk=id) 
#     post.delete()
#     return redirect('homepage')


@method_decorator(login_required, name= 'dispatch')
class DeleteTutionView(DeleteView):
    model = models.Tution
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# class DetailTutionView(DetailView):
#     model = models.Tution
#     pk_url_kwarg = 'id'
#     template_name = 'tution_details.html'
# class DetailTutionView(CreateView):
#     model = Applicant
#     form_class = ApplicantForm
#     template_name = 'tution_details.html'
#     success_url = 'some_success_url'  # Define the URL to redirect after successful application

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.tuition = Tution.objects.get(pk=self.kwargs['id'])
#         return super().form_valid(form)

#     def post(self, request, *args, **kwargs):
#         comment_form = forms.CommentForm(data=self.request.POST)
#         post = self.get_object()

#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.author = self.request.user
#             new_comment.tution = post
#             new_comment.save()

#         return self.get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object #post model er object store
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()


#         context['comments'] = comments
#         context["comment_form"] = comment_form
#         return context
    

# class DetailTutionView(DetailView):
#     model = Tution
#     template_name = 'tution_details.html'
#     context_object_name = 'tution'
#     pk_url_kwarg = 'pk'

#     def post(self, request, *args, **kwargs):
#         tution = self.get_object()
#         applicant_form = ApplicantForm(request.POST)

#         if applicant_form.is_valid():
#             applicant = applicant_form.save(commit=False)
#             applicant.user = request.user
#             applicant.tuition = tution
#             applicant.save()
#             messages.success(request, 'Application submitted successfully!')
#             return redirect('tution_details', id=tution.id)
#         else:
#             messages.error(request, 'Error submitting application. Please check the form.')
#             return render(request, self.template_name, {'tution': tution, 'applicant_form': applicant_form})
        

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object #post model er object store
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()


#         context['comments'] = comments
#         context["comment_form"] = comment_form
#         return context
    
@method_decorator(login_required, name='dispatch')
class DetailTutionView(CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'tution_details.html'
    success_url = reverse_lazy('some_success_url')  # Replace with the actual success URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tution = Tution.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        applicant_form = ApplicantForm(data=self.request.POST)

        if comment_form.is_valid() and applicant_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = self.request.user
            new_comment.tution = Tution.objects.get(pk=self.kwargs['pk'])
            new_comment.save()

            applicant = applicant_form.save(commit=False)
            applicant.user = self.request.user
            applicant.tution = Tution.objects.get(pk=self.kwargs['pk'])

            try:
                applicant.save()
            except IntegrityError:
                # Handle IntegrityError, e.g., duplicate applications
                pass

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tution = Tution.objects.get(pk=self.kwargs['pk'])
        comments = tution.comments.all()
        comment_form = CommentForm()
        applicant_form = ApplicantForm()

        context['tution'] = tution
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['applicant_form'] = applicant_form

        return context
    
@method_decorator(login_required, name='dispatch')
class DetailTutionView2(CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'tution_details2.html'
    success_url = reverse_lazy('some_success_url')  # Replace with the actual success URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tution = Tution.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        applicant_form = ApplicantForm(data=self.request.POST)

        if comment_form.is_valid() and applicant_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = self.request.user
            new_comment.tution = Tution.objects.get(pk=self.kwargs['pk'])
            new_comment.save()

            applicant = applicant_form.save(commit=False)
            applicant.user = self.request.user
            applicant.tution = Tution.objects.get(pk=self.kwargs['pk'])

            try:
                applicant.save()
            except IntegrityError:
                # Handle IntegrityError, e.g., duplicate applications
                pass

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tution = Tution.objects.get(pk=self.kwargs['pk'])
        comments = tution.comments.all()
        comment_form = CommentForm()
        applicant_form = ApplicantForm()

        context['tution'] = tution
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['applicant_form'] = applicant_form

        return context



    
class ApplyForTutionView(View):
    template_name = 'tution_details2.html'

    def get(self, request, *args, **kwargs):
        tution_id = kwargs.get('id')
        tution = Tution.objects.get(pk=tution_id)
        applicant_form = ApplicantForm()
        return render(request, self.template_name, {'tution': tution, 'applicant_form': applicant_form})

    def post(self, request, *args, **kwargs):
        tution_id = kwargs.get('id')
        tution = Tution.objects.get(pk=tution_id)
        applicant_form = ApplicantForm(request.POST)

        if applicant_form.is_valid():
            applicant = applicant_form.save(commit=False)
            applicant.user = request.user
            applicant.tution = tution 
            applicant.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('apply_for_tution', id=tution_id)
        else:
            messages.error(request, 'Error submitting application. Please check the form.')
            return render(request, self.template_name, {'tution': tution, 'applicant_form': applicant_form})

    