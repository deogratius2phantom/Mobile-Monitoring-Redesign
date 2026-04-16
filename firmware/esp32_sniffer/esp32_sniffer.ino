#include <WiFi.h>
#include <WiFiUdp.h>
#include <esp_wifi.h>

// -----------------------------
// User configuration
// -----------------------------
static const char* WIFI_SSID = "YOUR_WIFI_SSID";
static const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
static const char* SERVER_IP = "192.168.1.100"; // Raspberry Pi IP
static const uint16_t SERVER_PORT = 5005;
static const char* NODE_ID = "node-1";

// Channel hopping
static const uint8_t MIN_CHANNEL = 1;
static const uint8_t MAX_CHANNEL = 13;
static const uint32_t CHANNEL_HOP_INTERVAL_MS = 250;

WiFiUDP udp;
uint8_t currentChannel = MIN_CHANNEL;
uint32_t lastHopMs = 0;

static String macToString(const uint8_t* mac) {
  char buf[18];
  snprintf(buf, sizeof(buf), "%02X:%02X:%02X:%02X:%02X:%02X",
           mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  return String(buf);
}

// Promiscuous callback for captured 802.11 frames.
void snifferCallback(void* buf, wifi_promiscuous_pkt_type_t type) {
  if (type != WIFI_PKT_MGMT && type != WIFI_PKT_DATA) {
    return;
  }

  auto* pkt = reinterpret_cast<wifi_promiscuous_pkt_t*>(buf);
  const int8_t rssi = pkt->rx_ctrl.rssi;
  const uint8_t* payload = pkt->payload;

  // IEEE 802.11 MAC header source MAC starts at offset 10 (Address2).
  const uint8_t* srcMac = payload + 10;
  String srcMacStr = macToString(srcMac);

  uint32_t ts = millis();
  String json = "{";
  json += "\"node_id\":\"" + String(NODE_ID) + "\",";
  json += "\"mac\":\"" + srcMacStr + "\",";
  json += "\"rssi\":" + String(rssi) + ",";
  json += "\"channel\":" + String(currentChannel) + ",";
  json += "\"ts_ms\":" + String(ts);
  json += "}";

  udp.beginPacket(SERVER_IP, SERVER_PORT);
  udp.print(json);
  udp.endPacket();
}

static void connectWifi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  uint8_t retries = 0;
  while (WiFi.status() != WL_CONNECTED && retries < 20) {
    delay(500);
    retries++;
  }
}

void setup() {
  Serial.begin(115200);
  delay(500);

  connectWifi();
  udp.begin(0); // ephemeral local UDP port

  // Start promiscuous sniffing.
  esp_wifi_set_promiscuous(false);
  esp_wifi_set_channel(currentChannel, WIFI_SECOND_CHAN_NONE);
  esp_wifi_set_promiscuous_rx_cb(&snifferCallback);
  esp_wifi_set_promiscuous(true);

  Serial.println("ESP32 sniffer started");
}

void loop() {
  // Keep station connected when possible.
  if (WiFi.status() != WL_CONNECTED) {
    connectWifi();
  }

  // Channel hopping across channels 1..13.
  uint32_t now = millis();
  if (now - lastHopMs >= CHANNEL_HOP_INTERVAL_MS) {
    lastHopMs = now;
    currentChannel++;
    if (currentChannel > MAX_CHANNEL) {
      currentChannel = MIN_CHANNEL;
    }
    esp_wifi_set_channel(currentChannel, WIFI_SECOND_CHAN_NONE);
  }

  delay(10);
}
