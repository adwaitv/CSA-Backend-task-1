from django.shortcuts import render


def reminder_list(request):
    return render(request, 'RemindersWebApp/reminder_list.html', {})
