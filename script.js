// Typed terminal command effect
const typedEl = document.getElementById('typed');
const commandText = 'git log --oneline --reverse';
let i = 0;

function typeChar(){
  if(i <= commandText.length){
    typedEl.textContent = commandText.slice(0, i);
    i++;
    setTimeout(typeChar, 45);
  }
}

if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  typedEl.textContent = commandText;
} else {
  typeChar();
}

// Expand/collapse commit entries
document.querySelectorAll('.commit').forEach((commit) => {
  const row = commit.querySelector('.commit-row');
  const toggle = commit.querySelector('.toggle');

  row.addEventListener('click', () => {
    const isOpen = commit.classList.toggle('open');
    toggle.textContent = isOpen ? 'collapse ▴' : 'expand ▾';
  });
});

// Open the first commit by default so the page isn't empty on load
const first = document.querySelector('.commit');
if(first){
  first.classList.add('open');
  first.querySelector('.toggle').textContent = 'collapse ▴';
}
