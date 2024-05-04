from django.shortcuts import render

from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create your views here.
def home(request):
   if request.method == "POST":
      input_text = request.POST.get('input_text')
      Summarizer_ans = summarizer(input_text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
      return render(request,'home.html',{"Summarizer_ans":Summarizer_ans})
   return render(request,'home.html')