document.documentElement.classList.add('js');
// Application links reveal the referenced explanation, including deep links.
const revealApplication = (hash) => {
  if (!hash || hash === '#') return;
  const target = document.getElementById(hash.slice(1));
  if (target && target.matches('details.application-detail')) target.open = true;
};
revealApplication(window.location.hash);
window.addEventListener('hashchange', () => revealApplication(window.location.hash));
document.querySelector('.application-guide')?.addEventListener('click', (event) => {
  const link = event.target.closest('a[href^="#"]');
  if (link) revealApplication(link.getAttribute('href'));
});
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
