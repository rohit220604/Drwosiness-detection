// Define the pin where the buzzer is connected
#include <Servo.h>
const int buzzerPin = 9;

Servo myservo;

void setup() {
  // Set the buzzer pin as an output
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
  myservo.attach(8);
}

void loop() {

  if (Serial.available()) {
    char command = Serial.read();  // Read the command from the serial port

    if (command == '1') {
      myservo.write(90);  // Move the servo to 90 degrees
    }

    else if (command == '2') {
      myservo.write(45);  // Move the servo back to 45 degrees
    }
    
    else if (command == '0') {
      myservo.write(0);  // Move the servo back to 0 degrees
    }
  
    
    if (command == '1') {
        noTone(buzzerPin);
        tone(buzzerPin, 1000);  // 1000 Hz tone
//        delay(1000);  // Wait for 1 second
  
  // Stop the tone
//        noTone(buzzerPin);
//        delay(100);  // Wait for 1 sec
    }

    else if (command == '2') {
       noTone(buzzerPin);
       tone(buzzerPin, 1000);  // 1000 Hz tone
//       delay(1000);  // Wait for 1 second
  
  // Stop the tone
//       noTone(buzzerPin);
//       delay(100);  // Wait for 1 sec // Move the servo back to 0 degrees
    }
    
    else if (command == '0') {
         noTone(buzzerPin);
//       tone(buzzerPin, 1000);  // 1000 Hz tone
//       delay(1000);  // Wait for 1 second
  
  // Stop the tone
//         noTone(buzzerPin);
//       delay(100);  // Wait for 1 sec  // Move the servo back to 0 degrees
    }
  }
 
}


 // Play a tone on the buzzer
 
