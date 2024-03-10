from django.shortcuts import render
from .scrape.scrape import Scrape
from .forms import UploadUrl

# Create your views here.
def scrape_web_page(request):
    if request.method == "POST":
        form = UploadUrl(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            converter = Scrape()
            scraped_text = converter.scrape(url)
            with open(scraped_text, "r", encoding="utf-8") as file:
                text_content = file.read()
            context = {"scraped_text": text_content}
            return render(request, "scraped_text.html", context)
    else:
        form = UploadUrl()
    return render(request, "url.html", {"form": form})