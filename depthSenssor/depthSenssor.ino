q#include <SPI.h>
#include <ms5540c.h>

ms5540c sensor;

void setup() {
    Serial.begin(9600);
    SPI.begin(); // Sensor doesn't start SPI communication itself so we're to enable it ourselves
    // sensor.init();
}

void loop() {
    const long temp_raw = sensor.getTemperature(); // Temperature in tenths of the deg C
    const long prs_raw = sensor.getPressure(); // pressure in tenths of a mbar (because of the sensor precision)
    Serial.print("Temperature: ");   Serial.print(conv::degC(temp_raw));                     Serial.println(" C");
    Serial.print("Pressure: ");     Serial.print(conv::mbar(prs_raw));                       Serial.println(" mbar");
    Serial.print("          ");     Serial.print(conv::mbarToAtm(conv::mbar(prs_raw)));      Serial.println(" atm");
    Serial.print("          ");     Serial.println(conv::mbarToPascal(conv::mbar(prs_raw))); Serial.println(" pas");
    Serial.println("\n=======================\n");

    delay(3000);
}