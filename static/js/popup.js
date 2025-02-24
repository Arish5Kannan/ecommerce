AOS.init();
// Function to show the popup
function showPopup(greeting, message) {
    console.log("showPopup() called:", greeting, message);
    
    const popup = document.getElementById('popup');
    const popupBox = document.getElementById('popupbox');
    const greet = document.getElementById('greet');
    const msg = document.getElementById('msg');
    const closePopupBtn = document.getElementById('closePopup');
    const img = document.getElementById('popImg');
    alert("hello");
    greet.innerHTML = greeting;
    msg.innerHTML = message;

    if (greeting === 'Oops! sorry') {
        img.src = "{% static 'images/wrong1.jpeg' %}";
        closePopupBtn.style.backgroundColor = "red";
    } else {
        img.src = "{% static 'images/tick.jpeg' %}";
        closePopupBtn.style.backgroundColor = "#31d109";
    }

    popup.style.display = "block";  // Ensure the popup is displayed
    popupBox.classList.add("popup-open");

    // Close button event
    closePopupBtn.onclick = function() {
        console.log("Popup closed!");
        popupBox.classList.remove("popup-open");
        popup.style.display = "none";
        window.location.href = "{% url 'cart' %}";
    };

    // Close when clicking outside
    window.onclick = function(event) {
        if (event.target === popup) {
            popupBox.classList.remove('popup-open');
            popup.style.display = "none";
            window.location.href = "{% url 'cart' %}";
        }
    };
}
