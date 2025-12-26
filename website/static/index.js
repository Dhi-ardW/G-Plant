
// notifikasi
function openModal() {
      document.getElementById('modal').classList.remove('hidden')
    }

function closeModal() {
      document.getElementById('modal').classList.add('hidden')
    }


// menu 
profile = document.getElementById('profile');
menu = document.getElementById('menu')

profile.addEventListener('click', () => {
  menu.classList.toggle('active');
})

document.addEventListener('click', function(e) {
  if(!profile.contains(e.target) && !menu.contains(e.target)) {
     menu.classList.remove('active');
  }
})
