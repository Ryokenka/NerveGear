//Libraries
#include <Wire.h>//https://www.arduino.cc/en/reference/wire
#include <Adafruit_MPU6050.h>//https://github.com/adafruit/Adafruit_MPU6050
#include <Adafruit_Sensor.h>//https://github.com/adafruit/Adafruit_Sensor
#include <Streaming.h>
#include <WiFi.h>

const char* ssid = "CONECTMI";
const char* password = "12344562";

const int xThreshold = 3;
const int yThreshold = 3;
const int zThreshold = 10;



//Objects
Adafruit_MPU6050 mpu;
void setup() {
 	//Init Serial USB
 	Serial.begin(115200);
 	Serial.println(F("Initialize System"));
 if (!mpu.begin()) { // Change address if needed
 			Serial.println("Failed to find MPU6050 chip");
 			while (1) {
 					delay(10);
 			}
 	}
 	mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
 	mpu.setGyroRange(MPU6050_RANGE_250_DEG);
 	mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  WiFi.mode(WIFI_STA); //Optional
  WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

 // while(WiFi.status() != WL_CONNECTED){
 //     Serial.print(".");
 //     delay(100);
 // }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());
}


void loop() {
 	readMPU();
 	delay(100);
}

void readMPU( ) { /* function readMPU */
 	////Read acceleromter data
 	sensors_event_t a, g, temp;
 	mpu.getEvent(&a, &g, &temp);


 int x = a.acceleration.x;
  int y = a.acceleration.y;
  int z = a.acceleration.z;

  // vérifier si les valeurs d'accélération dépassent les seuils
  if (abs(x) > xThreshold) {
    ( x > 0) ? Serial.println("droite"): Serial.println("Gauche") ;
    
  }
  if (abs(y) > yThreshold) {
    ( y > 0) ? Serial.println("DEVANT"): Serial.println("DERRIERE") ;
  }
  if (abs(z) > zThreshold) {
    Serial.println("Accélération détectée sur l'axe z");
  }
  delay(1000);

}