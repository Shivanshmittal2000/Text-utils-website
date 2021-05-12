from django.http import HttpResponse
from django.shortcuts import render # this is for using templates
def index(request):
    # file1=open("textutility/one.txt",'r')
    # return HttpResponse(file1.read())
    # param={'name':'Shivansh','place':'India'}
    # return render(request,'index.html',param)
    return render(request,'index.html')
def webpages(request):
    html=''' <b> 5 major e-commerce websites </b>
     <h2>billions of people purchase online from these site</h2> 
    <a href="https://www.amazon.in/"> Amazon </a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.myntra.com/">Myntra</a><br>
             <a href="https://paytmmall.com/">Paytm mall </a><br>
             <a href="https://www.alibaba.com/"> Alibaba </a>'''
    return HttpResponse(html)
def home(request):
    html1 = ''' <b> Text utility websites </b>
                
                <a href="http://127.0.0.1:8000/removepunc">removepunc</a><br>
                <a href="http://127.0.0.1:8000/newlineremove">newlineremove</a><br>
                <a href="http://127.0.0.1:8000/charcount">Charcount</a><br>
                 <a href="http://127.0.0.1:8000/spaceremover">Space remover </a><br>
                 <a href="http://127.0.0.1:8000/capitalizefirst"> capitalize first </a>'''
    return HttpResponse(html1)
def removepucs(request):
    html2='''  
    <a href="http://127.0.0.1:8000/home"><-</a><br>
    Remove puncs<br>'''
    print(request.GET.get('text','default'))
    return HttpResponse("Remove puncs <a href='/'> back</a>")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepuc= request.POST.get("removepunc",'off')
    iscaptil=request.POST.get('iscapitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    print(removepuc)
    print(djtext)
    chagingvar=djtext
    analyzed=""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepuc=='on':
        for char in chagingvar:
            if char not in punctuations:
                analyzed+=char
        chagingvar=analyzed
        # params={'purpose':'Remove puc','analyzed_text': analyzed}
        # return render(request,'analyze.html',params)
    if iscaptil=='on':
        analyzed=""
        for char in chagingvar:
            analyzed+=char.upper()
        chagingvar=analyzed
        # params = {'purpose': 'make capitalize', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',params)
    if newlineremover == 'on':
        string=""
        for char in chagingvar:
            if char!='\n' and char!='\r':
                string+=char
        chagingvar=string
        print(chagingvar)
        # params = {'purpose': 'make capitalize', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',params)
    if spaceremover == 'on':
        print(chagingvar)
        print("he;llo")
        analyzed=""
        for i in range(len(chagingvar)-1):
            if chagingvar[i]==" " and chagingvar[i+1]==" ":
                pass
            else :
                analyzed+=chagingvar[i]
        chagingvar=analyzed
        print(chagingvar)
        # params = {'purpose': 'make capitalize', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if charcount=='on':
        dict={}

        for char in chagingvar:
            dict[char]=dict.get(char,0)+1
        chagingvar=dict
        # params = {'purpose': 'make capitalize', 'analyzed_text': dict}
        # return render(request, 'analyze.html', params)
    if removepuc!='on' and spaceremover!="on" and charcount!='on' and iscaptil!='on' and spaceremover!='on':
        return HttpResponse("Select at least one operation")
    # else :
    #     return HttpResponse('error')
    param={'analyzed_text':chagingvar}
    return render(request,'analyze.html',param)
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def Capitalizefirst(request):
    html3 = '''  
        <a href="http://127.0.0.1:8000/home"><-</a><br>
        Capitalize first<br>'''
    return HttpResponse(html3)
def newlineremove(request):
    html4 = '''  
        <a href="http://127.0.0.1:8000/home"><-</a><br>
        newline remove<br>'''
    return HttpResponse(html4)
def Spaceremover(request):
    html5 = '''  
        <a href="http://127.0.0.1:8000/home"><-</a><br>
        space remover<br>'''
    return HttpResponse(html5)
def Charcount(request):
    html6 = '''  
            <a href="http://127.0.0.1:8000/home"><-</a><br>
            Char count<br>'''
    return HttpResponse(html6)
