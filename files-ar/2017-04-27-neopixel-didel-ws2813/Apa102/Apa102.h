 // Apa102.h  ref 170104
#include <Arduino.h>
//typedef uint8_t byte;
//#define bitSet(x,y) x|=(1<<y)
//#define bitClear(x,y) x&=~(1<<y)
#define nop asm ("nop")

#define  bCk 0
#define  bDa 1
#define CkOn  bitSet (PORTC,bCk)
#define CkOff bitClear (PORTC,bCk)
#define DaOn bitSet (PORTC,bDa)
#define DaOff bitClear (PORTC,bDa)
void SetupApa () { DDRC = (1<<bCk)+(1<<bDa); }

void Snd8 (uint8_t dd) {
  for (uint8_t i=0;i<8;i++) {
    if (dd&0x80) DaOn;  else  DaOff;
    nop; CkOn; dd=dd<<1; CkOff;  // durée 0.25 us
  }
  DaOff;
}
void Snd (uint8_t nn,uint8_t aa,uint8_t rr,uint8_t gg,uint8_t bb) {
   Snd8(0); Snd8(0); Snd8(0); Snd8(0);   // start frame
   for (byte i=0;i<nn;i++) { Snd8(224+aa); Snd8(gg); Snd8(bb); Snd8(rr); }
   for (byte i=0; i< (nn+2)/2+2; i++) {CkOn; nop; CkOff; }// pushing bits till end
}



