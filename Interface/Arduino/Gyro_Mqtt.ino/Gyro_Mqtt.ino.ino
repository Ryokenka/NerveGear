#include <WiFi.h>
#include <PubSubClient.h> 
#include <Wire.h>//https://www.arduino.cc/en/reference/wire
#include <Adafruit_MPU6050.h>//https://github.com/adafruit/Adafruit_MPU6050
#include <Adafruit_Sensor.h>//https://github.com/adafruit/Adafruit_Sensor


//WIFI
const char* ssid = "CONECTMI";
const char* password = "12344562";
//MQTT
#define MQTT_BROKER       "54.38.241.241"
#define MQTT_BROKER_PORT  1883

;
WiFiClient espClient;
PubSubClient client(espClient);

//Acceleromètre
const int xThreshold = 3;
const int yThreshold = 3;
const int zThreshold = 10;
//Objects
Adafruit_MPU6050 mpu;

void setup() {

  Serial.begin(115200);
  Serial.println(F("Initialize System"));
  setup_wifi();
  setup_mqtt();
  setup_mpu();
}

void loop() {
  reconnect();
  char* data = readMPU();
  client.loop(); 
  mqtt_publish("MIN1",data);
  Serial.print("qqchose : ");
  Serial.println(data); delay(1000);
}


void setup_mpu(){
  if (!mpu.begin()) { // Change address if needed
 			Serial.println("Failed to find MPU6050 chip");
 			while (1) {
 					delay(10);
 			}
 	}
 	mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
 	mpu.setGyroRange(MPU6050_RANGE_250_DEG);
 	mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void setup_wifi(){
 WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

  while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(100);
  }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());
  
   
}

void setup_mqtt(){
  client.setServer(MQTT_BROKER, MQTT_BROKER_PORT);
  reconnect();

  
  client.publish("MIN1", "Hello from ESP32");
}

void reconnect(){
  while (!client.connected()) {
    Serial.println("Connection au serveur MQTT ...");
    if (client.connect("ESPClient")) {
      Serial.println("MQTT connecté");
    }
    else {
      Serial.print("echec, code erreur= ");
      Serial.println(client.state());
      Serial.println("nouvel essai dans 2s");
    delay(2000);
    }
  }
}

//Fonction pour publier un float sur un topic
void mqtt_publish(String topic, char* t){
  char top[topic.length()+1];
  topic.toCharArray(top,topic.length()+1);
  char t_char[50];
  String t_str = String(t);
  t_str.toCharArray(t_char, t_str.length() + 1);
  client.publish(top,t_char);
}


//Lire accéléromètre
char* readMPU() { /* function readMPU */
 	////Read acceleromter data
 	sensors_event_t a, g, temp;
 	mpu.getEvent(&a, &g, &temp);

  char* data;
  int x = a.acceleration.x;
  int y = a.acceleration.y;
  int z = a.acceleration.z;

  // vérifier si les valeurs d'accélération dépassent les seuils
  if (abs(x) > xThreshold) {
    ( x > 0) ? data = "DROITE": data="GAUCHE" ;
    
  }
  if (abs(y) > yThreshold) {
    ( y > 0) ? data= "AVANT": data= "ARRIERE" ;
  }
  if (abs(z) > zThreshold) {
    Serial.println("Accélération détectée sur l'axe z");
  }
  return data;

}