
(function(w, d) {
  'use strict';

  w.loadJSDeferred = function(src) {
    return new Promise(function(resolve, reject) {
      var script = d.createElement('script');
      script.src = src;
      script.onload = resolve;
      script.onerror = reject;
      
      function insert() {
        d.body.appendChild(script);
      }

      if (d.readyState === 'loading') {
        d.addEventListener('DOMContentLoaded', insert);
      } else {
        insert();
      }
    });
  };

  var pushState = history.pushState;
  var replaceState = history.replaceState;

  function setupSearch() {
    var searchInput = d.querySelector('#_search input');
    if(!searchInput) return;

    searchInput.addEventListener('input', function(e) {
      var value = e.target.value;
      console.log('Searching for:', value);
    });
  }

  w.addEventListener('load', function() {
    setupSearch();
  });

})(window, document);
