
int output=9;
int amp=0;
int in=A0;
int val=0;
int val_=0;
long _time=0;

void setup() {
  Serial.begin(9600);

}

void loop() {

  val = analogRead(in);
  amp = map(val, 0, 1023, 0, 255);




  analogWrite(output,amp);


  //Serial.println(amp);
  //Serial.print(","); 

  //if (_time==1000)
    //Serial.print("\nx");

  //_time+=1;




}
