from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def toggle_theme(request):
    current = request.session.get('theme', 'dark')
    request.session['theme'] = 'bright' if current == 'dark' else 'dark'
    return redirect(request.META.get('HTTP_REFERER', 'home'))