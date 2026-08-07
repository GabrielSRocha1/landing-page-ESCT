/* Service Worker — E.S.C.T / Escoteiro Coin
   Bump VERSION to invalidate every cache on the next deploy. */
const VERSION  = 'esct-v1';
const PRECACHE = 'precache-' + VERSION;
const RUNTIME  = 'runtime-'  + VERSION;

/* The page itself is precached so the app shell opens offline. */
const PRECACHE_URLS = [
  '/',
  '/manifest.webmanifest',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  '/icons/maskable-192.png',
  '/icons/maskable-512.png',
  '/icons/apple-touch-icon.png',
  '/icons/favicon-32.png',
  '/esct-favicon-lp.png'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(PRECACHE).then(function (cache) {
      // Added one by one: a single 404 in addAll() would reject the whole install.
      return Promise.all(PRECACHE_URLS.map(function (url) {
        return cache.add(new Request(url, { cache: 'reload' })).catch(function () {});
      }));
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (names) {
      return Promise.all(names.map(function (n) {
        if (n !== PRECACHE && n !== RUNTIME) return caches.delete(n);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

function isFontHost(url) {
  return url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com';
}

self.addEventListener('fetch', function (event) {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  /* Vercel Analytics must always hit the network — never cache or replay it. */
  if (url.pathname.indexOf('/_vercel') === 0) return;

  /* Navigations: network-first, so an online visitor always gets fresh HTML,
     with the precached shell as the offline fallback. */
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).then(function (res) {
        const copy = res.clone();
        caches.open(PRECACHE).then(function (c) { c.put('/', copy); });
        return res;
      }).catch(function () {
        return caches.match('/', { ignoreSearch: true }).then(function (hit) {
          return hit || Response.error();
        });
      })
    );
    return;
  }

  /* Google Fonts: stale-while-revalidate. */
  if (isFontHost(url)) {
    event.respondWith(
      caches.open(RUNTIME).then(function (cache) {
        return cache.match(req).then(function (hit) {
          const net = fetch(req).then(function (res) {
            if (res && (res.ok || res.type === 'opaque')) cache.put(req, res.clone());
            return res;
          }).catch(function () { return hit; });
          return hit || net;
        });
      })
    );
    return;
  }

  if (url.origin !== self.location.origin) return;

  /* Same-origin assets: cache-first, filling the runtime cache on miss. */
  event.respondWith(
    caches.match(req).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        if (res && res.ok && res.type === 'basic') {
          const copy = res.clone();
          caches.open(RUNTIME).then(function (c) { c.put(req, copy); });
        }
        return res;
      });
    })
  );
});

/* Lets the page trigger an immediate update via postMessage. */
self.addEventListener('message', function (event) {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});
