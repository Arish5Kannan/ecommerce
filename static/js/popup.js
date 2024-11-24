// Function to show the popup
function showPopup(greeting, message) {
    const popup = document.getElementById('popup');
    const greet = document.getElementById('greet');
    const msg = document.getElementById('msg');
    const closePopupBtn = document.getElementById('closePopup');

    greet.innerHTML = greeting;
    msg.innerHTML = message;

    // Show the popup
    popup.style.display = "block";

    // Handle closing the popup
    closePopupBtn.onclick = function() {
        popup.style.display = "none";
        // Optional: Redirect or enable background elements
    };

    // Close popup if user clicks outside the popup content
    window.onclick = function(event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    };
}
