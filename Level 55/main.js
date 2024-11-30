function passValidation() {
  let userPassword = document.getElementById("password").value;
  let message = document.getElementById("message");

  //? ამოწმებს მომხმარებლის მიერ შეყვანილი პაროლის სიგრძე არის თუ არა 4-სა და 12-ს შორის
  if (userPassword.length < 4 || userPassword.length > 12) {
    message.style.color = "red";
    message.textContent = "პაროლი უნდა შეიცავდეს 4-დან 12-მდე სიმბოლოს.";
    return;
  }

  //? ამოწმებს შეიცავს თუ არა პაროლი ცარიელ ადგილებს
  for (i = 0; i < userPassword.length; i++) {
    if (userPassword.includes(" ")) {
      message.style.color = "red";
      message.textContent = "პაროლი არ უნდა შეიცავდეს ცარიელ ადგილებს";
      return;
    }
  }

  const validChars =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._";
  //? ამოწმებს შეიცავს თუ არა პაროლი სიმბოლოებს
  for (i = 0; i < userPassword.length; i++) {
    if (!validChars.includes(userPassword[i])) {
      message.style.color = "red";
      message.textContent = "პაროლი უნდა შეიცავდეს რიცხვებს, ასოებს, -, . ან _";
      return;
    }
  }

  message.style.color = "green";
  message.textContent = "პაროლი ვალიდურია";
}
