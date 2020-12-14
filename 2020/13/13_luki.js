const fs = require('fs')
 
try {
  var data = fs.readFileSync('13_2.txt', 'utf8');
  inputData = data   
} catch(e) {
  console.log('Error:', e.stack);
}
 
inputData = inputData.split("\n")
 
 
let busIds = inputData[1].split(",")
console.log(busIds.toString());
 
let inLoop = true;
let i = 1;
let departTimeModifier = 1
let departTime = Number(busIds[0]);
let departIncrementor = departTime;
 
while (inLoop){
  departTime += departIncrementor;
 
  let newDepartTime = departTime + departTimeModifier;
 
  if (busIds[i] === "x"){
    departTimeModifier+=1;
    i+=1
  }
  else if(newDepartTime % Number(busIds[i]) == 0){
      //success! found one
      console.log("----")
      departTime = newDepartTime - departTimeModifier
      console.log(departTime)
      console.log(departIncrementor)
      console.log(departTimeModifier)
    departIncrementor = departIncrementor * Number(busIds[i])
    i+=1
    departTimeModifier+=1;
  }
  if (i === busIds.length){
    inLoop = false;
  }
}
console.log(departTime)
