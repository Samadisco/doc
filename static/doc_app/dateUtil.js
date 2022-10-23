
const myFunction = ()=>{
  
birthDate = "03/04/1999"
birthYear = birthDate.split("/")[2]
birthMonth = birthDate.split("/")[1]
birthDay = birthDate.split("/")[0]
const currentYear = new Date().getFullYear();
 const currentDay = new Date().getDate()

const currentMonth  = Number(1) + new Date().getMonth() 


if (currentMonth == birthMonth && currentDay>= birthDay){
  
  age = currentYear - birthYear
  console.log(age)
}else if (currentMonth > birthMonth){
age = (currentYear - birthYear) 
}else{
  age = (currentYear - birthYear) -1
}


console.log(`You are ${age} years old`)

}

myFunction()

