
import subprocess

# Exécute la commande d'installation de Django en utilisant pip
subprocess.call(['pip', 'install', 'django'])
subprocess.call(['pip', 'install', 'reportlab'])
subprocess.call(['pip', 'install', 'xhtml2pdf'])
subprocess.call(['pip', 'install', 'tqdm'])
subprocess.call(['pip', 'install', 'gunicorn'])
