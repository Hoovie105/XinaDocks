document.addEventListener('DOMContentLoaded', () => {
  // Animation stuff for index.html
  const animatedElements = document.querySelectorAll('.animate-fade-up');
  animatedElements.forEach(element => {
    element.addEventListener('animationend', () => {
      element.classList.add('animation-complete');
    });
  });
});

 // Toggle buttons for Sign In / Sign Up forms
document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.toggle-btn');
  const signInForm = document.getElementById('sign-in-form');
  const signUpForm = document.getElementById('sign-up-form');

  // Only handle clicks; do not override initial server-rendered state
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active from both buttons
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      if (btn.textContent.trim() === 'Sign In') {
        signInForm.style.display = 'block';
        signUpForm.style.display = 'none';

        // Clear error messages when switching to Sign In
        const errorLists = signInForm.querySelectorAll('.errorlist');
        errorLists.forEach(ul => ul.innerHTML = '');
      } else {
        signInForm.style.display = 'none';
        signUpForm.style.display = 'block';
      }
    });
  });
});
