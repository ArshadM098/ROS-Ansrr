
#define TRIG1 13
#define ECHO1 12

#define TRIG2 11
#define ECHO2 10

#define NUM_SENSOR 5

int trig_us[5] = {13,11,9,7,5};
int echo_us[5] = {12,10,8,6,4};

float distance = 0;

void setup()
{
  for(int i = 0; i < NUM_SENSOR; i++){
  	pinMode(trig_us[i], OUTPUT);
  	pinMode(echo_us[i], INPUT);
  }
  Serial.begin(9600);
}

float read_us(int trig, int echo){
  float dist = 0;
  long duration = 0;
  digitalWrite(trig,LOW);
  delay(2);
  
  digitalWrite(trig,HIGH);
  delay(10);
  digitalWrite(trig,LOW);

  duration = pulseIn(echo,HIGH);
  dist = duration * 0.03502/2;
  
  return dist;
}

void loop()
{
  for(int i = 0; i < NUM_SENSOR; i++){
    distance = read_us(trig_us[i],echo_us[i]);
    Serial.print("Distance_sens_");
    Serial.print(i);
    Serial.print(" = ");
    Serial.println(distance);
  }
  
}