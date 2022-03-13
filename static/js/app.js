//     function validation(){
//     var roll = document.getElementById("roll").value;    
//     var fname = document.getElementById("fname").value;
//     var lname = document.getElementById("lname").value;
//     var father = document.getElementById("father").value;
//     // var address = document.getElementById("address").value;
//     var mail = document.getElementById("mail").value;
//     var mobile = document.getElementById("mobile").value;
//     var alternate = document.getElementById("alternate").value;

//     var rollcheck = /^[0-9]{6}$/;
//     var fcheck = /^[A-Z a-z]{3,16}$/;
//     var lcheck = /^[A-Z a-z]{3,16}$/;
//     var fathercheck = /^[A-Z a-z]{3,16}$/;
//     var emailcheck = /^[A-Za-z_.0-9]{3,}@[A-Za-z]{3,}[.]{1}[a-z.]{2,6}$/;
//     var mobilecheck = /^[6789][0-9]{9}$/;
//     var altmobilecheck = /^[6789][0-9]{9}$/;

//     //if(roll=="" || fname== "" || lname== "" || father=="" || address=="" || mail=="" || mobile=="" || alternate==""){
//       //  alert("Please fill all details before submitting")
//     // }
//     if (rollcheck.test(roll)){
//         document.getElementById("rollerror").innerHTML = "";
//     }else{
//         document.getElementById("rollerror").innerHTML = " *Invalid Input";
//         return false;
//     }
//         if (fcheck.test(fname)){
//         document.getElementById("ferror").innerHTML = "";
//     }else{
//         document.getElementById("ferror").innerHTML = " *Invalid First Name";
//         return false;
//     }
//     if (lcheck.test(lname)){
//         document.getElementById("lerror").innerHTML = "";
//     }else{
//         document.getElementById("lerror").innerHTML = " *Invalid Last Name";
//         return false;
//     }
//     if (fathercheck.test(father)){
//         document.getElementById("fatherror").innerHTML = "";
//     }else{
//         document.getElementById("fathererror").innerHTML = " *Invalid Name";
//         return false;
//     }
//     if (emailcheck.test(mail)){
//         document.getElementById("mailerror").innerHTML = "";
//     }else{
//         document.getElementById("mailerror").innerHTML = " *Invalid Email";
//         return false;
//     }
//     if (mobilecheck.test(mobile)){
//         document.getElementById("mobileerror").innerHTML = "";
//     }else{
//         document.getElementById("mobileerror").innerHTML = " *Invalid Mobile Number";
//         return false;
//     }
//     if (altmobilecheck.test(alternate)){
//         document.getElementById("alterror").innerHTML = "";
//     }else{
//         document.getElementById("alterror").innerHTML = " *Invalid Mobile Number";
//         return false;
//     }
    
    
// }
// Example starter JavaScript for disabling form submissions if there are invalid fields
// (() => {
//     'use strict';
  
//     // Fetch all the forms we want to apply custom Bootstrap validation styles to
//     const forms = document.querySelectorAll('.needs-validation');
  
//     // Loop over them and prevent submission
//     Array.prototype.slice.call(forms).forEach((form) => {
//       form.addEventListener('submit', (event) => {
//         if (!form.checkValidity()) {
//           event.preventDefault();
//           event.stopPropagation();
//         }
//         form.classList.add('was-validated');
//       }, false);
//     });
//   })();
function validation() {
  var myarray = [];
  for (i = 0; i < 4; i++) {
  document.getElementById("error" + i).innerHTML = "";
  myarray[i] = 
  document.getElementById("mobile" + i).value;
  }
  for (i = 0; i < 4; i++) {
   var flag = false;
   for (j = 0; j < 4; j++) {
     if (i == j || myarray[i] == "" || myarray[j] == "") 
         continue;
     if (myarray[i] == myarray[j]) {
         flag = true;
      document.getElementById("error" + i).innerHTML += 
      "<br>Its identical to the phone number " + (j + 1);
                 }
             }
      if (flag == false) 
   document.getElementById("error" + i).innerHTML = "";
         }
}