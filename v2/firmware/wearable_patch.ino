#include <Wire.h>
#include <MAX30105.h>
#include <Adafruit_MLX90614.h>

#define SDA_PIN 8
#define SCL_PIN 9

#define MPU_ADDR 0x68
#define ECG_PIN 4

MAX30105 maxSensor;
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup()
{
    Serial.begin(115200);
    delay(2000);

    Wire.begin(SDA_PIN, SCL_PIN);

    Serial.println("================================");
    Serial.println("WEARABLE PATCH SENSOR PLATFORM");
    Serial.println("================================");

    if (!maxSensor.begin(Wire, I2C_SPEED_STANDARD))
    {
        Serial.println("MAX30102 NOT FOUND");
        while (1);
    }

    maxSensor.setup();

    if (!mlx.begin())
    {
        Serial.println("MLX90614 NOT FOUND");
        while (1);
    }

    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x6B);
    Wire.write(0x00);
    Wire.endTransmission();

    Serial.println("SYSTEM READY");
}

void loop()
{
    int ecgValue = analogRead(ECG_PIN);

    int16_t AcX = 0;
    int16_t AcY = 0;
    int16_t AcZ = 0;

    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x3B);
    Wire.endTransmission(false);

    if (Wire.requestFrom(MPU_ADDR, 6) == 6)
    {
        AcX = (Wire.read() << 8) | Wire.read();
        AcY = (Wire.read() << 8) | Wire.read();
        AcZ = (Wire.read() << 8) | Wire.read();
    }

    float bodyTemp = mlx.readObjectTempC();

    long irValue = maxSensor.getIR();
    long redValue = maxSensor.getRed();

    Serial.print("ECG:");
    Serial.print(ecgValue);

    Serial.print(" TEMP:");
    Serial.print(bodyTemp);

    Serial.print(" AX:");
    Serial.print(AcX);

    Serial.print(" AY:");
    Serial.print(AcY);

    Serial.print(" AZ:");
    Serial.print(AcZ);

    Serial.print(" IR:");
    Serial.print(irValue);

    Serial.print(" RED:");
    Serial.println(redValue);

    delay(500);
}
