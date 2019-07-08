
from django.urls import path, re_path, include
from alumni import views as alumniviews


urlpatterns = [
    path('', alumniviews.homepage.as_view(), name='homepage'),

    path('angkatan/', alumniviews.AngkatanList.as_view(), name='angkatan-list'),
    path('angkatan/<slug:Akademik>/<slug:Angkatan>/', alumniviews.AngkatanDetail.as_view(), name='angkatan-detail'),

    path('acara/', alumniviews.AcaraList.as_view(), name='acara-list'),
    path('acara/<str:slug>/', alumniviews.AcaraDetail, name='judulacara-list'),
    path('acara/<str:slug>/detail/', alumniviews.RincianList.as_view(), name='detail-list'),
    path('acara/<slug:Judul_Acara>/detail/<str:slug>/', alumniviews.RincianDetail, name='detail-detail'),

    path('berita/', alumniviews.BeritaList.as_view(), name='berita-list'),
    path('berita/<str:slug>/', alumniviews.BeritaDetail, name='berita-detail'),

    path('tentangkami/', alumniviews.AboutUS.as_view(), name='Tentang-Kami'),
]