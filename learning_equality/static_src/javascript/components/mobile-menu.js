class MobileMenu {
    static selector() {
        return '[data-mobile-menu-toggle]';
    }

    constructor(node, openCb = () => {}, closeCb = () => {}) {
        this.node = node;

        // Any callbacks to be called on open or close.
        this.openCb = openCb;
        this.closeCb = closeCb;

        this.state = {
            open: false,
        };

        this.bindEventListeners();
    }

    bindEventListeners() {
        this.node.addEventListener('click', () => {
            this.toggle();
        });
    }

    toggle() {
        if (this.state.open) {
            this.close();
        } else {
            this.open();
        }
    }

    open() {
        this.node.classList.add('is-open');
        this.openCb();

        this.state.open = true;
    }

    close() {
        this.node.classList.remove('is-open');
        this.closeCb();

        this.state.open = false;
    }
}

export default MobileMenu;
