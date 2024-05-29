//Libraries
#include <Wire.h>//https://www.arduino.cc/en/reference/wire
#include <Adafruit_MPU6050.h>//https://github.com/adafruit/Adafruit_MPU6050
#include <Adafruit_Sensor.h>//https://github.com/adafruit/Adafruit_Sensor
#include <Streaming.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "CONECTMI";
const char* password = "12344562";

const char* mqtt_server= "54.38.241.241";
const int mqtt_port =1883;
long tps=0;


WiFiClient espClient;
PubSubClient client(espClient);


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

  setup_wifi();
  setup_mqtt();
  client.publish("MIN1", "Hello from ESP32");
}

void setup_mqtt(){
  client.setServer(mqtt_server, mqtt_port);
  reconnect();
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

void loop() {
 	data=readMPU();
 	delay(100);

  reconnect();
  client.loop(); 
  //On utilise pas un delay pour ne pas bloquer la réception de messages 
  if (millis()-tps>10000){
     tps=millis();
     float temp = random(30);
     mqtt_publish("MIN1",temp);
     Serial.print("qqchose : ");
     Serial.println(temp); 
   }
}

void setup_wifi(){
  //connexion au wifi
  WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

  while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(100);
  }
  Serial.println("");
  Serial.println("WiFi connecté");
  Serial.print("MAC : ");
  Serial.println(WiFi.macAddress());
  Serial.print("Adresse IP : ");
  Serial.println(WiFi.localIP());
}


//Fonction pour publier un float sur un topic
void mqtt_publish(String topic, float t){
  char top[topic.length()+1];
  topic.toCharArray(top,topic.length()+1);
  char t_char[50];
  String t_str = String(t);
  t_str.toCharArray(t_char, t_str.length() + 1);
  client.publish(top,t_char);
}


char* readMPU( ) { /* function readMPU */
 	////Read acceleromter data
 	sensors_event_t a, g, temp;
 	mpu.getEvent(&a, &g, &temp);
  reponse="";

 int x = a.acceleration.x;
  int y = a.acceleration.y;
  int z = a.acceleration.z;

  // vérifier si les valeurs d'accélération dépassent les seuils
  if (abs(x) > xThreshold) {
    ( x > 0) ? reponse="droite": reponse"Gauche" ;
  }
  if (abs(y) > yThreshold) {
    ( y > 0) ? reponse="DEVANT": reponse="DERRIERE" ;
  }
  if (abs(z) > zThreshold) {
    Serial.println("Accélération détectée sur l'axe z");
  }
  delay(1000);
  return reponse;
}