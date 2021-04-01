// Doesn't work in IE11, this is a progressive enhancement
class ProgressBar {
    static selector() {
        return '[data-progress-bar]';
    }

    constructor(node) {
        this.node = node;
        this.init();
    }

    init() {
        document.addEventListener(
            'scroll',
            () => {
                const scrollTop =
                    document.documentElement.scrollTop ||
                    document.body.scrollTop;
                const scrollBottom =
                    (document.documentElement.scrollHeight ||
                        document.body.scrollHeight) -
                    document.documentElement.clientHeight;
                const scrollPercent = `${(scrollTop / scrollBottom) * 100}%`;
                this.node.style.setProperty('--scroll', scrollPercent);
            },
            { passive: true },
        );
    }
}

export default ProgressBar;
