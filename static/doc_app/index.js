function idGenerator() {
  var minm = 100000;
  var maxm = 999999;
  return Math.floor(Math
  .random() * (maxm - minm + 1)) + minm;
}


if (sessionStorage.getItem('id')==''|| sessionStorage.getItem('id') == null){
  let output = idGenerator()
  document.getElementById('id').value=output;
  sessionStorage.setItem('id', output)
  console.log("First")
}else if(sessionStorage.getItem('id')!=''){
  document.getElementById('id').value = sessionStorage.getItem('id');
  console.log(sessionStorage.getItem('id'))
}



//////////////////////////////////////////////////////////////////
 document.getElementById("profile_group2").style.display='none';

$(function(){
  var effects = 'animate__animated animate__slideOutLeft';
  var effects2 ='animate__animated animate__slideInRight'
  var effectsEnd = 'animationend oAnimationEnd mozAninationEnd webkitAnimationEnd';
  
  $("#next_btn").click(function(){
  idGenerator()
      $("#profile_group1").addClass(effects).one(effectsEnd, function(){
          $("#profile_group1").css("display","none");
          $("#profile_group2").addClass(effects2);
            $("#profile_group2").css("display","block");
          
    });
  });
});