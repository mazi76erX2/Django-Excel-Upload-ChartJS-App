from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.core.serializers.json import json, DjangoJSONEncoder

from .models import Accounting
from .forms import AccountingForm

from openpyxl import load_workbook


def extract_transaction_info(filename):
    workbook = load_workbook(filename=filename)
    sheet = workbook.active
    sheet.delete_rows(0)

    amounts_list = []
    dates_list = []
    for row in sheet.rows:
        if row[0]:
            amounts_list.append(row[1].value)
            dates_list.append(row[0].value)

    data_dict = {
        'amounts': amounts_list,
        'dates': dates_list
    }
    data_json = json.dumps(data_dict, cls=DjangoJSONEncoder)

    return data_json


def model_form_upload(request):
    if request.method == 'POST':
        form = AccountingForm(request.POST, request.FILES)
        if form.is_valid():
            new_accounting = form.save()
            excel_data = extract_transaction_info(
                filename=new_accounting.finances.name
            )
            new_accounting.finance_data = excel_data
            new_accounting.save()
            return redirect('chart', new_accounting.pk)
    else:
        form = AccountingForm()
    return render(request, 'form.html', {
        'form': form
    })


class ChartView(DetailView):
    template_name = 'chart.html'
    model = Accounting

    def get_context_data(self, **kwargs):
        context = super(ChartView, self).get_context_data(**kwargs)

        finance_data = json.loads(context['object'].finance_data)

        context['amounts'] = finance_data['amounts']
        context['dates'] = finance_data['dates']
        return context
