(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl;
    (el instanceof HTMLElement) ? selectEl = el : selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Mobile nav toggle
   */
  const toogleNav = function () {
    let navButton = select('.nav-toggle')
    navButton.classList.toggle('nav-toggle-active')
    navButton.querySelector('i').classList.toggle('bx-x')
    navButton.querySelector('i').classList.toggle('bx-menu')

    select('.nav-menu').classList.toggle('nav-menu-active')
  }
  on('click', '.nav-toggle', function (e) {
    toogleNav();
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.nav-menu .drop-down > a', function (e) {
    e.preventDefault()
    this.nextElementSibling.classList.toggle('drop-down-active')
    this.parentElement.classList.toggle('active')
  }, true)

  /**
   * Scrool links with a class name .scrollto
   */
  on('click', '.scrollto', function (e) {
    if (select(this.hash)) {
      select('.nav-menu .active').classList.remove('active')
      this.parentElement.classList.toggle('active')
      toogleNav();
    }
  }, true)

  const copyUrlBtn = select('#copy_url_btn')
  const inputEl = select('#shorten_url_input')
  on('submit', '#shorten_url_form', async function (e) {
    e.preventDefault()
    const errorEl = select('#shorten_url_error')
    const submitBtn = select('#shorten_url_btn')
    const copyUrlBtn = select('#copy_url_btn')
    const followNum = select('#shorten_url_number')

    const formData = new FormData(e.target)
    const url = formData.get('url')
    try {
      errorEl.textContent = ''
      const shortUrl = await document.linkShortener.makeShortLink(url)
      inputEl.value = shortUrl.short_link
      submitBtn.classList.add('hidden')
      copyUrlBtn.classList.remove('hidden')
      if (shortUrl.is_created === false) {
        followNum.textContent = shortUrl.follows
        followNum.classList.remove('hidden')
      }
    } catch (e) {
      errorEl.textContent = e
    }
  })

  on('click', copyUrlBtn, function () {
    inputEl.focus()
    inputEl.select()
    try {
      document.execCommand('copy');
    } catch {
      navigator.clipboard.writeText(inputEl.value).then()
    }
  })
})();