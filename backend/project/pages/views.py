from django.shortcuts import render
from . models import Product, CompanyInfo, SocialMedia
# Create your views here.
def index(request):
    compinfo = CompanyInfo.objects.all()
    social = SocialMedia.objects.all()
    context = {
        "compinfo":compinfo,
        "social":social,
    }
    return render(request, "index.html", context)

def products(request):
    productinfo = Product.objects.all()
    compinfo = CompanyInfo.objects.all()
    social = SocialMedia.objects.all()
    context = {
        "compinfo":compinfo,
        "social":social,
        "products":productinfo,
    }
    return render(request, "urunler.html", context)

def productdetail(request, productslug):
    try: productinfo = Product.objects.get(slug=productslug)
    except: return render(request, "notfound.html")
    context = {"product":productinfo,}
    return render(request, "urundetay.html", context)