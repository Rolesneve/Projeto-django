from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .form import *
from .models import *


class AutorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Autor
    form_class = AutorForm
    success_message = 'Autor cadastrado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("autores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores'
        context['descricao'] = 'Cadastro de Autor(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class AutorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    success_message = 'Autor(a) atualizado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("autores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores'
        context['descricao'] = 'Editar Autor(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class AutorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Autor
    success_message = 'Autor(a) excluído com sucesso!'
    template_name = "formulario/excluir.html"
    success_url = reverse_lazy("autores")

class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "tabelas/autores.html"

#CURSO

class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Curso
    form_class = CursoForm
    success_message = 'Curso cadastrado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos'
        context['descricao'] = 'Cadastro de curso'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    success_message = 'Curso atualizado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("cursos")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos'
        context['descricao'] = 'Editar curso'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Curso
    success_message = 'Curso excluído com sucesso!'
    template_name = "formulario/excluir.html"
    success_url = reverse_lazy("cursos")

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "tabelas/cursos.html"

#ORIENTADOR

class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Orientador
    form_class = OrientadorForm
    success_message = 'Orientador cadastrado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores'
        context['descricao'] = 'Cadastro de orientador(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Orientador
    form_class = OrientadorForm
    success_message = 'Orientador(a) atualizado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores'
        context['descricao'] = 'Editar orientador(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Orientador
    success_message = 'Orientador(a) excluído com sucesso!'
    template_name = "formulario/excluir.html"
    success_url = reverse_lazy("orientadores")

class OrientadorList(ListView):
    model = Orientador
    template_name = "tabelas/orientadores.html"

#TCC


class TccCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tcc
    form_class = TccForm
    success_message = 'Tcc cadastrado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tccs'
        context['descricao'] = 'Cadastro de tcc'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tcc
    form_class = TccForm
    success_message = 'Tcc atualizado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tccs'
        context['descricao'] = 'Editar tcc'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tcc
    success_message = 'Tcc excluído com sucesso!'
    template_name = "formulario/excluir.html"
    success_url = reverse_lazy("index")


class TccDetalhe(DetailView):
    model = Tcc
    template_name = "detalhe/tcc.html"

class PaginaInicial(ListView):
    model = Tcc
    template_name = "tabelas/tccs.html"
