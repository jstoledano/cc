// JavaScript necesario para el funcionamiento de la navbar en index.html
// y para el funcionamiento de la galería de imágenes en gallery.html
// Se utiliza el framework Materialize para el diseño de la página
// y la librería Lightbox para la galería de imágenes

// Navbar
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});

// Código para mostar y ocultar el menu Servicios en la navbar
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});