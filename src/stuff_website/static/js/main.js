document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll(".fade-in");
    fadeElements.forEach(element => {
        element.classList.add("visible");
    });
});
