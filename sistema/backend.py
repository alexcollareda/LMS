def entrar(request):
    context = {}
    if request.method == "POST":
        if autenticar(request):
            return redirect("/")
        else:
            context["erro"] = "Problemas no login"
            return render(request, "home.html", context)
