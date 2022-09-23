// C++ code
//
void setup()
{
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(7,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int a_value=analogRead(A3);
  int tem=a_value*(5.0/1023.0)*100;
  Serial.println("the temperatur is:");
  Serial.println(tem);//tem=temperature
  if(tem>28)
  {
    analogWrite(5,255);
    delay(500);
    digitalWrite(7,HIGH);
    delay(2000);
  }
  else if(tem<28)
  {
    analogWrite(6,255);
    digitalWrite(7,LOW);
  }
  delay(3000);
   
  
                         

}