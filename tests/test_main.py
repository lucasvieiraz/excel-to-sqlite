import subprocess
import os

def test_script_roda_e_gera_arquivos():
    result = subprocess.run(
        ["python", "main.py"],
        capture_output=True,
        text=True
    )  
    assert result.returncode == 0, f"Erro ao executar script: {result.stderr}"

    assert os.path.exists("controle_2026.db")