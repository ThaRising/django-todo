from crispy_forms.layout import Submit
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import mixins, viewsets
from .schemas import serializers, models as todo_models
from django import forms
from crispy_forms.helper import FormHelper


class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_models.Model
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.add_input(Submit('submit', 'Submit'))


class TodoViewset(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = serializers.TodoSerializer
    queryset = todo_models.Model.objects.all()


class IndexView(View):
    def get(self, request):
        return render(request, "todo/index.html", {
            "models": todo_models.Model.objects.all(),
            "form": TodoForm()
        })

    def post(self, request):
        data = {
            "title": request.POST.get("title"),
            "description": request.POST.get("description")
        }
        serializer = serializers.TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return redirect(request.path)
