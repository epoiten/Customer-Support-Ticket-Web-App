document.addEventListener("DOMContentLoaded", function () {
    const descriptionInput = document.getElementById("description");
    const charCountSpan = document.getElementById("charCount");
    const ticketForm = document.getElementById("ticketForm");
    const errorBanner = document.getElementById("formError");

    // 1. Live Character Counter Interaction
    if (descriptionInput && charCountSpan) {
        const updateCounter = () => {
            const len = descriptionInput.value.length;
            charCountSpan.textContent = len;
            charCountSpan.style.color = len >= 450 ? "#dc2626" : "#64748b";
        };
        updateCounter(); // Initialize on page load (for Edit form)
        descriptionInput.addEventListener("input", updateCounter);
    }

    // 2. Client-Side Form Validation Interaction
    if (ticketForm) {
        ticketForm.addEventListener("submit", function (event) {
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const subject = document.getElementById("subject").value.trim();
            const description = document.getElementById("description").value.trim();

            let errorMessage = "";

            if (!name || !email || !subject || !description) {
                errorMessage = "Please fill in all required fields.";
            } else if (!email.includes("@") || !email.includes(".")) {
                errorMessage = "Please enter a valid email address.";
            } else if (description.length < 10) {
                errorMessage = "Description must be at least 10 characters long.";
            }

            if (errorMessage) {
                event.preventDefault();
                errorBanner.textContent = errorMessage;
                errorBanner.style.display = "block";
            }
        });
    }
});