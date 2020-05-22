
from django.contrib.admin.views.decorators import staff_member_required
from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pygments.lexers import factor

from c_invoice.models import Factor, Records, Guest
from c_invoice.forms import FactorForm,RecordForm


def home(request):
    if not request.session.session_key:
        request.session.create()
    Guest.objects.get_or_create(session_id=request.session.session_key)
    return render(request, 'project/main.html')

def dashboard(request):
    factor=Factor.objects.filter(guest__session_id__exact=request.session.session_key)
    record = Records.objects.filter().all()
    return render(request, 'project/dashboard.html', {'factor': factor, 'record': record})
def create(request):
    if request.method == 'POST':
        form = FactorForm(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            g=Guest.objects.get(session_id__exact=request.session.session_key)
            x.guest=g
            x.save()

            return redirect('invoice:dash')
    else:
        form=FactorForm()
    return render(request, 'project/c_invoice.html', {'form':form, })
def read(request,nid):

    kk=Guest.objects.get(session_id__exact=request.session.session_key)
    try:
        factor =Factor.objects.filter(guest__session_id__exact=request.session.session_key,id=nid)

    except:
        return redirect('invoice:read',nid=factor.id)

    if not factor.get(guest__session_id__exact=kk.session_id):
        return HttpResponse("dgb")
    return render(request, 'project/read.html', {'factor': factor})

def r_create(request,nid):

    if request.method == 'POST':

        form = RecordForm(request.POST)
        if form.is_valid():
         p=form.save(commit=False)


         mo=Factor(nid)
         p.factor=mo
         p.save()
         return redirect('invoice:record',nid)
    else:
        form=RecordForm()
    xo = Records.objects.filter(factor=nid)
    return render(request, 'project/c_record.html', {'form':form, 'xo':xo})