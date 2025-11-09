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
    const docs = Array.from(documentList.getElementsByClassName('doc-card-link'));
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        docs.forEach(linkWrapper => {
            const docCard = linkWrapper.querySelector('.doc-card');
            const title = docCard.querySelector('.doc-title').textContent.toLowerCase();
            const content = docCard.querySelector('.doc-content').textContent.toLowerCase();
            const isMatch = (title.includes(query) || content.includes(query));
            linkWrapper.style.display = isMatch ? '' : 'none'; 
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
// File upload + preview script
    (function(){
      const dropZone = document.getElementById('dropZone');
      const fileInput = document.getElementById('fileInput');
      const fileList = document.getElementById('fileList');

      function humanFileSize(size){
        const i = size==0?0:Math.floor(Math.log(size)/Math.log(1024));
        return (size/Math.pow(1024,i)).toFixed( (i?1:0) ) * 1 + [' B',' KB',' MB',' GB'][i];
      }

      function renderFiles(files){
        fileList.innerHTML = '';
        const list = Array.from(files);
        list.forEach((file, idx)=>{
          const item = document.createElement('div');
          item.className = 'file-item';

          const preview = document.createElement('div');
          preview.className = 'file-preview';

          const info = document.createElement('div');
          info.className = 'file-info';

          const name = document.createElement('div');
          name.className = 'file-name';
          name.textContent = file.name;

          const meta = document.createElement('div');
          meta.className = 'file-meta';
          meta.textContent = humanFileSize(file.size);

          // image preview
          if(file.type.startsWith('image/')){
            const img = document.createElement('img');
            img.className = 'thumb';
            const reader = new FileReader();
            reader.onload = e => img.src = e.target.result;
            reader.readAsDataURL(file);
            preview.appendChild(img);
          } else if(file.type === 'application/pdf' || file.name.toLowerCase().endsWith('.pdf')){
            const icon = document.createElement('div');
            icon.className = 'file-icon pdf';
            icon.textContent = 'PDF';
            preview.appendChild(icon);
          } else {
            const icon = document.createElement('div');
            icon.className = 'file-icon';
            icon.textContent = file.name.split('.').pop().toUpperCase();
            preview.appendChild(icon);
          }

          const removeBtn = document.createElement('button');
          removeBtn.className = 'file-remove';
          removeBtn.type = 'button';
          removeBtn.innerHTML = '\u2715';
          removeBtn.addEventListener('click', ()=>{
            // remove file from FileList — we create a new DataTransfer
            const dt = new DataTransfer();
            list.forEach((f, i)=>{ if(i!==idx) dt.items.add(f); });
            fileInput.files = dt.files;
            renderFiles(dt.files);
          });

          info.appendChild(name);
          info.appendChild(meta);

          item.appendChild(preview);
          item.appendChild(info);
          item.appendChild(removeBtn);

          fileList.appendChild(item);
        });
      }
      dropZone.addEventListener('click', (e)=>{
        if (e.target.id !== 'fileInput') { 
          fileInput.click();
        }
      });
      fileInput.addEventListener('change', ()=> renderFiles(fileInput.files));

      dropZone.addEventListener('dragover', (e)=>{
        e.preventDefault();
        dropZone.classList.add('dragover');
      });
      dropZone.addEventListener('dragleave', ()=> dropZone.classList.remove('dragover'));

      dropZone.addEventListener('drop', (e)=>{
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const dt = e.dataTransfer;
        if(!dt) return;
        const files = dt.files;
        // merge existing files
        const existing = Array.from(fileInput.files || []);
        const merged = new DataTransfer();
        existing.forEach(f=> merged.items.add(f));
        Array.from(files).forEach(f=> merged.items.add(f));
        fileInput.files = merged.files;
        renderFiles(fileInput.files);
      });

    })();
});
// main.html Animations
document.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.2
    }
  );

  // Observe document cards and empty states
  document.querySelectorAll(".doc-card, .empty-card").forEach(el => observer.observe(el));
});
