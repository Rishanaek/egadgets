

# Create your views here.
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from.forms import Loginform,Regform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView

# Create your views here.
# class LandingView(View):
#     def get(self,request):
#         return render(request,'landing.html')
class LandingView(TemplateView):
    template_name='landing.html'
    
# class LoginView(View):
#      def get(self,request):
#         form=Loginform()
#         return render(request,'login.html',{"form":form})
#      def post(self,request):
#          form=Loginform(data=request.POST)
#          if form.is_valid():
#              uname=form.cleaned_data.get('username')
#              pswd=form.cleaned_data.get('password')
#              user=authenticate(request,username=uname,password=pswd)
#              if user:
#                  return redirect('home')
#              else:
#                  messages.error(request,"Login Failed ")
#                  return redirect('log')
#          return render(request,'login.html',{'form':form})

class LoginView(FormView):
    template_name='login.html'
    form_class=Loginform
    def post(self,request):
         form=Loginform(data=request.POST)
         if form.is_valid():
             uname=form.cleaned_data.get('username')
             pswd=form.cleaned_data.get('password')
             user=authenticate(request,username=uname,password=pswd)
             if user:
                 login(request,user)
                 return redirect('home')
             else:
                 messages.error(request,"Login Failed ")
                 return redirect('log')
         return render(request,'login.html',{'form':form})
     
# class RegView(View):
#     def get(self,request):
#         form=Regform()      
#         return render(request,'reg.html',{'form':form})
#     def post(self,request):
#         formdata=Regform(data=request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             messages.success(request,'Registration Successfull!!')
#             return redirect('log')
#         messages.error(request,'Registration Failed!')
#         return render(request,'reg.html',{'form':formdata})
class RegView(CreateView):
    template_name='reg.html'
    form_class=Regform
    success_url=reverse_lazy('log')

    def form_valid(self, form):
        messages.success(self.request,"Successfully Registered")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'Registration Failed')
        return super().form_invalid(form)

class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('home')
