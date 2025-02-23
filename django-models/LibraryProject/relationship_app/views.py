from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.forms import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library  # Specify the model
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('list_books')  # Redirect to a desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

