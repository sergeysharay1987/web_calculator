import pytest
from django.test import Client
from django.urls import reverse, resolve
from settings import BASE_DIR
from calculator.views import *
from calculator.validators import *


# Create your tests here.


class TestUrls:

    def test_path_of_index_page(self):
        path = reverse('index')
        # print(resolve(path).view_name)
        assert resolve(path).view_name == 'index'

    def test_path_of_database_page(self):
        path = reverse('database')
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'database'

    def test_path_of_detail_page(self):
        path = reverse('details', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'details'

    def test_path_of_delete_page(self):
        path = reverse('delete', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'delete'


class TestViews:
    client = Client()
    paths = {'index': reverse('index'),
             'database': reverse('database'),
             'delete ': reverse('delete', kwargs={'id': 5})}
    key_of_context_of_index_page = 'form'
    key_of_context_of_database_page = 'expressions'
    key_of_context_of_exp_detail_page = 'expression'
    key_of_context_of_delete_page = 'expression'

    # def test_calculate_expression(self):
    #     pytest.raises(ValidationError, calculate_expression, '1/0')
    #     # pytest.raises(NameError, calculate_expression, '1/a')

    def test_equlity_key_of_context_of_index_page_with_template(self):
        index_page = open(BASE_DIR + '/calculator/templates/calculator/index.html', 'r')
        assert self.key_of_context_of_index_page in index_page.read()

    def test_equlity_key_of_context_of_database_page_with_template(self):
        database_page = open(BASE_DIR + '/calculator/templates/calculator/database.html', 'r')
        assert self.key_of_context_of_database_page in database_page.read()

    def test_equlity_key_of_context_of_exp_detail_page_with_template(self):
        exp_detail_page = open(BASE_DIR + '/calculator/templates/calculator/expression detail.html', 'r')
        assert self.key_of_context_of_exp_detail_page in exp_detail_page.read()

    def test_equlity_key_of_context_of_exp_delete_page_with_template(self):
        exp_delete_page = open(BASE_DIR + '/calculator/templates/calculator/delete expression.html', 'r')
        assert self.key_of_context_of_delete_page in exp_delete_page.read()

    def test_key_of_context_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        assert self.key_of_context_of_index_page in response.context

    def test_key_of_context_of_database_page(self):
        path = '/database/5/delete/'
        response = self.client.get(path)
        assert self.key_of_context_of_database_page in response.context

    def test_key_of_context_of_delete_page(self):
        path = self.paths['delete']
        response = self.client.get(path)
        print(response.context)
        assert 'expression' in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert self.key_of_context_of_database_page in response.context

    def test_template_using_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        assert 'calculator/index.html' in [template.name for template in response.templates]

    @pytest.mark.django_db
    def test_template_using_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert 'calculator/database.html' in [template.name for template in response.templates]

    # def test_post_get_expression(self):
    #     path = self.paths['index']
    #     response = self.client.post(path, data={'expression': '15/3', 'result_of_expression': ''})
    #     assert response.context['result_of_expression'] ==


# class TestModels:
#
#     def test_check_expression(self):
#         pytest.raises(ValidationError, check_expression, '1/0')
#         pytest.raises(ValidationError, check_expression, '1/a')
#         pytest.raises(ValidationError, check_expression, '1//')
#         pytest.raises(ValidationError, check_expression, '1/')
#         pytest.raises(ValidationError, check_expression, '[]')
#         pytest.raises(ValidationError, check_expression, '[')
#         pytest.raises(ValidationError, check_expression, 'print(""Hello")')
#         pytest.raises(ValidationError, check_expression, '')
#         pytest.raises(ValidationError, check_expression, '1**')
