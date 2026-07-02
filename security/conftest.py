import sys
import os

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Hook de Pytest que se ejecuta al finalizar la sesión de pruebas.
    Si el estado de salida es 0 (todas las pruebas pasaron), imprime el banner premium.
    """
    if exitstatus == 0:
        # Truco mágico para forzar a la terminal de Windows a aceptar colores ANSI
        if sys.platform == "win32":
            os.system("") 

        # Colores ANSI para una apariencia de terminal hacker / premium
        VERDE_BRILLANTE = "\033[1;32m"
        FONDO_VERDE = "\033[1;42;30m"
        RESET = "\033[0m"

        print("\n" + "🟩" * 32)
        print(f" {FONDO_VERDE}  🚀 [ SUCCESS !!! ] ONIRIUM SECURITY GUARDRAILS PASSED  {RESET} ")
        print(f" {VERDE_BRILLANTE}👉 TDD Certification: 100% Secure & Cloud-Ready Environment{RESET}")
        print("🟩" * 32 + "\n")