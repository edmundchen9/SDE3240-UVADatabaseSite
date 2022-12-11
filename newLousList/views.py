from django.http import HttpResponseRedirect

# Create your views here.
# simple display of what is shown when the website first loads asks you to sign in
def index(request):
    return HttpResponseRedirect('/main/')
