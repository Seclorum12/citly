(function () {
  "use strict";
  document.linkShortener = {}

  async function postMakeShortLink(long_url) {
    const response = await fetch(window.location.origin + '/api/links/make-short-link', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        link: long_url
      })
    })
    return await response.json()
  }

  async function makeShortLink(long_url) {
    validateUrl(long_url)
    return await postMakeShortLink(long_url)
  }

  function validateUrl(long_url) {
    let url;
    try {
      url = new URL(long_url);
    } catch {
      throw "Invalid URL"
    }
    if (url.hostname === window.location.hostname) throw "Link is from Citly"
  }

  document.linkShortener.makeShortLink = makeShortLink
})();