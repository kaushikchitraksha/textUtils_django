from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("Heloo This View is about view")

def remove_punction(extracted_text,analyed_text):
    punctutions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if extracted_text != 'None':
            for char in extracted_text:
                if char not in punctutions:
                    analyed_text = analyed_text + char
    return analyed_text

def capitalize_fun(extracted_text,analyed_text):
    if extracted_text != 'None':
            for char in extracted_text:
                analyed_text = analyed_text + char.upper()
    return analyed_text

def Char_count_fun(extracted_text,count):
    if extracted_text != 'None':
        for char in extracted_text:
            count= count+1
    return count
    
    

def analyzetext(request):
    remove_punc = request.POST.get('removepunc','off')
    print(remove_punc)
    capitalize = request.POST.get('capitalize','off')
    print(capitalize)
    char_count = request.POST.get('char_count','off')
    print(char_count)
    extracted_text = request.POST.get('text','None')
    count = 0
    print(extracted_text)
    analyed_text = ""
    if remove_punc != 'off' and capitalize != 'off':
        print("Inside remove punc and cap block")
        analyed_text_1 =  remove_punction(extracted_text,analyed_text)
        analyed_text = capitalize_fun(analyed_text_1,analyed_text)
        params = {'purpose':'Remove Punctation and Capitalize text','analyzed_text':analyed_text}
        return render(request,'analyzetext.html',params)
    
    elif remove_punc != 'off' and capitalize == 'off':
         print("Inside remove punc block")
         analyed_text =  remove_punction(extracted_text,analyed_text)
         params = {'purpose':'Remove Punctation','analyzed_text':analyed_text}
         return render(request,'analyzetext.html',params)
    elif remove_punc == 'off' and capitalize != 'off':
         print("Inside cap block")
         analyed_text =  capitalize_fun(extracted_text,analyed_text)
         params = {'purpose':'Capitalize text','analyzed_text':analyed_text}
         return render(request,'analyzetext.html',params)
    elif remove_punc == 'off' and capitalize == 'off' and char_count != 'off':
         print("Inside char count block")
         count = Char_count_fun(extracted_text,count)
         params = {'purpose':'Character Count','analyzed_text':count}
         return render(request,'analyzetext.html',params)
    else:
         return HttpResponse("No Feature is selected so we cant do anything")
                
    



# def WebSite_link(request):
#     return HttpResponse('''<p><a href="https://www.aajtak.in/">Aaj Tak </a> </p>
#                             <p><a href="https://www.youtube.com/">YouTube </a> </p>
#                             <p><a href="https://github.com/">GitHub </a> </p>''')

# def link_home(request):
#     return HttpResponse('''<p> Hello Gyus This is link home View.  <a href="/website_link/">Go to Websites link </a> </p>''')
