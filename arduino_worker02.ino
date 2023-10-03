/*
Arduino worker for RaspberryPi Pico HW Controller
arduino_worker2.ino connects to RaspberryPi pico HW via I2C
*/

# include <Wire.h>  // Includes the Wire library for I2C

//LED on pin 13
const int ledPin = 13 ;

void setup() {
Wire.begin(5);                /* join i2c bus as worker with address 5 */
Wire.onReceive(receiveEvent); /* register receive event when data is received*/

// Setup pin 13 as output and turn LED off
pinMode(ledPin, OUTPUT);
digitalWrite(ledPin, LOW);

}

//Function that executed whenever data is received from controller
void receiveEvent(int howMany) {
 while (0 <Wire.available()) {  // loop through all but the last
    char c = Wire.read();      /* receive byte as a character */
    digitalWrite(ledPin, c);
 }
}
void loop() {
  delay(100);
}