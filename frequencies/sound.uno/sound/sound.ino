
int pin_sine=9;
int pin_cos=10;
int amp_sine=0;
int amp_cos=0;

long frequency=1;

long _time=0;
void setup() {
  // put your setup code here, to run once:
  //pinMode(9,OUTPUT);
  //pinMode(10,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  amp_sine=255*sin(2*3.142*frequency*_time);
  amp_cos=255*cos(2*3.142*frequency*_time);

  //if (amp_sine<0)
  //amp_sine=-amp_sine;

  //if (amp_cos<0)
  //amp_cos=-amp_cos;


  analogWrite(pin_sine,amp_sine);
  analogWrite(pin_cos,amp_cos);

  _time+=1;


}
