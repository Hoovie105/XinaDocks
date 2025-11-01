document.addEventListener('DOMContentLoaded', () => {
    // Add animation-complete class after animations finish
    const animatedElements = document.querySelectorAll('.animate-fade-up');
    
    animatedElements.forEach(element => {
        element.addEventListener('animationend', () => {
            element.classList.add('animation-complete');
        });
    });
});