#include <LiquidCrystal.h>
#include <TimerOne.h>

//LCD pin to Arduino
const int pin_RS = 8; 
const int pin_EN = 9; 
const int pin_d4 = 4; 
const int pin_d5 = 5; 
const int pin_d6 = 6; 
const int pin_d7 = 7; 
const int pin_BL = 10; 
String CadenaEntrada="";
bool FinCadena= false;
int Analogica0;
int Analogica1;
int Analogica2;
int Analogica3;
int Analogica4;
int Analogica5;

char button;

LiquidCrystal lcd( pin_RS,  pin_EN,  pin_d4,  pin_d5,  pin_d6,  pin_d7);

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  lcd.begin(16, 2);
  CadenaEntrada.reserve(20);
  //Timer interrumpe cada 1 segundo
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(CadaSegundo);
}

void loop() {
  int x;
  int last_x;
  int i;
  char last_data[8];
  


if(FinCadena){
CadenaEntrada.remove(CadenaEntrada.length()-1,1);
if (CadenaEntrada.endsWith("+")){
CadenaEntrada.remove(CadenaEntrada.length()-1,1);
lcd.setCursor(0,0);
lcd.print(CadenaEntrada);    
}else if(CadenaEntrada.endsWith("-")){
CadenaEntrada.remove(CadenaEntrada.length()-1,1);
lcd.setCursor(0,1);
lcd.print(CadenaEntrada);    
}
CadenaEntrada="";
FinCadena=false;
}

 
Analogica0 = analogRead (0);
Analogica1 = analogRead (1);
Analogica2 = analogRead (2);
Analogica3 = analogRead (3);
Analogica4 = analogRead (4);
Analogica5 = analogRead (5);
x=Analogica0;

lcd.setCursor(15,0);
if (x < 60) {
    lcd.print ("R");
    button='R';
  }
  else if (x < 200) {
    lcd.print ("U");
    button='U';
  }
  else if (x < 400){
    lcd.print ("D");
    button='D';
  }
  else if (x < 600){
    lcd.print ("L");
    button='L';
  }
  else if (x < 800){
    lcd.print ("S");
    button='S';
  }
  
  }

void serialEvent(){
  //recepcion Serial
  while(Serial.available()){
    char CaracterEntrada=Serial.read();
    CadenaEntrada+=CaracterEntrada;
    if (CaracterEntrada =='\n'|| CadenaEntrada.length()>=18){
      FinCadena=true;
      }
  }
}

void CadaSegundo(){
String mensaje=button+"|"+String(Analogica0, DEC)+"|"+String(Analogica1, DEC)+"|"+String(Analogica2, DEC)+"|"+String(Analogica3, DEC)+"|"+String(Analogica4, DEC)+"|"+String(Analogica5, DEC);
Serial.println(mensaje);

}


