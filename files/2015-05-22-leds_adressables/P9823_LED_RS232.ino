#include <Adafruit_NeoPixel.h>

#define LED_PIN 13
#define LED_COUNT 4
#define LED_TYPE ( NEO_RGB + NEO_KHZ800 )


uint8_t LEDnb = 0;
uint8_t colR  = 0;
uint8_t colG  = 0;
uint8_t colB  = 0;

Adafruit_NeoPixel strip = Adafruit_NeoPixel( LED_COUNT, LED_PIN, LED_TYPE);

void setup() {
    // initialize serial:
    Serial.begin( 115200 );
    Serial.print( "START LED\n" );
    strip.begin();
    for( uint16_t iLED=0; iLED<LED_COUNT; iLED++ )
        strip.setPixelColor( iLED, strip.Color( colR, colG, colB ) );
    strip.show();
}

void loop() {
    // if there's any serial available, read it:
    while( Serial.available() > 0 )
    {
        // look for the next valid integer in the incoming serial stream:
        int red = Serial.parseInt();
        // do it again:
        int green = Serial.parseInt();
        // do it again:
        int blue = Serial.parseInt();

        // look for the newline. That's the end of your
        // sentence:
        if( Serial.read() == '\n' )
        {
            // constrain the values to 0 - 255 and invert
            // if you're using a common-cathode LED, just use "constrain(color, 0, 255);"
            red   = constrain( red,   0, 255 );
            green = constrain( green, 0, 255 );
            blue  = constrain( blue,  0, 255 );

            colR = red;
            colG = green;
            colB = blue;

            strip.setPixelColor( 0, strip.Color( colR, colG, colB ) );
            strip.setPixelColor( 1, strip.Color( colR, colG, colB ) );
            // strip.setPixelColor( 2, strip.Color( colR, colG, colB ) );
            // strip.setPixelColor( 3, strip.Color( colR, colG, colB ) );
            strip.show();

            // print the three numbers in one string:
            Serial.print( red,    DEC ); Serial.print( "," );
            Serial.print( green,  DEC ); Serial.print( "," );
            Serial.print( blue,   DEC ); Serial.print( "\n" );
        }
    }
}

