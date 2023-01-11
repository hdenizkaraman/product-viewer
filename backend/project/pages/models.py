from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=240, verbose_name="Ürün İsmi", default="Yeni Ürün")
    slug = models.SlugField(max_length=240, unique=True, null=True)
    price = models.IntegerField(verbose_name="Ürün Fiyatı", blank=None, null=None)
    photo = models.CharField(max_length=800, verbose_name="Ürün Resim Linki", default="https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg")
    activity = models.BooleanField(verbose_name="Aktiflik Durumu")

    def __str__(self):
        return self.name
    
class SocialMedia(models.Model):
    name = models.CharField(max_length=500, verbose_name="Bootstrap Icon Kodu", default="<i class='bi bi-chat-square-quote-fill'></i>", blank=None)
    link = models.CharField(max_length=800, verbose_name="Sosyal Medya Linki", default="https://www.instagram.com/h.denizkaraman/", blank=None)
    activity = models.BooleanField(verbose_name="Aktiflik Durumu")

    def __str__(self):
        return self.name

class CompanyInfo(models.Model):
    def save(self):
        # count will have all of the objects from the Aboutus model
        count = CompanyInfo.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = CompanyInfo.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(CompanyInfo, self).save()
        elif save_permission:
            super(CompanyInfo, self).save()

    def has_add_permission(self):
        return CompanyInfo.objects.filter(id=self.id).exists()

    name = models.CharField(max_length=240, verbose_name="Şirket İsmi", default="Yeni Ürün", blank=None)
    photo = models.CharField(max_length=800, verbose_name="Şirket Resim Linki", default="https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg")

    def __str__(self):
        return self.name