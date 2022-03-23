/**
 * EmailJs code taken from https://www.emailjs.com/docs/tutorial/creating-contact-form/
 * and help was taken from code institute
 */
function sendMail(contactForm) {
    emailjs.init("user_ijKY6mblVUbu5AeWdbYlk");
    emailjs.send("gmail", "instrumenta", {
        "customer_email": contactForm.email.value
    }).then(
        function (response) {
            $("#mail-container").replaceWith("Thanks for subscribing");
        }
    );
    return false;
}