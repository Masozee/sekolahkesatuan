from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
# Create your models here.
class Homepage(models.Model):
    #SLIDER ke -1
    Judul = models.CharField(max_length=50)
    Subjudul = models.CharField(max_length=50, blank=True, null=True)
    Link_to = models.TextField(default="#")
    Slide = models.ImageField(upload_to='homepage/')
    created = models.DateTimeField(auto_now=True)
    #SLIDER ke -2
    Judul_1 = models.CharField(max_length=50, default=True)
    Subjudul_1 = models.CharField(max_length=50, blank=True, null=True)
    Link_to_1 = models.TextField(default="#")
    Slide_1 = models.ImageField(upload_to='homepage/', default=True)
    created_1 = models.DateTimeField(auto_now=True)
    #SLIDER ke -3
    Judul_2 = models.CharField(max_length=50, default=True)
    Subjudul_2 = models.CharField(max_length=50, blank=True, null=True)
    Link_to_2 = models.TextField(default="#")
    Slide_2 = models.ImageField(upload_to='homepage/',default=True)
    created_2 = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.Judul) 

    class Meta:
        verbose_name_plural = 'Homepage'

class Header (models.Model):
    Header_Date = models.DateField(auto_now=False)
    Acara = models.ImageField(upload_to='sitesettings/')
    Berita = models.ImageField(upload_to='sitesettings/')
    Rincian_Berita = models.ImageField(upload_to='sitesettings/')

    def __str__(self):
        return str(self.Header_Date) 

    class Meta:
        verbose_name_plural = 'Header Settings'

class TahunAngkatan(models.Model):
    JENIS_SEKOLAH = (
        ('Toddler', 'Toddler'),
        ('SD', 'SD'),
        ('SMP', 'SMP'),
        ('SMA', 'SMA'),
        ('SMK', 'SMK')
    )

    Angkatan = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999)])
    Akademik = models.CharField(max_length=7, choices=JENIS_SEKOLAH)
    Keterangan = models.TextField(blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ("Tahun Angkatan")

    def __str__(self):
        return str(self.Angkatan)

class FotoAngkatan(models.Model):
    Angkatan = models.ForeignKey('TahunAngkatan', on_delete=models.CASCADE)
    Gambar = models.ImageField(upload_to="Angkatan/")
    Keterangan = models.TextField(blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Angkatan) 
    
    class Meta:
        verbose_name_plural = ("Foto Angkatan")
    
class NamaAlumni (models.Model):
    JENIS_SEKOLAH = (
        ('Toddler', 'Toddler'),
        ('SD', 'SD'),
        ('SMP', 'SMP'),
        ('SMA', 'SMA'),
        ('SMK', 'SMK')
    )

    Nama = models.CharField(max_length=50)
    NIS = models.IntegerField(blank=True, null=True)
    Alamat = models.TextField(blank=True, null=True)
    Akademik = models.CharField(max_length=7, choices=JENIS_SEKOLAH, default=True)
    Angkatan = models.ForeignKey('TahunAngkatan', on_delete=models.CASCADE)
    No_Telp = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999999)])
    Foto = models.ImageField( upload_to='Alumni/', blank=True, null=True)
    Keterangan = models.TextField(blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ("Alumni")

    def __str__(self):
        return self.Nama +" "+ str(self.Angkatan)

class Acara(models.Model):
    Nama_Acara = models.CharField(max_length=100)
    slug = models.SlugField(default='', editable=False, max_length=140)
    Waktu_Mulai = models.DateField()
    Waktu_Selesai = models.DateField()
    Tempat = models.TextField(blank=True, null=True)
    Foto = models.ImageField(upload_to="Acara/", blank=True, null=True)
    Keterangan = RichTextField()
    Date_Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nama_Acara

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('berita', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.Nama_Acara
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = ("Acara")

class RincianAcara(models.Model):
    Judul_Acara = models.ForeignKey('Acara', on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=140)
    Rincian_Acara = models.CharField(max_length=100)
    Waktu_Mulai = models.DateTimeField()
    Waktu_Selesai = models.DateTimeField()
    Foto = models.ImageField( upload_to="Acara/")
    Keterangan =RichTextField()
    Date_Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Rincian_Acara

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('judulacara-list', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.Rincian_Acara
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = ("Rincian Acara")

class Berita(models.Model):
    Judul = models.CharField(max_length=150)
    slug = models.SlugField(default='', editable=False, max_length=140)
    Tanggal = models.DateField(auto_now_add=True)
    Isi = RichTextField()
    Gambar = models.ImageField( upload_to="Berita/", blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Judul


    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('berita', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.Judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = ("Berita")
