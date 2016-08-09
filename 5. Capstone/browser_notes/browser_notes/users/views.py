# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm
from .models import User
from .models import Note


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
        if request.POST.get("note_id") == "newnote":
            # create a new note

            print(request.POST.get("note"))
            print(request.POST.get("note_id"))
            n = Note(note=request.POST.get("note"), user=request.user)

            n.save()
            json_object = {'id': n.id}
            return JsonResponse(json_object)


        else:
            # update existing note
            print("test")
            note = Note.objects.get(id=request.POST.get("note_id"))
            note.note = request.POST.get("note")  # change field
            note.save()  # this will update only
            return JsonResponse({'id': note.id})

    else:

        notes = Note.objects.filter(user=request.user).order_by('-modified')
        return render(request, 'notes.html', {"notes": notes})


# Below view for future work on search
# def search(request):
#    if request.method == 'POST':
#        query = request.POST['query']
#        results = Note.objects.filter(user=request.user, note__contains=query)
#        return  render(request, 'search.html', {'results':results})
#    return HttpResponse('Nothing to see here, Move along.')

# Below is the view function for the Note model for a new saved note

def note(request):
    note = Note.objects.filter(id=request.GET.get("note_id")).values("note")
    print(request.GET.get("note_id"))
    print(note)
    # if request.method == 'POST':
    #     html = render_note(note)
    #     print(html)
    return JsonResponse({'note': note[0]["note"]})


def base(request):
    user = request.user
    if user is not None:
        notes = Note.objects.filter(user=user)
        notes_html = render_notes(notes)
        # Figure out how to grab a single note from the database.
        note_html = render_note(notes)
        # html = notes_html + note_html
        html = '<section class="ui grid"><div id="notes-list" class="ui four wide column notes-list">' + notes_html + '</div>' + note_html + '</section>'
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




def login_form(request):
    form = LoginForm()
    return render(request, 'my_login.html', {'form': form})








