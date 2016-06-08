/*

HORLOGE À CYCLES ULTRADIENS

http://ouilogique.com/horloge_cycles_ultradiens/

DESCRIPTION DU PROGRAMME
Ce programme affiche le pourcentage d’attention d’une personne en fonction
de l’heure. Il se base sur les hypothèses suivantes :

- Le corps humain est soumis à des cycles d’attention d’une durée d’une
  heure et demie, soit 16 cycles de 5400 secondes par jour.
- Lors de ces cycles, l’attention passe par un minimum et par un maximum et
  peut être représentée sous la forme d’un cosinus.
- Le seul paramètre qui change d’une personne à l’autre est le déphasage de
  la courbe.

Pour utiliser ce programme, il faut donc connaître une des 16 heures
d’attention maximum possibles lors d’une journée et de modifier la constante
“heureAttentionMax” en conséquence.

Pour mettre à jour l’heure de l’horloge, il faut changer la valeur de
“avecSerial” à “true” et recharger le programme sur le microcontrôleur.
Cette valeur est à “false” par défaut pour limiter l’utilisation de la RAM.


HORLOGE DS1307 I²C
    RÉFÉRENCE AliExpress
    http://www.aliexpress.com/item/5pcs-lot-Tiny-RTC-I2C-AT24C32-DS1307-Real-Time-Clock-Module-Board-For-Arduino-With-A/32327865928.html

    ADRESSES I²C
    0x50 (EEPROM AT24C32)
    0x68 (DS1307)

    LIBRAIRIE Adafruit
    https://github.com/adafruit/RTClib.git

    CONNEXIONS
    GND    GND
    VCC    +5V
    SDA    pin A4
    SCL    pin A5

ÉCRAN OLED 128×64 I²C
    RÉFÉRENCE AliExpress
    http://www.aliexpress.com/item/1Pcs-Yellow-blue-double-color-128X64-OLED-LCD-LED-Display-Module-For-Arduino-0-96/32305641669.html

    ADRESSE I²C
    0x3C

    LIBRAIRIE Adafruit
    https://github.com/adafruit/Adafruit_SSD1306.git

    CONNEXIONS
    GND    GND
    VDD    +5V
    SCK    pin A5
    SDA    pin A4

PULLUPS I²C
    4.7 kΩ

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

#define avecSerial false

// Modifier ici l’heure d’attention maximum.
// Par exemple, si 7 h 15 est une heure d’attention maximum :
// heureAttentionMax = 7 h 15
// heureAttentionMax = MOD( 7*3600 + 15*60, 5400 )
// heureAttentionMax = 4500 s
// (5400 est le nombre de secondes dans 1 h 30)
const long heureAttentionMax = 4500;
const byte displayWidth = 128;
static const unsigned char cosinus_cmap[ displayWidth ] PROGMEM =
{
  63, 63, 63, 63, 63, 62, 62, 62,
  62, 62, 62, 61, 61, 61, 61, 60,
  60, 60, 59, 59, 58, 58, 57, 57,
  56, 56, 55, 55, 54, 54, 53, 53,
  52, 52, 51, 51, 50, 50, 49, 49,
  48, 48, 47, 47, 46, 46, 45, 45,
  45, 44, 44, 44, 44, 43, 43, 43,
  43, 43, 43, 42, 42, 42, 42, 42,
  42, 42, 42, 42, 42, 43, 43, 43,
  43, 43, 43, 44, 44, 44, 44, 45,
  45, 45, 46, 46, 47, 47, 48, 48,
  49, 49, 50, 50, 51, 51, 52, 52,
  53, 53, 54, 54, 55, 55, 56, 56,
  57, 57, 58, 58, 59, 59, 60, 60,
  60, 61, 61, 61, 61, 62, 62, 62,
  62, 62, 62, 63, 63, 63, 63, 63
};

void prepareCourbeCycle( int16_t frac16eJourPx )
{
  unsigned char py;
  // Partie de la courbe avec remplissage
  for( int16_t px=0; px<=frac16eJourPx; px++ )
  {
    py = pgm_read_byte( &cosinus_cmap[ px ] );
    display.drawLine( px, display.height()-1, px, py, WHITE );
  }
  // Partie de la courbe sans remplissage
  for( int16_t px=frac16eJourPx+1; px<displayWidth; px++ )
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
  // 2016,6,8,11,18,20

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

  // ****
  // Calculs du pourcentage du cycle d’attention (cycleAtt)
  // et du temps équivalent en 1/16e de jour exprimé en pixels (frac16eJourPx)
  // **

  // lecture de l’heure actuelle
  DateTime now = RTC.now();

  // Calcul du temps équivalent en 1/16e de jour
  // NB : - Il y a 16 cycles d’1 h 30 dans 24 h
  //      - 1 h 30 = 5400 s
  long frac16eJour = ( now.secondstime() - heureAttentionMax ) % 5400;

  // Calcul du pourcentage du cycle d’attention
  // 2 * π * 16 / 86400 = 0.0011635528
  double cycleAtt = 100.0 * 0.5 * ( 1.0 + cos( ( double )( frac16eJour ) * 0.0011635528 ) );

  // Conversion de “frac16eJour” en pixels.
  // Le cosinus est affiché avec un déphasage d’une demi-période, donc
  // les valeurs de la 1ère moitié du cycle correspondent à la partie droite du cosinus et
  // les valeurs de la 2e moitié du cycle correspondent à la partie gauche du cosinus.
  // Le code ci-dessous permute les deux moitiés pour qu’elles s’affichent du bon côté.
  int16_t frac16eJourPx;
  if( frac16eJour < 5400/2 )
    { frac16eJourPx = map( frac16eJour,
                              0,              5400/2-1,
                              displayWidth/2, displayWidth-1 ); }
  else
    { frac16eJourPx = map( frac16eJour,
                              5400/2,         5400-1,
                              0,              displayWidth/2-1 ); }


  // ****
  //  Affichage des résultats
  // **

  // Effacement de l’écran
  display.clearDisplay();

  // Préparation de l’affichage de la date
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
    case 12: display.print( F( "DEC"  ) );
  }
  display.setCursor( 0, 9 );
  display.print( now.year() );

  // Préparation de l’affichage de l’heure et des minutes
  char texteAffichage[ 5 ];
  sprintf( texteAffichage, "%2d:%02d", now.hour(), now.minute() );
  display.setTextSize( 2 );
  display.setCursor( 49, 0 );
  display.print( texteAffichage );

  // Préparation de l’affichage des secondes
  sprintf( texteAffichage, ":%02d", now.second() );
  display.setTextSize( 1 );
  display.print( texteAffichage );

  // Préparation de l’affichage du pourcentage du cycle
  display.setTextSize( 2 );
  #if false // Affichage avec 3 chiffres significatifs pour le déverminage
    if( cycleAtt < 0.005 )
      { display.setCursor( 53, 21 ); display.print( cycleAtt, 0 ); }
    else if( cycleAtt < 9.995 )
      { display.setCursor( 34, 21 ); display.print( cycleAtt, 2 ); }
    else if( cycleAtt < 99.95 )
      { display.setCursor( 34, 21 ); display.print( cycleAtt, 1 ); }
    else
      { display.setCursor( 42, 21 ); display.print( cycleAtt, 0 ); }
  #else // Affichage sans décimales pour l’utilisation normale
    if( cycleAtt < 9.5 )       { display.setCursor( 54, 21 ); }
    else if( cycleAtt < 99.5 ) { display.setCursor( 49, 21 ); }
    else                       { display.setCursor( 42, 21 ); }
    display.print( cycleAtt, 0 );
  #endif
  display.print( char( 37 ) ); // signe %

  // Préparation de l’affichage de la courbe du cycle
  prepareCourbeCycle( frac16eJourPx );

  // Met à jour l’affichage
  display.display();

  _delay_ms( 1000 );
}
