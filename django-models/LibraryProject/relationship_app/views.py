from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
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
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-checking functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")  # Ensure this path is present

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")  # Ensure this path is present

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")  # Ensure this path is present
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library  # Specify the model
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'