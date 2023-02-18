/*

TRIGGER DE SCHMIDT POUR ENCLANCHEMENT DE RELAIS
===============================================

# DESCRIPTION DU PROGRAMME


Pour la gestion des interruptions, voir
https://sites.google.com/site/qeewiki/books/avr-guide/external-interrupts-on-the-atmega328

octobre 2016, ouilogique.com

*/


const int inPin = 2;
const int outPin = 12;
const int led1Pin = 13;
const int led2Pin = 11;


void setup()
{
  pinMode( inPin, INPUT );
  pinMode( outPin, OUTPUT );
  pinMode( led1Pin, OUTPUT );
  pinMode( led2Pin, OUTPUT );
  digitalWrite( led2Pin, HIGH );

  // Configure D2 pour générer une interruption
  // sur les changements d’état.
  EICRA |=  (1 << ISC00);
  EICRA &= ~(1 << ISC01);
  EIMSK |=  (1 << INT0);
  sei();
}

long T1;
const long dT = 100000;
bool inputGet = false;
bool prevInputGet = false;
bool inputRise = false;


void loop()
{
  if( inputRise )
  {
    if( inputGet )
    {
      T1 = millis();
      digitalWrite( outPin, HIGH );
    }
    else if( millis() - T1 >= dT )
    {
      inputRise = false;
      digitalWrite( outPin, LOW );
    }
  }
}


ISR( INT0_vect )
{
  inputGet = digitalRead( inPin );
  digitalWrite( led1Pin, inputGet );

  if( !prevInputGet && inputGet )
    { inputRise = true; }
  prevInputGet = inputGet;
}

