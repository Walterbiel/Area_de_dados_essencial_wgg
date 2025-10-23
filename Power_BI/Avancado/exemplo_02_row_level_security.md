# Implementar Row-Level Security (RLS)

## Descrição
Ensina a limitar o acesso dos usuários a dados específicos usando funções DAX de segurança.

## Código
```dax
[Região] = LOOKUPVALUE(DimUsuario[RegiaoPermitida]; DimUsuario[Email]; USERPRINCIPALNAME())
```

## Explicação passo a passo
1. Crie uma tabela DimUsuario com e-mails e regiões permitidas.
2. No Power BI Desktop, acesse Modelagem > Gerenciar Funções.
3. Crie função 'RegiaoRestrita' com o filtro DAX fornecido.
4. Teste a função usando 'Exibir como função'.
5. Publique o relatório e atribua usuários à função no serviço.

## Resultado esperado
Cada usuário visualiza apenas os dados da região autorizada, garantindo segurança e conformidade.
