from django.shortcuts import render, redirect

SECRET_PASSWORD = "12345"

def password_page(request):
    if request.method == "POST":
        entered_password = request.POST.get("password")

        if entered_password == SECRET_PASSWORD:
            return redirect("surprise")
        else:
            return render(request, "password.html", {"error": "Wrong password 😢"})

    return render(request, "password.html")


def surprise_page(request):
    return render(request, "home.html")

def gallery_page(request):
    return render(request, "gallery.html")

def special_page(request):
    return render(request, "special.html")

def poems_page(request):
    return render(request, "poems.html")

def letter_page(request):
    return render(request, "letter.html")