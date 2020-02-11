from django import forms
from publicacoes import models
from perfis import models as perfis_models


class TweetAddForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = (
            'conteudo',
            'autor',
        )

        widgets = {
            'autor': forms.HiddenInput
        }

    def __init__(self, request, *args, **kwargs):
        super(TweetAddForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['autor'].queryset = perfis_models.Perfil.objects.filter(usuario=request.user)

    def clean(self):
        super(TweetAddForm, self).clean()
        autor = self.cleaned_data.get('autor')
        perfil = self.request.user.perfil_set.first()
        if autor != perfil:
            self.add_error('autor', 'O autor do tweet não é você!')

        return self.cleaned_data
