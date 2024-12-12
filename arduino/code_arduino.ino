#include "model_arduino.h"

int in1 = 5;
int in2 = 6;
int in3 = 10;
int in4 = 11;

int trig = 13;
int echo = 12;

int vitesse = 100;

// Broches des capteurs infrarouges
int capteurGauche = 7;
int capteurDroit = 2;


void setup() {
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(capteurGauche, INPUT);
  pinMode(capteurDroit, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  Serial.begin(9600);
}

void loop() {

  // Lire l'état des capteurs
  int etatGauche = digitalRead(capteurGauche);  // 0 : blanc, 1 : noir
  int etatDroit = digitalRead(capteurDroit);    // 0 : blanc, 1 : noir
 // put your main code here, to run repeatedly:
 digitalWrite(trig, LOW);
 delayMicroseconds(2);
 digitalWrite(trig,HIGH);
 delayMicroseconds(10);
 digitalWrite(trig,LOW);

 
 long duration = pulseIn(echo, HIGH);
 int distance = (duration * 0.034)/2;

 Serial.println(distance);

 double input[2] = {etatGauche, etatDroit};
 double output[4];

 score(input, output);

 if (output[0] == 1.0  && (distance < 15 || distance == 0)) {
   return  arreter();
} else if (output[1] == 1.0 && distance >= 15) {
    return  avancer();
} else if (output[2] == 1.0 && distance >= 15) {
    return tournerDroite();
} else if (output[3] == 1.0 && distance >= 15) {
     return tournerGauche();
}else {
      Serial.println("Aucune action reconnue par le modèle.");

}

}

void avancer() {
  digitalWrite(in3, 0);   
  digitalWrite(in2, 0); 
  digitalWrite(in1, vitesse);
  digitalWrite(in4,vitesse);  
  
  // Affichage de l'état des moteurs sur le moniteur série
  Serial.println("Les moteurs sont activés pour avancer.");

}

void arreter() {
  digitalWrite(in1, 0);
  digitalWrite(in2, 0);
  digitalWrite(in3, 0);
  digitalWrite(in4, 0);
  Serial.println("Arrêt");
}

void tournerDroite() {
 digitalWrite(in3, 0);   
  digitalWrite(in2, 0); 
  digitalWrite(in1, 0);
  digitalWrite(in4,vitesse);  
  Serial.println("Tourner à droite");
}

void tournerGauche() {
  digitalWrite(in4, 0);   
  digitalWrite(in2, 0); 
  digitalWrite(in1, vitesse);
  digitalWrite(in3,0);  
    Serial.println("Tourner à gauche");

}





