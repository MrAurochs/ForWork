//In this version which I slaved at for probably 3 or 4 hours I had to figure out 
//how to get the Dragonette to randomly attack with one of two attacks
//what I found was that I had to use the return command correctly 
//or everything was messed up 
//also, I made a new variable and it accidentally called the attacks on the skeleton
//which is NOT what I wanted since the skeleton was getting attacked 3 times in a row
//per turn

function dice(number,type){
	var total = 0 
	for (var n = 1; n < number + 1; n++)
		total += Math.floor(Math.random() * type ) + 1 
	return total
}

var myMonster ={
	name :"a critter", 
	hp : dice(4,6),
	str: [2,4],
	attack: function(other){
		
		var dam = dice(this.str[0], this.str[1])
		other.hp -= dam
		return (this.name + " attacks " + other.name + " for " + dam + " damage."   )
	
	}

}

function firebreath(other) {
	
	var dam = dice(3,8);
	
		
	other.hp = other.hp - dam;


	return (this.name + " breathes flames at " + other.name + " for " + dam + " damage." ) 
}



var Skeleton = Object.create(myMonster);
Skeleton.name = "skeleton"
Skeleton.hp = dice(4,8)
var Dragonette = Object.create(myMonster);
Dragonette.name = "dragonette" 
Dragonette.hp = dice(4,6)

Dragonette.str = [1,2]
Dragonette.firebreath = firebreath
Dragonette.attacks = function(other)
{
	
	Dragonette[0] = firebreath
	Dragonette[1] = Dragonette.attack
	
	var x =  Math.floor(Math.random() * 2)
	// if (x == 0){return Dragonette.firebreath(other)};
	// if (x == 1){return Dragonette.attack(other)} ;
	
	return Dragonette[x](other)
}


	

var Troll = Object.create(myMonster);
Troll.name = "troll"
Troll.str = [3,8]
Troll.hp = dice(5,10)


console.log("let the games begin!") 

var battlers = [Skeleton, Dragonette]

counter = 0 



while (Skeleton.hp > 0 && Dragonette.hp > 0) 
	
if (counter%2 === 0){
		console.log(Dragonette.attacks(Skeleton));
		counter++ 
		console.log("skelHP:", Skeleton.hp)
	}
	
	else{
		console.log(Skeleton.attack(Dragonette));
		counter++
		console.log("DragHP:", Dragonette.hp) 
		
	}

if (Skeleton.hp > 0){
	console.log("skeleton is the winner")}
if (Dragonette.hp > 0){
	console.log("dragonette is the winner") 
}