let userid = document.getElementById("usr_id");
let userpw = document.getElementById("usr_pw");

let FailMsgId01 = document.querySelector('.fail-msg');
let FailMsgId02 = document.querySelector('.fail-msg2');

let Pwdreq1 = document.querySelector('.need-item1');
let Pwdreq2 = document.querySelector('.need-item2');
let Pwdreq3 = document.querySelector('.need-item3');



// 각종 함수

function SignupVaildation() {
  let regExUserId = /^[A-Za-z0-9][A-Za-z0-9]*$/;
  let regExUserPw1 = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
  let regExUserPw2 = /(.)\1{2,}/;

  // id check

  if (userid.value.length < 4 || userid.value.length > 12) {
    console.log(userid.value.length);
    alert('Wrong length');
    return;
  }

  if (!regExUserId.test(userid.value)) {
    alert('check your name');
    return;
  }

  // pw check

  // Make sure it contains at least 8 characters, Eng, numbers, and special characters.
  if (!regExUserPw1.test(userpw.value)) {
    alert('check your password');
    return;
  }

  // Check for characters duplicated more than 3 times
  if (regExUserPw2.test(userpw.value)) {
    alert('check your password 2');
    return;
  }

  // Check if the ID is inside
  if ((userpw.value).search(userid.value) > -1) {
    alert('id inserted in passwd');
    return;
  }


  // document.Signup.submit();
}

function idLength(value) {
  return value.length >= 4 && value.length <= 12
}

function onlyNumberAndEnglish(str) {
  return /^[A-Za-z0-9][A-Za-z0-9]*$/.test(str);
}

// ---

function PwdLength(value) {
  return value.length > 7
}

function Pwdregtest(str) {
  return /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]*$/.test(str);
}

function Pwdregtest2(str) {
  return /(.)\1{2,}/.test(str);
}

function isMatch(password1, password2) {
  return password1 === password2;
}


// 회원가입 설정 - 유효성 검사

// Description when entering key about ID

userid.onkeyup = function () {
  if (userid.value.length !== 0) {
    if (onlyNumberAndEnglish(userid.value) === false) {
      FailMsgId01.classList.add('hide');
      FailMsgId02.classList.remove('hide');
    } else if (idLength(userid.value) === false) {
      FailMsgId01.classList.remove('hide');
      FailMsgId02.classList.add('hide');
    } else if (idLength(userid.value) || onlyNumberAndEnglish(userid.id)) {
      FailMsgId01.classList.add('hide');
      FailMsgId02.classList.add('hide');
    }
  } else {
    FailMsgId01.classList.add('hide');
    FailMsgId02.classList.add('hide');
  }
}


// Description when entering key about password

userpw.onkeyup = function () {
  if (userpw.value.length !== 0) {

    if (PwdLength(userpw.value) === false) {
      Pwdreq1.classList.remove('hide');
      document.querySelector('.need-item1').style.color = 'red';
    } else {
      // Pwdreq1.classList.add('hide');
      document.querySelector('.need-item1').style.color = '#38c938';
    }

    if (Pwdregtest(userpw.value) === false) {
      Pwdreq2.classList.remove('hide');
      document.querySelector('.need-item2').style.color = 'red';
    } else {
      // Pwdreq2.classList.add('hide');
      document.querySelector('.need-item2').style.color = '#38c938';
    }

    if (Pwdregtest2(userpw.value) === true) {
      Pwdreq3.classList.remove('hide');
      document.querySelector('.need-item3').style.color = 'red';
    } else {
      // Pwdreq3.classList.add('hide');
      document.querySelector('.need-item3').style.color = '#38c938';
    }

  } else {
    Pwdreq1.classList.add('hide');
    Pwdreq2.classList.add('hide');
    Pwdreq3.classList.add('hide');
  }
}

// 아이템 등록 설정 - 유효성 검사

// let itemName = document.getElementById("item_name");