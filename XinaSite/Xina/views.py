from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Document, Attachment
from .forms import DocumentForm 

# TOD0:
# 6- add animations (last)
# add styling to CRUD pages/formating (Last)

@login_required(login_url='xina:login')
def mainPage(request):
    documents = Document.objects.all().order_by('-created_at')
    return render(request, 'Xina/main.html', {'documents': documents})

@login_required(login_url='xina:login')
def Create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()

            # Handle multiple attachments
            for file in request.FILES.getlist('files'):
                Attachment.objects.create(document=document, file=file)

            return redirect('xina:main')
    else:
        form = DocumentForm()

    return render(request, 'Xina/Create.html', {
        'form': form,
        'is_create_view': True # remove search bar in nav while in create view pass to nav.html under if condition.
    })

@login_required(login_url='xina:login')
def read(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    can_manage = doc.created_by == request.user

    attachments = []
    for f in doc.attachments.all():
        f.is_pdf = f.file.url.lower().endswith(".pdf")
        f.is_image = f.file.url.lower().endswith((".png", ".jpg", ".jpeg"))
        attachments.append(f)

    return render(request, 'Xina/read.html',{
        'update_mode': True,
        'doc': doc,
        'attachments': attachments,
        'can_manage': can_manage
    })

@login_required(login_url='xina:login')
def update(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)

    if doc.created_by != request.user:
        messages.error(request, "You do not have permission to edit this document.")
        return redirect('xina:read', doc_id=doc.id)

    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if not title:
            messages.error(request, "Title cannot be empty.")
            return redirect('xina:update', doc_id=doc.id)

        doc.title = title
        doc.content = content
        doc.save()

        # 2. Handle Deletion of Existing Attachments (if implemented in template)
        delete_file_ids = request.POST.getlist('delete_files')
        if delete_file_ids:
            # Assuming 'Attachment' is your model name
            Attachment.objects.filter(id__in=delete_file_ids).delete()
            # Note: Deleting the Attachment object typically handles deleting the file 
            # from storage if you use the signal method, but check your model's implementation.

        # 3. Handle Addition of NEW Attachments (THE MISSING LOGIC)
        # request.FILES.getlist('files') retrieves all newly uploaded files
        for file in request.FILES.getlist('files'):
            Attachment.objects.create(document=doc, file=file)

        messages.success(request, "Document updated successfully!")
        return redirect('xina:read', doc_id=doc.id)

    context = {
        'doc': doc,
        'attachments': doc.attachments.all(),
        'update_mode': True
    }
    return render(request, 'Xina/create.html', context)

@login_required(login_url='xina:login')
def delete_attachment(request, attachment_id):
    attachment = get_object_or_404(Attachment, id=attachment_id)
    document = attachment.document 

    if document.created_by != request.user:
        messages.error(request, "You do not have permission to delete this attachment.")
        return redirect('xina:read', doc_id=document.id)

    if request.method == 'POST':
        attachment.delete()
        messages.success(request, f"Attachment '{attachment.file.name.split('/')[-1]}' deleted successfully.")
    
    return redirect('xina:read', doc_id=document.id)

@login_required(login_url='xina:login')
def delete(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id) 
    if doc.created_by != request.user: # if not owner
        messages.error(request, "You do not have permission to delete this document.") 
        return redirect('xina:main')
    else:
        if request.method == 'POST':
            doc.delete()
            messages.success(request, "Document deleted successfully.")
    return redirect('xina:main')

def index(request):
    return render(request, 'Xina/index.html') 

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Authenticate credentials
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'Xina/Auth.html')

        # Login successful
        login(request, user)
        return redirect('xina:main')

    # GET request: render login form
    return render(request, 'Xina/Auth.html')

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        response = redirect('xina:index')
        response.delete_cookie('sessionid')
        return response
    return redirect('xina:index')

def SignUpPage(request):
    sign_up_active = True  # By default, show signup tab
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
        else:
            # Create user and log in
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            messages.success(request, f"Welcome, {username}! Your account has been created.")
            return redirect('xina:main')

    # GET request or failed POST: render the page with signup active
    return render(request, 'Xina/Auth.html', {'sign_up_active': sign_up_active})

