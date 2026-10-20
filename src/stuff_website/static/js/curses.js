document.addEventListener("DOMContentLoaded", () => {
    // Trigger initial page fade-in
    const fadeElements = document.querySelectorAll(".fade-in");
    fadeElements.forEach(element => {
        element.classList.add("visible");
    });

    // Subpage 1 API Fetch logic
    const fetchBtn = document.getElementById("fetch-btn");
    const textDisplay = document.getElementById("text-display");

    if (fetchBtn && textDisplay) {
        fetchBtn.addEventListener("click", async () => {
            fetchBtn.disabled = true;
            textDisplay.classList.add("loading");

            try {
                const response = await fetch("/api/random-curse");
                const data = await response.json();

                // Replace text and remove placeholder styling
                textDisplay.textContent = data.text;
                textDisplay.classList.remove("placeholder");
            } catch (error) {
                console.error("Error fetching text:", error);
                textDisplay.textContent = "Failed to load text. Please try again.";
            } finally {
                fetchBtn.disabled = false;
                textDisplay.classList.remove("loading");
            }
        });
    }
});