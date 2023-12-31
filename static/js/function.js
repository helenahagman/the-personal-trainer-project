(function() {
    document.getElementById("sendButton").addEventListener("click", function() {
      var email = document.getElementById("form2Example1").value;
      var message = document.getElementById("messageInput").value;
  
      var templateParams = {
        email: email,
        message: message
      };
  
      emailjs.send("service_b8gz1av", "template_8j0ugds", templateParams, "RO0elmR_iHiWZiyEO")
        .then(function(response) {
          console.log("SUCCESS!", response.status, response.text);
          alert("Thank you! Your message was sent successfully!");
        }, function(error) {
          console.log("FAILED...", error);
          alert("Oops something went wrong, check your email and try again.");
        });
    });
  
    document.getElementById("signInButton").addEventListener("click", function() {
      var email = document.getElementById("form2Example1").value;
      var password = document.getElementById("form2Example2").value;
  
      // Perform authentication logic here
  
      // Redirect to the user.html page if authentication is successful
      if (authenticationSuccessful) {
        window.location.href = "/templates/profile-page.html";
      } else {
        alert("Authentication failed. Please check your credentials.");
      }
    });
  })();
  