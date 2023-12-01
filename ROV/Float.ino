#include <Wire.h>

#include <SoftwareSerial.h>

#include <DS1307RTC.h>

#include <TimeLib.h>

#include <ms5540c.h>

#include <SPI.h>

class Float
{
private:
    // Pin numbers
    int depthClockPin;
    int hc12TxPin;
    int hc12RxPin;
    int motorInput1;
    int motorInput2;
    int enablePin;

    int depthThreshold;
    int depth;
    int temp_c;
    int rtcSecond;
    int rtcMinute;
    int rtcHour;
    int rtcDay;
    int rtcMonth;
    int rtcYear;
    String data;
    SoftwareSerial hc12Serial;
    ms5540c sensor;
    const char *monthName[12] = {
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"};
    tmElements_t tm;

    bool getTime(const char *str)
    {
        int Hour, Min, Sec;

        if (sscanf(str, "%d:%d:%d", &Hour, &Min, &Sec) != 3)
            return false;
        tm.Hour = Hour;
        tm.Minute = Min;
        tm.Second = Sec + 8;
        return true;
    }

    bool getDate(const char *str)
    {
        char Month[12];
        int Day, Year;
        uint8_t monthIndex;

        if (sscanf(str, "%s %d %d", Month, &Day, &Year) != 3)
            return false;
        for (monthIndex = 0; monthIndex < 12; monthIndex++)
        {
            if (strcmp(Month, monthName[monthIndex]) == 0)
                break;
        }
        if (monthIndex >= 12)
            return false;
        tm.Day = Day;
        tm.Month = monthIndex + 1;
        tm.Year = CalendarYrToTm(Year);
        return true;
    }

public:
    Float(int depthClockPin, int txPin, int rxPin, int input1, int input2, int enable, int threshold) : depthClockPin(depthClockPin),
                                                                                                        hc12TxPin(txPin),
                                                                                                        hc12RxPin(rxPin),
                                                                                                        motorInput1(input1),
                                                                                                        motorInput2(input2),
                                                                                                        enablePin(enable),
                                                                                                        depthThreshold(threshold),
                                                                                                        hc12Serial(txPin, rxPin) {}

    void initialize()
    {
        // motor driver
        pinMode(motorInput1, OUTPUT);
        pinMode(motorInput2, OUTPUT);
        pinMode(enablePin, OUTPUT);

        // HC-12
        hc12Serial.begin(9600);

        // RTC

        bool parse = false;
        bool config = false;

        if (getDate(__DATE__) && getTime(__TIME__))
        {
            parse = true;
            if (RTC.write(tm))
            {
                config = true;
            }
        }

        Serial.begin(9600);
        delay(200);
        if (parse && config)
        {
            Serial.print("DS1307 configured Time=");
            Serial.print(__TIME__);
            Serial.print(", Date=");
            Serial.println(__DATE__);
        }
        else if (parse)
        {
            Serial.println("DS1307 Communication Error :-{");
            Serial.println("Please check your circuitry");
        }
        else
        {
            Serial.print("Could not parse info from the compiler, Time=\"");
            Serial.print(__TIME__);
            Serial.print("\", Date=\"");
            Serial.print(__DATE__);
            Serial.println("\"");
        }

        // M5540C
        SPI.begin();
        sensor.begin();
    }

    void readDepth()
    {
        const long temp_raw = this->sensor.getTemperature(); // Temperature in tenths of the deg C
        const long prs_raw = this->sensor.getPressure();     // pressure in tenths of a mbar (because of the sensor precision)
        this->temp_c = conv::degC(temp_raw);
        long prs_mbar = conv::mbar(prs_raw);
        // long prs_atm = conv::mbarToAtm(prs_mbar);
        long prs_pasc = conv::mbarToPascal(prs_mbar);
        this->depth = prs_pasc / (1000 * 9.8); // calculate depth
    }
    void readTime()
    {
        RTC.read(tm);
        this->rtcHour = tm.Hour;
        this->rtcMinute = tm.Minute;
        this->rtcSecond = tm.Second;
        this->rtcDay = tm.Day;
        this->rtcMonth = tm.Month;
        this->rtcYear = tmYearToCalendar(tm.Year);
    }

    void getData()
    {
        readTime();
        readDepth();

        this->data = String(this->rtcHour) + "_" +
                     String(this->rtcMinute) + "_" +
                     String(this->rtcSecond) + "_" +
                     String(this->rtcDay) + "_" +
                     String(this->rtcMonth) + "_" +
                     String(this->rtcYear) + "_" +
                     String(this->depth) + "_" +
                     String(this->temp_c);
    }
    void sendData()
    {
        this->getData();
        hc12Serial.print(this->data);
        Serial.println(this->data);
    }
    void adjustMotor(int depth)
    {

        if (depth > depthThreshold)
        {
            down();
        }
        else if (depth < (depthThreshold / 2))
        {
            up();
        }
        else
        {
            stopMotor();
        }
    }

    void down()
    {
        digitalWrite(motorInput1, HIGH);
        digitalWrite(motorInput2, LOW);
        analogWrite(enablePin, 255);
    }

    void up()
    {
        digitalWrite(motorInput1, LOW);
        digitalWrite(motorInput2, HIGH);
        analogWrite(enablePin, 255);
    }

    void stopMotor()
    {
        digitalWrite(motorInput1, LOW);
        digitalWrite(motorInput2, LOW);
        analogWrite(enablePin, 0);
    }

    void operate()
    {
        this->sendData();
    }
};

Float myFloat(9, 1, 0, 2, 4, 5, 5); // depthClockPin,txPin,rxPin, input1, input2, enable, threshold

void setup()
{
    Serial.begin(9600);

    myFloat.initialize();
}

void loop()
{
    myFloat.operate();

    delay(1000);
}