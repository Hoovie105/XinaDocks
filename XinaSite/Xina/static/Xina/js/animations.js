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
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const documentList = document.getElementById('documentList');
  const docs = Array.from(documentList.getElementsByClassName('doc-item'));

  searchInput.addEventListener('input', function() {  
    const query = this.value.toLowerCase();
    docs.forEach(doc => {
      const title = doc.querySelector('.doc-title').textContent.toLowerCase();
      const content = doc.querySelector('.doc-content').textContent.toLowerCase();
      // Show if title OR content includes the search query
      doc.style.display = (title.includes(query) || content.includes(query)) ? '' : 'none';
    });
  });
});