#include <SPI.h>
#include <LoRa.h>
#include <ArduinoJson.h>

int counter = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(12);
  LoRa.setSignalBandwidth(125E3);
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);

  StaticJsonBuffer<200> jsonBuffer;

  JsonObject& root = jsonBuffer.createObject();
  root["sensor"] = "中文";
  root["time"] = 1351824120;

  JsonArray& data = root.createNestedArray("data");
  data.add(48.756080);
  data.add(2.302038);

  // send packet
  LoRa.beginPacket();
  LoRa.print("01050");
  root.printTo(LoRa);
  LoRa.print("43524C46");
  //LoRa.print("hello ");
  //LoRa.print(counter);
  LoRa.endPacket();

  counter++;

  delay(5000);
}
