# Automatizar relatório com macro VBA

## Descrição
Crie uma macro simples para atualizar tabelas dinâmicas e exportar um PDF do relatório.

## Código
```vba
Sub AtualizaRelatorio()
    ' Atualiza todas as Tabelas Dinâmicas
    ThisWorkbook.RefreshAll
    ' Exporta a planilha ativa em PDF
    ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, Filename:="Relatorio_Vendas.pdf"
End Sub
```

## Explicação passo a passo
1. Pressione Alt+F11 para abrir o Editor VBA.
2. Insira um novo módulo e cole o código fornecido.
3. Feche o editor e crie um botão na planilha.
4. Associe o botão à macro AtualizaRelatorio.
5. Clique no botão para atualizar os dados e gerar o PDF automaticamente.

## Resultado esperado
Relatórios são atualizados e exportados com um único clique, economizando tempo em rotinas recorrentes.
