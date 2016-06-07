/*

HORLOGE CYCLES ULTRADIENS

RÉFÉRENCE AliExpress DU DS1307
http://fr.aliexpress.com/item/5pcs-lot-Tiny-RTC-I2C-AT24C32-DS1307-Real-Time-Clock-Module-Board-For-Arduino-With-A/32327865928.html

ADRESSES I²C DU DS1307
0x50 (EEPROM AT24C32)
0x68 (DS1307)

LIBRAIRIE Adafruit du DS1307
https://github.com/adafruit/RTClib.git

CONNEXIONS
GND    GND
VCC    +5V
SDA    pin A4
SCL    pin A5

MICROCONTRÔLEUR
Clone Arduino Nano

juin 2016, ouilogique.com

*/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <math.h>
#include "RTClib.h"
RTC_DS1307 RTC = RTC_DS1307();
#include <Adafruit_SSD1306.h>
#define OLED_RESET 4
Adafruit_SSD1306 display( OLED_RESET );
#if( SSD1306_LCDHEIGHT != 64 )
#error( "Height incorrect, please fix Adafruit_SSD1306.h!" );
#endif

const int bBtn1  = PORTD2;
const int bLed13 = PORTB5;

#define btn1Read   ! bitRead( PIND, bBtn1 )
#define led13Set   bitSet( PORTB, bLed13 )
#define led13Clear bitClear( PORTB, bLed13 )
#define avecSerial false

const byte displayWidth = 128;
// static const unsigned char cosinus_cmap[ displayWidth ] PROGMEM =
// {
//   61, 61, 61, 61, 61, 60, 60, 60,
//   60, 59, 59, 59, 58, 58, 57, 57,
//   56, 56, 55, 54, 53, 52, 51, 50,
//   49, 48, 47, 46, 45, 44, 43, 42,
//   41, 40, 39, 38, 37, 36, 35, 34,
//   33, 32, 31, 30, 29, 28, 27, 26,
//   25, 25, 24, 24, 23, 23, 22, 22,
//   21, 21, 20, 20, 20, 20, 19, 19,
//   19, 19, 19, 20, 20, 20, 20, 21,
//   21, 22, 22, 23, 23, 24, 24, 25,
//   25, 26, 27, 28, 29, 30, 31, 32,
//   33, 34, 35, 36, 37, 38, 39, 40,
//   41, 42, 43, 44, 45, 46, 47, 48,
//   49, 50, 51, 52, 53, 54, 55, 56,
//   56, 57, 57, 58, 58, 59, 59, 59,
//   60, 60, 60, 60, 61, 61, 61, 61
// };

static const unsigned char cosinus_cmap[ displayWidth ] PROGMEM =
{
  63, 63, 63, 63, 63, 62, 62, 62,
  62, 62, 62, 62, 61, 61, 61, 61,
  60, 60, 60, 59, 59, 58, 58, 57,
  57, 56, 56, 55, 55, 54, 54, 53,
  53, 52, 52, 51, 51, 50, 50, 49,
  49, 48, 48, 47, 47, 46, 46, 45,
  45, 45, 44, 44, 44, 44, 43, 43,
  43, 43, 42, 42, 42, 42, 42, 42,
  42, 42, 42, 42, 42, 42, 42, 43,
  43, 43, 43, 44, 44, 44, 44, 45,
  45, 45, 46, 46, 47, 47, 48, 48,
  49, 49, 50, 50, 51, 51, 52, 52,
  53, 53, 54, 54, 55, 55, 56, 56,
  57, 57, 58, 58, 59, 59, 60, 60,
  60, 61, 61, 61, 61, 62, 62, 62,
  62, 62, 62, 62, 63, 63, 63, 63
};

void afficheCourbeCycle( int16_t pxNow )
{
  unsigned char py;
  // Partie de la courbe avec remplissage
  for( int16_t px=0; px<=pxNow; px++ )
  {
    py = pgm_read_byte( &cosinus_cmap[ px ] );
    display.drawLine( px, display.height()-1, px, py, WHITE );
  }
  // Partie de la courbe sans remplissage
  for( int16_t px=pxNow+1; px<displayWidth; px++ )
  {
    py = pgm_read_byte( &cosinus_cmap[ px ] );
    display.drawPixel( px, py, WHITE );
  }
}

#if avecSerial
void serialEvent()
{
  // Cette procédure permet de régler l’heure de l’horloge
  // via le bus RS232.
  // Exemple de commande à envoyer :
  // 2016,6,6,13,39,10

  const byte nbCharMax = 19;
  char str[ nbCharMax ] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };

  // Lecture de la nouvelle heure sur le port série
  byte compteur = 0;
  while( Serial.available() && compteur <= nbCharMax )
  {
    char inChar = ( char )Serial.read();
    if( inChar == '\n' ) break;
    str[ compteur++ ] = inChar;
  }

  // Séparation des éléments
  const char sep[ 2 ] = ",";
  char *token;
  int dateHeureInt[ 6 ];
  compteur = 0;
  // Trouve le premier séparateur
  token = strtok( str, sep );
  dateHeureInt[ 0 ] = atoi( token );
  // Trouve les autres séparateurs
  while( token != NULL )
  {
    token = strtok( NULL, sep );
    dateHeureInt[ ++compteur ] = atoi( token );
  }

  // Réglage de l’horloge et affichage de la nouvelle heure
  RTC.adjust( DateTime(
    dateHeureInt[ 0 ],
    dateHeureInt[ 1 ],
    dateHeureInt[ 2 ],
    dateHeureInt[ 3 ],
    dateHeureInt[ 4 ],
    dateHeureInt[ 5 ] ) );
  DateTime now = RTC.now();
  char nowChar[ 19 ];
  sprintf(
    nowChar,
    "Heure actuelle : %1d-%02d-%02d %02d:%02d:%02d",
    now.year(), now.month(),  now.day(),
    now.hour(), now.minute(), now.second() );
  Serial.println( nowChar );
}
#endif

void setup()
{
  #if avecSerial
  // Initalisation de la communication série pour régler l’heure
  Serial.begin( 115200 );
  #endif

  // Initialisation de l’horloge
  RTC.begin();

  // Initialisation de l’écran
  display.begin( SSD1306_SWITCHCAPVCC, 0x3C );
  display.clearDisplay();
  display.setTextColor( WHITE );
}

void loop()
{
/*
  // 2016,6,6,15,10,50
  // 2016,6,6,7,15,00
  // 2016,6,6,7,29,50
  // 2016,6,6,8,0,0
  // 2016,6,6,8,15,00
  // 2016,6,6,8,45,00
  // 2016,6,6,19,04,20
  // 2016,6,6,19,31,20
*/
  DateTime now = RTC.now();
  long secondstime = now.secondstime();
  // long nbSecondesSeiziemeJour = secondstime % 86400 % 5400;
  long nbSecondesSeiziemeJour = secondstime % 5400;
  const long heureMax = 4500; // 1:15 ⇒ correspond à 7:15
  long tempsCos = ( nbSecondesSeiziemeJour - heureMax );
  if( tempsCos < 0 )
    { tempsCos = 5400 + tempsCos; }
  double cycle = 50.0 * ( 1.0 + cos( double( tempsCos ) * 0.0011635528 ) ); // 2 * π * 16 / 86400 = 0.0011635528
  cycle = int( cycle * 10.0 ) / 10.0;
  byte pxNow = map( tempsCos, 0, 5399, 0, 127 );
  if( pxNow < displayWidth / 2 )
  { pxNow += displayWidth / 2; }
  else
  { pxNow -= displayWidth / 2; }
  // Serial.print( "\tsecondstime = " );
  // Serial.print( secondstime );
  // Serial.print( "\tnbSecondesSeiziemeJour = " );
  // Serial.print( nbSecondesSeiziemeJour );
  // Serial.print( "\ttempsCos = " );
  // Serial.print( tempsCos );
  // Serial.print( "\tpxNow = " );
  // Serial.print( pxNow );
  // Serial.print( "\tcycle = " );
  // Serial.print( cycle );
  // if( cycle < 100 )
  //   Serial.print( "\tcycle < 100" );
  // else
  //   Serial.print( "\tcycle >= 100" );
  // Serial.print( "\n" );

  // Efface l’écran
  display.clearDisplay();

  // Prépare l’affichage de la date
  display.setTextSize( 1 );
  display.setCursor( 0, 0 );
  display.print( now.day() );
  display.print( " " );
  switch( now.month() )
  {
    case  1: display.print( F( "JAN"  ) ); break;
    case  2: display.print( F( "FEV"  ) ); break;
    case  3: display.print( F( "MARS" ) ); break;
    case  4: display.print( F( "AVR"  ) ); break;
    case  5: display.print( F( "MAI"  ) ); break;
    case  6: display.print( F( "JUIN" ) ); break;
    case  7: display.print( F( "JUIL" ) ); break;
    case  8: display.print( F( "AOUT" ) ); break;
    case  9: display.print( F( "SEPT" ) ); break;
    case 10: display.print( F( "OCT"  ) ); break;
    case 11: display.print( F( "NOV"  ) ); break;
    case 12: display.print( F( "DEC"  ) ); break;
  }
  display.setCursor( 0, 9 );
  display.print( now.year() );

  // Prépare l’affichage de l’heure et des minutes
  char texteAffichage[ 5 ];
  sprintf( texteAffichage, "%2d:%02d", now.hour(), now.minute() );
  display.setTextSize( 2 );
  display.setCursor( 43, 0 );
  display.print( texteAffichage );

  // Prépare l’affichage des secondes
  sprintf( texteAffichage, ":%02d", now.second() );
  display.setTextSize( 1 );
  display.print( texteAffichage );

  // Prépare l’affichage du poucentage du cycle
  display.setTextSize( 2 );
  if( cycle < 10 )             // cycle = 0..9.9
  {
    display.setCursor( 45, 21 );
    display.print( cycle, 1 );
  }
  else if( cycle < 100 )       // cycle = 10..99.9
  {
    display.setCursor( 33, 21 );
    display.print( cycle, 1 );
  }
  else                         // cycle = 100
  {
    display.setCursor( 41, 21 );
    display.print( cycle, 0 );
  }
  display.print( char( 37 ) ); // signe %

  // Prépare l’affichage de la courbe du cycle
  afficheCourbeCycle( pxNow );

  // Met à jour l’affichage
  display.display();

  _delay_ms( 1000 );
}
