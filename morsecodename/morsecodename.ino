// ------------
// Name in Morse Code by Blinking Onboard LED
// ------------


// Initialising the variables for the LEDs


int led = D7; // This one is the little blue LED on the board

int buttonPin = D3; // This declares the pushbutton

const int spaceDelay = 1000; // Delay between components of a letter
const int characterDelay = 3000; // Delay between characters in a word 
const int wordDelay = 7000; // Delay between words

// Need to fill out the setup function, acts as a constructor.
// It runs only once when the device boots up or is reset.
void setup() {

  // Initialising D7, the blue LED
  pinMode(led, OUTPUT);
  
  // Initialising the button
  pinMode(buttonPin, INPUT_PULLUP);

}

// Next we have the loop function, the other essential part of a microcontroller program.
// This routine gets repeated over and over, as quickly as possible and as many times as possible, after the setup function is called.
// Note: Code that blocks for too long (like more than 5 seconds), can make weird things happen (like dropping the network connection).  The built-in delay function shown below safely interleaves required background activity, so arbitrarily long delays can safely be done if you need them.

void loop() {
  // Initialise the LED to off
  digitalWrite(led, LOW);
  
  // Initialise a variable for the state of the button
  int buttonState = digitalRead(buttonPin);
  
  
//   nameLED();
  
  if( buttonState == LOW )
  {
    // turn the LED On
    nameLED();
  }else{
    // otherwise
    // turn the LED Off
    digitalWrite(led, LOW);
  }


}

void nameLED()
{
    S();
    delay(characterDelay); 
    U();
    delay(characterDelay); 
    N();
    delay(characterDelay); 
    N();
    delay(characterDelay); 
    Y();
    delay(wordDelay); 
}
// ------------------------------------FUNCTIONS FOR DASH AND DOT COMPONENTS--------------------------------------------------------------
// Define a function for a dash
void dash()
{
    digitalWrite(led, HIGH); // Turn the LED on
    delay(characterDelay); // A dash is considered 3 dits so we need to light it up for 3 units of time
    digitalWrite(led, LOW); // Turn LED off
    delay(spaceDelay); // Regular space delay after
}

void dot()
{
    digitalWrite(led, HIGH); // Turn the LED on
    delay(spaceDelay); // A dash is considered 1 dits so we need to light it up for 1 unit of time
    digitalWrite(led, LOW); // Turn LED off
    delay(spaceDelay); // Regular space delay after
}

// ---------------------------------------FUNCTIONS FOR NAME ------------------------------------------------------------------------------
// Morse code instructions can be found here: https://morsecode.world/international/morse2.html
// S - dot dot dot
void S()
{
    dot();
    dot();
    dot();
}

// U - dot dot dash
void U()
{
    dot();
    dot();
    dash();
}

// N - dot dash
void N()
{
    dot();
    dash();
}

// Y - dash dot dash dash
void Y()
{
    dash();
    dot();
    dash();
    dash();
}
