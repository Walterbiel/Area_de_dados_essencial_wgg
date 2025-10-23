import os
import pathlib

TECHS = ["Excel", "Power_BI", "SQL", "Python"]
LEVELS = ["Basico", "Intermediario", "Avancado"]
REQUIRED_SECTIONS = ["# ", "## Descrição", "## Código", "## Explicação passo a passo", "## Resultado esperado"]


def test_tecnologias_existem():
    for tech in TECHS:
        assert pathlib.Path(tech).is_dir(), f"Diretório {tech} não encontrado"


def test_niveis_e_quantidade_arquivos():
    for tech in TECHS:
        for level in LEVELS:
            level_path = pathlib.Path(tech) / level
            assert level_path.is_dir(), f"Subpasta {level_path} não encontrada"
            arquivos = sorted(p for p in level_path.glob("*.md"))
            assert len(arquivos) == 10, f"{level_path} deve conter 10 exemplos, encontrou {len(arquivos)}"


def test_conteudo_basico_padrao():
    for tech in TECHS:
        for level in LEVELS:
            for arquivo in (pathlib.Path(tech) / level).glob("*.md"):
                texto = arquivo.read_text(encoding="utf-8")
                for secao in REQUIRED_SECTIONS:
                    assert secao in texto, f"Seção '{secao}' ausente em {arquivo}"
                linhas = texto.splitlines()
                assert linhas[0].startswith("# "), f"Título principal faltando em {arquivo}"

