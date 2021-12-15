pip install urllib3 uuid

Ensure the request is strictly POST and not GET

Create a short 5 letter code slicing a UUID string

Validate it using urllib3 and return the user the newly generated uuid concatenated with the link in the template (Jinja2 Python format)

Also we have the store the values in the cookies (browser local storage)

Insert the values into the database using insert_one(<schema>) command

Redirect user to the net page based on whether the response is valid of not

In views.py, the shorten method:

def short(request):    
    if request.method == 'POST':
        user = request.COOKIES.get('key')
        url = request.POST['link']
        if url.find('<name of your domain>') != -1:
            return render(request, 'index.html', {'status': 'Funny'})  #dynamic data onto your HTML template
        http = urllib3.PoolManager()
        valid = False
        if url.startswith("http"):            
            url = url    
        else:
            url = "http://"+url
        
        try:
            ret = http.request('GET',url)
            if ret.status == 200:
                valid = True
        except Exception as e:
            valid = False
            
        if valid == True:
            new_url = str(uuid.uuid4())[:5]
            surl = "<name of your domain>"+new_url
            sch = {'uid' : user, 'link' : url, 'new' : surl}
            coll.insert_one(sch)
            return render(request, 'short.html', {'user':user, 'url': url, 'new':surl})           #dynamic data onto your HTML template
        else:
            return render(request, 'index.html', {'status': False})
    return redirect('/')
in URLapp/urls.py

urlpatterns = [
    path('',views.index, name="index"),
    path('s/short',views.short, name="short")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    # loads the static files without trouble

References
Inserting Data
Setting UUID
More about cookies

Expected Outcome:
Your database should now have your inserted links along with the newly generated links identifiable by an unique ID. Upon clicking the submit button, you should be redirected to a new template displaying the new link (shown below in my case) and the mailing feature that we are going to implement next.
