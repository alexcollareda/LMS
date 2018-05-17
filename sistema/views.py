def login_user(request):
logout(request)
username = password = ''
form1 = RegistrationForm()
if request.POST:
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("redirect any whre u want")

return render(request, 'Write login templaye address')

def logout_user(request):
    user = request.user
    logout(request, user)
    return redirect("redirect any whre u want")
