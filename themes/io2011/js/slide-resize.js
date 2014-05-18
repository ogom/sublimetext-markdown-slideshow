/**
 * slide-resize
 */
(function() {
  var slides = null,
      timer = null;

  var width = 1200,
      height = 700,
      wait = 10;

  var transform = function() {
    clearTimeout(timer);
    timer = setTimeout(function() {
      if (width > window.innerWidth || height > window.innerHeight) {
        var ratio = Math.min(window.innerWidth / width, window.innerHeight / height)
        var transform = 'scale(' + ratio + ')';

        slides.style.transform = transform;
        slides.style.OTransform = transform;
        slides.style.msTransform = transform;
        slides.style.MozTransform = transform;
        slides.style.WebkitTransform = transform;
      }
    }, wait);
  };

  var resize = function() {
    slides = document.getElementsByTagName('section')[0];
    if (width < slides.offsetWidth) width = slides.offsetWidth
    if (height < slides.offsetHeight) height = slides.offsetHeight

    transform();
    window.addEventListener('resize', transform);
  };

  window.addEventListener('load', resize);
})();
