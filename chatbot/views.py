from django.shortcuts import render
from django.http import JsonResponse
import openai
from chatbotmodel.longresponses import get_response
# Create your views here.
# openai_api_key='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'
# openai.api_key=openai_api_key
# def ask_openai(message):
#     response=openai.Completion.create(
#         model="gpt-3.5-turbo",
#         prompt=message,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7,
    
#     )
#     print(response)

#     answer=response.choice[0].text.strip()
#     return answer

def get_response_here(message):
    return get_response(message)

def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response=get_response_here(message=message)
        return JsonResponse({
            'message':message,
            'response':response

        })

    return render(request,'chatbot.html')