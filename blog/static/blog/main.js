const nav_links = document.querySelectorAll('#siteheader .navbar-nav a');
for (const nav_link of nav_links) {
    if (nav_link.pathname == window.location.pathname){
        nav_link.classList.add('active');
    }
}

// function click_func() {
//     let nav_active = document.querySelectorAll('#siteheader .navbar-nav a.active')[0];
//     nav_active.classList.remove('active');
//     this.classList.add('active');
// }
// const nav_links = document.querySelectorAll('#siteheader .navbar-nav a');
// for (const nav_link of nav_links) {
//     nav_link.addEventListener('click', click_func);
// }