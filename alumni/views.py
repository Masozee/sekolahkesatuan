from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import TahunAngkatan, Acara, Berita, RincianAcara,Homepage



# Create your views here.

class homepage(TemplateView):
    template_name = "Homepage/index.html"

    def get_context_data(self, **kwargs):
         context = super(homepage, self).get_context_data(**kwargs)
         context['Slide'] = Homepage.objects.all()
         context['berita'] = Berita.objects.all().order_by('-Tanggal').distinct()[:3]
         context['acara'] = Acara.objects.all().order_by('-Waktu_Mulai').distinct()[:3]
         return context


class AcaraList(ListView):
   model                = Acara
   queryset             = Acara.objects.all()
   template_name        = "Acara/list.html"
   context_object_name  = "acara"
   paginate_by          = 10
   ordering             = ['-Waktu_Mulai']


def AcaraDetail(request, slug):
   acara = Acara.objects.get(slug=slug)
   context = {
        "acara": acara,
    }
   return render(request, 'Acara/detail.html', context)

class RincianList(ListView):
   model                = RincianAcara
   queryset             = RincianAcara.objects.all()
   template_name        = 'RincianAcara/list.html'
   context_object_name  = 'Rinci'
   paginate_by          = 10
   ordering             = ['-Judul_Acara']

def RincianDetail(request, slug):
   Rincian = RincianAcara.objects.get(slug=slug)
   context = {
        "Rincian": Rincian,
    }
   return render(request, 'RincianAcara/detail.html', context)

class BeritaList(ListView):
   model                = Berita
   queryset             = Berita.objects.all()
   template_name        = 'Berita/list.html'
   context_object_name  = 'berita'
   paginate_by          = 10
   ordering             = ['-Tanggal']


def BeritaDetail(request, slug):
   berita = Berita.objects.get(slug=slug)
   context = {
        "berita": berita,
    }
   return render(request, 'Berita/detail.html', context)

class AngkatanList(ListView):
   model                = TahunAngkatan
   queryset             = TahunAngkatan.objects.all()
   template_name        = 'Angkatan/list.html'
   context_object_name  = 'angkatan'
   paginate_by          = 10
   ordering             = ['-angkatan']

class AngkatanDetail(DetailView):
    model               = TahunAngkatan
    template_name       = 'Angkatan/detail.html'
    slug_field          = 'Angkatan'
    slug_url_kwarg      = 'Angkatan'

class AboutUS(TemplateView):
    template_name       = "About/about.html"
