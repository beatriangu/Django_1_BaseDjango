import logging
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from . import forms
from datetime import datetime

def index(request: HttpRequest):
    logger = logging.getLogger('history')
    logging.basicConfig(format='%(asctime)s %(message)s')

    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            now = datetime.now()
            entry = f"{form.cleaned_data['history']} ({now.strftime('%d/%m/%Y, %H:%M:%S')})"
            logger.info(entry)
            with open(settings.HISTORY_LOG_FILE, 'a') as f:
                f.write(entry + '\n')
        return redirect('/ex02')

    try:
        with open(settings.HISTORY_LOG_FILE, 'r') as f:
            histories = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        histories = []

    return render(request, 'ex02/index.html', {'form': forms.History(), 'histories': histories})
