import MobileMenu from './mobile-menu';

describe('MobileMenu', () => {
    beforeEach(() => {
        document.body.innerHTML = `
            <button class="button button-menu-toggle" data-mobile-menu-toggle />
            <div class="header__menus header__menus--mobile" data-mobile-menu />
        `;
    });

    it('hides the menu by default', () => {
        // eslint-disable-next-line no-new
        new MobileMenu(document.querySelector(MobileMenu.selector()));

        expect(document.querySelector('[data-mobile-menu]').className).toBe(
            'header__menus header__menus--mobile',
        );
    });

    it('calls the open callback and shows the menu when clicked', () => {
        const openCb = jest.fn();

        // eslint-disable-next-line no-new
        new MobileMenu(document.querySelector(MobileMenu.selector()), openCb);

        const button = document.querySelector('[data-mobile-menu-toggle]');
        button.dispatchEvent(new Event('click'));

        expect(button.className).toBe('button button-menu-toggle is-open');
        expect(openCb).toHaveBeenCalled();
    });

    it('calls the close callback and hides then menu when clicked once open', () => {
        const closeCb = jest.fn();

        // eslint-disable-next-line no-new
        new MobileMenu(
            document.querySelector(MobileMenu.selector()),
            () => {},
            closeCb,
        );

        const button = document.querySelector('[data-mobile-menu-toggle]');
        button.dispatchEvent(new Event('click'));
        button.dispatchEvent(new Event('click'));

        expect(button.className).toBe('button button-menu-toggle');
        expect(closeCb).toHaveBeenCalled();
    });
});
