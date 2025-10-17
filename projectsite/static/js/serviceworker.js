self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function(cache) {
            return cache.addAll([
                '/',
                '/static/css/bootstrap.min.css',
                '/static/js/main.js',
                '/static/img/pweypwey.png',
                'css/bootstrap.min.css',
                'css/ready.css',
                'css/demo.css',
                'css/demo.css',
                'newcssstyle/style.css',
            ]);
        })
    );
});
self.addEventListener('fetch', function(e) {
     e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});