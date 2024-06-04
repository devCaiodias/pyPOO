from pathlib import Path
from warnings import filters
import pandas as pd
import numpy as np

TIPO_DADOS = 'completo'

LINK_DADOS = {
    "amostra" : {
        "escola.parquet" : "C:\\Users\\caio\\pyPOO\cienciaDeDados\\amostra\\aquisicao\\escola.parquet",
        "ideb.parquet" : "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\amostra\\aquisicao\\ideb.parquet",
        "turma.parquet" : "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\amostra\\aquisicao\\turma.parquet"
    }, 
    "completo" : {
        "escola.parquet" : "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\dados\\completo\\aquisicao\\escola.parquet",
        "ideb.parquet" : "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\dados\\completo\\aquisicao\\ideb.parquet",
        "turma.parquet" : "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\dados\\completo\\aquisicao\\turma.parquet"
    }
}

vPATH_DADOS = Path(f"C:\\Users\\caio\\pyPOO\\cienciaDeDados\\dados{TIPO_DADOS}")

df = pd.read_parquet(vPATH_DADOS / "C:\\Users\\caio\\pyPOO\\cienciaDeDados\\dados\\amostra\\aquisicao\\escola.parquet", filters=[("ANO", "=", 2020)])

print(df)