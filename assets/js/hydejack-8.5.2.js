
(function(w, d) {
  'use strict';

  var pushState = history.pushState;
  var replaceState = history.replaceState;

  function setupSearch() {
    var searchInput = d.querySelector('#_search input');
    if(!searchInput) return;

    searchInput.addEventListener('input', function(e) {
      var value = e.target.value;
      // Implement search logic here
      console.log('Searching for:', value);
    });
  }

  w.addEventListener('load', function() {
    setupSearch();
  });

  // Export
  w.loadJSDeferred = function(src) {
    return new Promise(function(resolve, reject) {
      var script = d.createElement('script');
      script.src = src;
      script.onload = resolve;
      script.onerror = reject;
      d.head.appendChild(script);
    });
  };
})(window, document);
