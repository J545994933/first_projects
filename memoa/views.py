from django.shortcuts import render
from .models import MemoTemplateModel
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

from django.contrib.auth.models import User
# 不使用ModelViewSet视图时单独使用
# @api_view(http_method_names=['GET'])


# @action(methods=['GET'], detail=False) 使用类时在类中继承使用
@api_view(http_method_names=['POST'])
def post_data(request, *args, **kwargs):
    # @api_view(http_method_names=['POST'])
    data = request.data.get('data_id')
    # data = request.GET.get('data_id')
    print(data)
    return Response('successful')


@api_view(http_method_names=['POST'])
def memo_add(request):  # 增
    name = request.data.get('name')
    content = request.data.get('content')
    print(name, content)
    MemoTemplateModel.objects.create(memo_name=name, memo_tent=content)
    return Response('successful')


@api_view(http_method_names=['GET'])
def memo_delete(request):  # 删
    del_id = request.GET.get('id')
    memo_del = MemoTemplateModel.objects.get(pk=del_id)
    memo_del.delete()
    return Response('delete successful')


@api_view(http_method_names=['GET'])
def memo_update(request):  # 改
    # update_data_key = request.GET.keys()
    # update_data_value = request.GET.values()
    update_data_dict = request.GET.dict()
    update_id = update_data_dict.pop('id')
    MemoTemplateModel.objects.filter(pk=update_id).update(**update_data_dict)  # 更新
    return Response('successful')


@api_view(http_method_names=['GET'])
def memo_views(request):  # 查
    id = request.GET.get('id')
    return Response(MemoTemplateModel.objects.filter(pk=id).values())
