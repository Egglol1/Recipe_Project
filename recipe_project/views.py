from django.shortcuts import render, redirect  
#Django authentication libraries           
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm    

def login_view(request):
  error_message = None
  form = AuthenticationForm()
  if request.method == 'POST':
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():                                
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      #use Django authenticate function to validate the user
      user=authenticate(username = username, password = password)
      if user is not None:
        #then use pre-defined Django function to login
        login(request, user)                
        return redirect('recipes:list')
      else:
        error_message ='ooops.. something went wrong'
  #prepare data to send from view to template
  context = {
    'form': form,
    'error_message': error_message
  }
  #load the login page using 'context' information
  return render(request, 'auth/login.html', context)

def logout_view(request):
  logout(request) #pre-defined Django function to logout
  return redirect('success')

def success_view(request):
  return render(request, 'recipes/success.html')