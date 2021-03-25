const host = process.env.PROXY_HOST || 'localhost';
const port = process.env.PROXY_PORT || '8000';

module.exports = {
    proxy: {
        target: `${host}:${port}`,
        proxyOptions: {
            changeOrigin: false,
        },
    },
    serveStatic: [
        {
            route: '/static',
            dir: 'learning_equality/static_compiled',
        },
    ],
    files: 'learning_equality/static_compiled',
};
