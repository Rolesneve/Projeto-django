from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .form import UsuarioForm


class UsuarioCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = UsuarioForm
    success_message = 'Usuário cadastrado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("usuarios")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários'
        context['descricao'] = 'Cadastro de Usuário'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UsuarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UsuarioForm
    success_message = 'Usuário atualizado com sucesso!'
    template_name = "formulario/form.html"
    success_url = reverse_lazy("usuarios")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários'
        context['descricao'] = 'Editar Usuário'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = "tabelas/usuarios.html"

class UsuarioDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_message = 'Usuário excluído com sucesso!'
    template_name = "formulario/excluir.html"
    success_url = reverse_lazy("usuarios")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UsuarioDelete, self).delete(request, *args, **kwargs)

class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name='usuarios/mudarSenha.html'
    from_class = PasswordChangeView
    success_message = 'Senha alterada com sucesso!'
    success_url = reverse_lazy('index')
