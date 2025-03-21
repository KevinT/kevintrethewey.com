
(function() {
  function displaySearchResults(results, store) {
    const searchResults = document.getElementById('search-results');
    if (!searchResults) return;

    if (results.length) {
      let resultList = '';
      for (const n in results) {
        const item = store[results[n].ref];
        resultList += `
          <li>
            <h3><a href="${item.url}">${item.title}</a></h3>
            <p>${item.content.substring(0, 150)}...</p>
          </li>
        `;
      }
      searchResults.innerHTML = resultList;
    } else {
      searchResults.innerHTML = '<li>No results found</li>';
    }
  }

  function getQueryVariable(variable) {
    const query = window.location.search.substring(1);
    const vars = query.split('&');
    for (let i = 0; i < vars.length; i++) {
      const pair = vars[i].split('=');
      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  const searchTerm = getQueryVariable('query');
  if (searchTerm) {
    document.getElementById('search-box').setAttribute("value", searchTerm);
    const idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('content');
      for (const key in window.store) {
        this.add({
          'id': key,
          'title': window.store[key].title,
          'content': window.store[key].content
        });
      }
    });
    const results = idx.search(searchTerm);
    displaySearchResults(results, window.store);
  }
})();
