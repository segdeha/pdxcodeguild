# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User
from .models import Note
from django.shortcuts import redirect


from django.shortcuts import render
from django.template import Context, Template

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


# Below is the view function for the Notes model

def notes(request):
    if request.method == 'POST':
        print(request.POST.get("note"))
        print(request.POST.get("note_id"))
        n = Note(note=request.POST.get("note"), user=request.user)

        n.save()
        json_object = {'id': n.id}
        return JsonResponse(json_object)
    else:
        notes = Note.objects.filter(user=request.user)
        return render(request, 'notes.html', {"notes": notes})

# def search(request):
#    if request.method == 'POST':
#        query = request.POST['query']
#        results = Note.objects.filter(user=request.user, note__contains=query)
#        return  render(request, 'search.html', {'results':results})
#    return HttpResponse('Nothing to see here, Move along.')

# Below is the view function for the Note model for a new saved note

def note(request):
    note = Note.objects.filter(user=request.user)
    if request.method == 'POST':
        html = render_note(note)
        print(html)
    return render(request, 'note.html', {"note": note})


def base(request):
    """if it is a POST log user in else redirect back to '/'

    else check whether user is logged in  if logged in show notes
    else redirect to '/' """
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                notes = Note.objects.filter(user=user)
                notes_html = render_notes(notes)
                # Figure out how to grabe a single note from the database.
                note_html = render_note(notes)
                # html = notes_html + note_html
                html = '<section class="ui grid"><div id="notes-list" class="ui four wide column notes-list">' + notes_html + '</div>' + note_html + '</section>'
                return render(request, 'base.html', {"html": html})

        else:
            return redirect('/')

    else:       # if user types wrong login (Anonymous user)

        if '' == request.user.get_username():
            return redirect('/')        # redirect back to login screen

        else:
            notes = Note.objects.filter(user=request.user)
            notes_html = render_notes(notes)
            note_html = render_note(notes)
            html = '<section class="ui grid"><div id="notes-list" class="ui four wide column notes-list">'+notes_html+'</div>'+note_html+'</section>'
            return render(request, 'base.html', {"html": html})


def render_notes(notes):
    # pure function to hand a value to notes view

    with open('/Users/jefferybentley/Documents/pdxcodeguild/5. Capstone/browser_notes/browser_notes/templates/notes.html') as f:
        tmpl = Template(f.read())
        ctxt = Context({'notes': notes})
        return tmpl.render(ctxt)


def render_note(note):
    # get template as string
    with open('/Users/jefferybentley/Documents/pdxcodeguild/5. Capstone/browser_notes/browser_notes/templates/note.html') as f:
        tmpl = Template(f.read())
        ctxt = Context({'note': note})
        return tmpl.render(ctxt)


def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'my_login.html')
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...


def login(request):
    form = LoginForm()
    return render(request, 'my_login.html', {'form': form})








