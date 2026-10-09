document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-navigation');
const brandMenu = document.querySelector('.brand-menu');
if (brandMenu) {
  document.addEventListener('click', (event) => {
    if (!brandMenu.contains(event.target)) brandMenu.open = false;
  });
  brandMenu.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !brandMenu.contains(event.relatedTarget)) brandMenu.open = false;
  });
}
if (menuButton && navigation) {
  const setMenu = (open) => {
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.dataset.open = String(open);
    menuButton.querySelector('span').textContent = open ? 'Close' : 'Menu';
    if (!open && brandMenu) brandMenu.open = false;
  };
  menuButton.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    if (brandMenu && brandMenu.open) {
      brandMenu.open = false;
      brandMenu.querySelector('summary').focus();
    } else if (menuButton.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      menuButton.focus();
    }
  });
  window.matchMedia('(min-width: 981px)').addEventListener('change', () => setMenu(false));
}
