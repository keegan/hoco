from django.shortcuts import render, redirect
from django.urls import reverse
from .things import *
from datetime import datetime

# Create your views here.
def index(request):
    if "admin" in request.session and request.session["admin"] == True:
        now = datetime.now()
        rally = max(day for day in week if dates[day] < now)
        return render(
            request, 
            "index.html",
            {
                "theme": rally_themes[rally],
                "subtheme": rally_subthemes[rally],
                "link": rally_links[rally],
            },
        )
    else:
        request.session.flush()
        return render(request, "fail.html")
