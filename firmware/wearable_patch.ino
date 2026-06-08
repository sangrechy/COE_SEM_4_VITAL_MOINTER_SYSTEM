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

    if (!maxSensor.begin(Wire, I2C_SPEED_STANDARD))
    {
        while (1);
    }

    maxSensor.setup();

    if (!mlx.begin())
    {
        while (1);
    }

    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x6B);
    Wire.write(0x00);
    Wire.endTransmission();

    Serial.println("EDGE AI SYSTEM READY");
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

    /*
        FUTURE PIPELINE

        ECG FEATURES
            ↓
        ecg_predict()

        STRESS FEATURES
            ↓
        stress_predict()

        FUSION
            ↓
        fusion_predict()
    */

    Serial.print("ECG=");
    Serial.print(ecgValue);

    Serial.print(" TEMP=");
    Serial.print(bodyTemp);

    Serial.print(" IR=");
    Serial.print(irValue);

    Serial.print(" RED=");
    Serial.println(redValue);

    delay(500);
}

