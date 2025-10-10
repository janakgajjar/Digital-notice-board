// Trigger animation on new notices (e.g., after form submit, reload adds class)
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.notice-card');
    cards.forEach((card, index) => {
        setTimeout(() => card.style.animationDelay = `${index * 0.2}s`, 100);  // Staggered pinning
    });
});