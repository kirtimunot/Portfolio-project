from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blogs=Blog.objects
    return render(request,"blog/allblogs.html",{'blogs':blogs})

def details(request,blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,"blog/details.html",{'detail':detailblog})


'''home.html
  {%for job in jobs.all %}
      <div class="row">
        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <img class="card-img-top" src="{{job.image.url}}"/>
            <div class="card-body">
              <p class="card-text">{{job.summary}}</p>
            </div>
          </div>
        </div>
        {%endfor%}'''