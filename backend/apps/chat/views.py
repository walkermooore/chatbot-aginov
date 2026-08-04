from django.shortcuts import render

from apps.chat.services import ChatbotService


def home(request):
    result = None

    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        if question:
            result = ChatbotService().answer(question)

    return render(request, "chat/index.html", {"result": result})
