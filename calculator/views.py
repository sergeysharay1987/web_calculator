from django.shortcuts import render, redirect
from django.urls import reverse
from calculator.models import Exp
from calculator.forms import ExpForm


def get_expression(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bound_form = ExpForm(request.POST)
        # check whether it's valid:
        if bound_form.is_valid():
            expression = bound_form.cleaned_data['expression']
            result_of_expression = bound_form.cleaned_data['result_of_expression']
            d = {'expression': expression, 'result_of_expression': result_of_expression}
            bound_form = ExpForm(d)
            bound_form.save()
            return render(request, 'calculator/index.html', context={'form': bound_form})
        elif bound_form.errors:
            d = {'expression': request.POST['expression'], 'result_of_expression': ''}
            bound_form = ExpForm(d)
            return render(request, 'calculator/index.html', context={'form': bound_form})
    if request.method == 'GET':
        form = ExpForm()
        return render(request, 'calculator/index.html', context={'form': form})


def detail_of_expression(request, id):
    expression = Exp.expressions.get(id=id)
    return render(request, 'calculator/expression detail.html', context={'expression': expression})


def list_of_expressions(request):
    expressions = Exp.expressions.all()
    return render(request, 'calculator/database.html', context={'expressions': expressions})


def delete_expression(request, id):
    if request.method == 'GET':
        expression = Exp.expressions.get(id=id)
        return render(request, 'calculator/delete expression.html', context={'expression': expression})
    if request.method == 'POST':
        expression = Exp.expressions.get(id=id)
        expression.delete()
        return redirect(reverse('database'))




