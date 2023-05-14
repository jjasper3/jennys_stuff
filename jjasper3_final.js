var loopAgain = "y";
var userName = prompt("Before we get started, what is your name?");

function Main() {  //added

var decisionOne;
var decisionTwo;
var decisionThree;
var thankYou = ("Thanks for playing! Have a great day!");
var goodLuck = ("Good Luck!");



//userName = prompt("Before we get started, what is your name?"); 
while (loopAgain === "y"){
  decisionOne = prompt('Hello, ' + userName +'! You have been stranded on a remote island in the Pacific Ocean. Your first decision - do you make a fire to signal for help, or find shelter? Enter "1" to start a fire, or anything else to find shelter.');
    if (Number(decisionOne) === 1){
      decisionTwo=prompt('You find some tinder and light it with some matches you had in your backpack. Now to find food. Enter "1" to go fishing or anything else to forage for grubs.');
      if(Number(decisionTwo) === 1){
        alert("You caught a fish! You are able to cook it over the fire you created and comfortably make it through the night.  In the morning, a search and rescue boat arrives and saves you! Congratulations, you survived!");
      }else{
        alert("You ate a poisonous beetle. Better luck next time."); 
      }        
    }else{
      decisionThree=prompt("You find a cave. Do you want to explore inside? 1 for yes or anything else for no.");
        if (Number(decisionThree) === 1){
          alert("You enter the cave and encounter a tiger! You try to outrun it, but the tiger is too fast. Better luck next time!");
        }else{
          alert("You decide the cave may be too dangerous... who knows whats lurking inside?! You make a shelter using downed tree limbs and make it through the night unscathed. In the morning, a search and rescue boat arrives and saves you! Congratulations, you survived!");
        }      
      }
loopAgain =prompt('Do you want to try again? Enter "y" to try again, or "n" to exit.');
 //while (loopAgain){
  if (loopAgain !== "y"){
    alert(thankYou);
    loopAgain = "n";
  }else{
    alert(goodLuck);
  }
}   
}
//Run program

Main();




    






