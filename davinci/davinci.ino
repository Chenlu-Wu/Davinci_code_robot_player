#include <Servo.h>

Servo servo1;      //initialize a servo object for the connected servo                
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
int angle = 0;    
int inpython=0;
int val = 0;
int i=0;
String a;
  void setup() {
        // put your setup code here, to run once:
    servo1.attach(12); //l-arm 1st
    servo2.attach(13); //l-arm 2nd 
    servo3.attach(7);//l-arm 3rd, initialize value is 30
    servo4.attach(6);//clamp
    servo5.attach(10);//wraist
    servo6.attach(5);//camrotate
    Serial.begin(9600);
servo1.write(90);
servo2.write(30);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
  }
  
  void loop() {
if(Serial.available()>0) {
a= Serial.readString();// read the incoming data as string
//Serial.println(a);
}
if(a=="rec"){
  //move to robot panpel
    for(i=35;i>=0;i--){
    servo1.write(i);
servo2.write(112);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }
  for(i=112;i<=140;i++){
    servo2.write(i);
servo1.write(0);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }
      for(i=123;i>=120;i--){
    servo3.write(i);
servo2.write(140);
servo1.write(0);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }

//delay(10000);
Serial.write("1");
a="";
}
if (a=="recf"){
//robot 
//move back
    //move back
          for(i=120;i<=123;i++){
    servo3.write(i);
servo2.write(140);
servo1.write(0);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }

    //servo2
      for(i=140;i>=112;i--){
    servo2.write(i);
servo1.write(0);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }

    //servo1

        for(i=0;i<=35;i++){
    servo1.write(i);
servo2.write(112);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }
    Serial.write("1");
a="";
  }

  
if(a=="reck"){
//new
  //move to kid 
 for(i=35;i>=0;i--){
    servo1.write(i);
servo2.write(112);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }
  for(i=112;i<=140;i++){
    servo2.write(i);
servo1.write(0);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }
      for(i=123;i>=90;i--){
    servo3.write(i);
servo2.write(140);
servo1.write(0);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }


//delay(10000);
Serial.write("1");
a="";}

if (a=="reckf"){
//new merged
    //move back
          for(i=90;i<=123;i++){
    servo3.write(i);
servo2.write(140);
servo1.write(0);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }

    //servo2
      for(i=140;i>=112;i--){
    servo2.write(i);
servo1.write(0);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);
    }

    //servo1

        for(i=0;i<=35;i++){
    servo1.write(i);
servo2.write(112);
servo3.write(123);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(10);

Serial.write("1");
a="";
    }
//......................
}  
if (a=="take"){
  for(i=90;i>=70;i--){
    servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    //move the servo 2 from 30 to 72
  for(i=30;i<=72;i++){
    servo2.write(i);
servo1.write(70);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }

    //move servo three from 30 to 78
      for(i=30;i<=78;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(70);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    // move servo 1 back from 70 to 83
for(i=70;i<=83;i++){
    servo1.write(i);
servo2.write(72);
servo3.write(78);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//Load the pannel
//Move servo 3 up 3 degree
for(i=78;i<81;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(83);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//MOVE arm 1 back 
for(i=83;i>=40;i--){
    servo1.write(i);
servo2.write(72);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}


//move servo 2 back to 79
for(i=72;i<=79;i++){
    servo2.write(i);
servo1.write(40);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo 3 back to 137
for(i=81;i<=137;i++){
    servo3.write(i);
servo1.write(40);
servo2.write(79);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo1 back to 57
for(i=40;i<=57;i++){
    servo1.write(i);
servo2.write(79);
servo3.write(137);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//fang
for(i=90;i>=50;i--){
servo1.write(57);
servo2.write(79);
servo3.write(137);
servo4.write(i);
servo5.write(200);
servo6.write(90);
delay(5);
}



    //.................
    //move back
  //servo3
  for(i=137;i>=30;i--){
 servo1.write(57);
servo2.write(79);
servo3.write(i);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20) ;
  }

    
  //servo2
  for(i=79;i>=30;i--){
 servo2.write(i);
servo1.write(57);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }


    
//servo1
for(i=57;i<=90;i++){
 servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }
//one time end
  for(i=90;i>=70;i--){
    servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    //move the servo 2 from 30 to 72
  for(i=30;i<=72;i++){
    servo2.write(i);
servo1.write(70);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }

    //move servo three from 30 to 78
      for(i=30;i<=78;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(70);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    // move servo 1 back from 70 to 83
for(i=70;i<=83;i++){
    servo1.write(i);
servo2.write(72);
servo3.write(78);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//Load the pannel
//Move servo 3 up 3 degree
for(i=78;i<81;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(83);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//MOVE arm 1 back 
for(i=83;i>=40;i--){
    servo1.write(i);
servo2.write(72);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}


//move servo 2 back to 79
for(i=72;i<=79;i++){
    servo2.write(i);
servo1.write(40);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo 3 back to 137
for(i=81;i<=137;i++){
    servo3.write(i);
servo1.write(40);
servo2.write(79);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo1 back to 57
for(i=40;i<=57;i++){
    servo1.write(i);
servo2.write(79);
servo3.write(137);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//fang
for(i=90;i>=50;i--){
servo1.write(57);
servo2.write(79);
servo3.write(137);
servo4.write(i);
servo5.write(200);
servo6.write(90);
delay(5);
}



    //.................
    //move back
  //servo3
  for(i=137;i>=30;i--){
 servo1.write(57);
servo2.write(79);
servo3.write(i);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20) ;
  }

    
  //servo2
  for(i=79;i>=30;i--){
 servo2.write(i);
servo1.write(57);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }


    
//servo1
for(i=57;i<=90;i++){
 servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }
//one time end
  for(i=90;i>=70;i--){
    servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    //move the servo 2 from 30 to 72
  for(i=30;i<=72;i++){
    servo2.write(i);
servo1.write(70);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }

    //move servo three from 30 to 78
      for(i=30;i<=78;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(70);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    // move servo 1 back from 70 to 83
for(i=70;i<=83;i++){
    servo1.write(i);
servo2.write(72);
servo3.write(78);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//Load the pannel
//Move servo 3 up 3 degree
for(i=78;i<81;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(83);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//MOVE arm 1 back 
for(i=83;i>=40;i--){
    servo1.write(i);
servo2.write(72);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}


//move servo 2 back to 79
for(i=72;i<=79;i++){
    servo2.write(i);
servo1.write(40);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo 3 back to 137
for(i=81;i<=137;i++){
    servo3.write(i);
servo1.write(40);
servo2.write(79);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo1 back to 57
for(i=40;i<=57;i++){
    servo1.write(i);
servo2.write(79);
servo3.write(137);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//fang
for(i=90;i>=50;i--){
servo1.write(57);
servo2.write(79);
servo3.write(137);
servo4.write(i);
servo5.write(200);
servo6.write(90);
delay(5);
}


    //.................
    //move back
  //servo3
  for(i=137;i>=30;i--){
 servo1.write(57);
servo2.write(79);
servo3.write(i);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20) ;
  }

    
  //servo2
  for(i=79;i>=30;i--){
 servo2.write(i);
servo1.write(57);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }


    
//servo1
for(i=57;i<=90;i++){
 servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }
//one time end
  for(i=90;i>=70;i--){
    servo1.write(i);
servo2.write(30);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    //move the servo 2 from 30 to 72
  for(i=30;i<=72;i++){
    servo2.write(i);
servo1.write(70);
servo3.write(30);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }

    //move servo three from 30 to 78
      for(i=30;i<=78;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(70);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
    }
    // move servo 1 back from 70 to 83
for(i=70;i<=83;i++){
    servo1.write(i);
servo2.write(72);
servo3.write(78);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//Load the pannel
//Move servo 3 up 3 degree
for(i=78;i<81;i++){
    servo3.write(i);
servo2.write(72);
servo1.write(83);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//MOVE arm 1 back 
for(i=83;i>=40;i--){
    servo1.write(i);
servo2.write(72);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}


//move servo 2 back to 79
for(i=72;i<=79;i++){
    servo2.write(i);
servo1.write(40);
servo3.write(81);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo 3 back to 137
for(i=81;i<=137;i++){
    servo3.write(i);
servo1.write(40);
servo2.write(79);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}

//Move servo1 back to 57
for(i=40;i<=57;i++){
    servo1.write(i);
servo2.write(79);
servo3.write(137);
servo4.write(90);
servo5.write(200);
servo6.write(90);
delay(30);
}
delay(3000);

//fang
for(i=90;i>=50;i--){
servo1.write(57);
servo2.write(79);
servo3.write(137);
servo4.write(i);
servo5.write(200);
servo6.write(90);
delay(5);
}





      Serial.write("1");
    a="";
    //.................
    //move back
    
//servo1
for(i=57;i>=35;i--){
 servo1.write(i);
servo2.write(79);
servo3.write(137);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }


    
  //servo3
  for(i=137;i>=123;i--){
 servo1.write(35);
servo2.write(79);
servo3.write(i);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20) ;
  }

    
  //servo2
  for(i=79;i<=112;i++){
 servo2.write(i);
servo1.write(35);
servo3.write(123);
servo4.write(50);
servo5.write(200);
servo6.write(90); 
delay(20); 
  }



//one time end


  //...................

  }
if(a=="mo2"){
      Serial.write("1");
    a="";
  }
if(a=="mo3"){
      Serial.write("1");
    a="";
  }
if(a=="mo4"){
      Serial.write("1");
    a="";
  }
if(a=="tic1"){
 for(i=200;i>=140;i--){
servo5.write(i);
servo1.write(47);
servo2.write(112);
servo3.write(111);
servo4.write(90);
servo6.write(80);
delay(20);
    }
    delay(3000);
  for(i=111;i>=75;i--){
servo5.write(140);
servo1.write(47);
servo2.write(112);
servo3.write(i);
servo4.write(90);
servo6.write(80);
delay(5);
    }
      Serial.write("1");
    a="";
    
    //move back

      for(i=75;i<=123;i++){
servo5.write(140);
servo1.write(47);
servo2.write(112);
servo3.write(i);
servo4.write(90);
servo6.write(80);
delay(20);
    }   

       for(i=140;i<=200;i++){
servo5.write(i);
servo1.write(47);
servo2.write(112);
servo3.write(111);
servo4.write(90);
servo6.write(80);
delay(20);
    }
    //...................
  }
if(a=="tic2"){
for(i=200;i>=84;i--){
servo1.write(37);
servo2.write(130);
servo3.write(104);
servo4.write(90);
servo5.write(i);
servo6.write(124);
delay(20);
    }
    delay(3000);
    
  for(i=104;i>=75;i--){
servo1.write(37);
servo2.write(130);
servo3.write(i);
servo4.write(90);
servo5.write(84);
servo6.write(124);
delay(5);
    }
      Serial.write("1");
    a="";
     //move back
   for(i=75;i<=104;i++){
servo1.write(37);
servo2.write(130);
servo3.write(i);
servo4.write(90);
servo5.write(84);
servo6.write(124);
delay(20);
    }    

      for(i=84;i<=200;i++){
servo1.write(37);
servo2.write(130);
servo3.write(104);
servo4.write(90);
servo5.write(i);
servo6.write(124);
delay(20);
    }
    delay(3000);
    //...........................
  }
if(a=="tic3"){
for(i=200;i>=57;i--){
servo1.write(35);
servo2.write(123);
servo3.write(112);
servo4.write(90);
servo5.write(i);
servo6.write(92);
delay(20);
    }
    delay(3000);
  for(i=111;i>=75;i--){
servo1.write(35);
servo2.write(123);
servo3.write(i);
servo4.write(90);
servo5.write(47);
servo6.write(92);
delay(5);
    }    
      Serial.write("1");
    a="";
    
      for(i=75;i<=112;i++){
servo1.write(35);
servo2.write(123);
servo3.write(i);
servo4.write(90);
servo5.write(47);
servo6.write(92);
delay(20);
    }  

       for(i=57;i<=200;i++){
servo1.write(35);
servo2.write(123);
servo3.write(112);
servo4.write(90);
servo5.write(i);
servo6.write(92);
delay(20);
    }
    //....................................
  }
if(a=="tic4"){
     for(i=200;i>=-10;i--){
servo1.write(36);
servo2.write(131);
servo3.write(104);
servo4.write(90);
servo5.write(i);
servo6.write(92);
delay(20);
    }
    delay(3000);
  for(i=104;i>=75;i--){
servo1.write(36);
servo2.write(131);
servo3.write(i);
servo4.write(90);
servo5.write(15);
servo6.write(92);
delay(5);
    } 
Serial.write("1");
    a="";
for(i=75;i<=104;i++){
servo1.write(36);
servo2.write(131);
servo3.write(i);
servo4.write(90);
servo5.write(15);
servo6.write(92);
delay(20);
    }   

      for(i=-10;i<=200;i++){
servo1.write(36);
servo2.write(131);
servo3.write(104);
servo4.write(90);
servo5.write(i);
servo6.write(92);
delay(20);
    }
    //.................
  }  
  }
